from dataclasses import dataclass, asdict
from pathlib import Path

# ↓ ffmpeg-python causes DeprecationWarning
import ffmpeg
from bs4 import BeautifulSoup
import m3u8
from m3u8 import M3U8, Playlist
import requests
from requests import Response
from requests.cookies import RequestsCookieJar

from videoarchiver import CONFIG
from videoarchiver.abstract_client_for_back_end import AbstractClientForBackEnd
from videoarchiver.cookie_converter import CookieConverter
from videoarchiver.tvasahi.models import Episode


@dataclass
class Payload:
    key: int
    limit: int
    sort: int
    page: int = 1
    bought: int = 1


class ClientForBackEnd(AbstractClientForBackEnd):
    HOST_NAME = 'mv.tv-asahi.co.jp'
    BASE_URL = 'https://' + HOST_NAME
    BASE_URL_DIRECTORY = BASE_URL + '/douga'
    SLASH = '/'
    API_LIST_EPISODES = 'api/list/episodes'

    @classmethod
    def login(cls) -> RequestsCookieJar:
        data = {
            'LOGIN_ID': CONFIG.tv_asahi.mail_address,
            'PASSWORD': CONFIG.tv_asahi.password,
        }
        response = requests.post(ClientForBackEnd.BASE_URL_DIRECTORY + '/login.php', data=data, allow_redirects=False)
        response.raise_for_status()
        return response.cookies

    @classmethod
    def request_program_home_page(cls, program_id_string: str) -> BeautifulSoup:
        return cls.request_html(
            cls.BASE_URL_DIRECTORY + cls.SLASH + program_id_string,
            program_id_string
        )

    @classmethod
    def request_episode_page(cls, episode: Episode, cookies_login: RequestsCookieJar) -> BeautifulSoup:
        return cls.request_html(
            cls.BASE_URL_DIRECTORY + cls.SLASH + episode.directory + cls.SLASH + str(episode.episode_num),
            episode.directory,
            cookies_login
        )

    @classmethod
    def request_html(cls, request_url: str, program_id_string: str, cookies: RequestsCookieJar = None) -> BeautifulSoup:
        print('request = ' + request_url)
        headers = {
            'Referer': cls.BASE_URL_DIRECTORY + cls.SLASH + program_id_string,
            'Origin': cls.BASE_URL
        }
        response = requests.get(request_url, headers=headers, cookies=cookies)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    @classmethod
    def request_cookies(cls, request_url: str) -> RequestsCookieJar:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.cookies

    @classmethod
    def request_playlist(cls, request_url: str) -> M3U8:
        response: Response = requests.get(request_url)
        response.raise_for_status()
        print(response.text)
        return m3u8.loads(response.text, response.request.url)

    @classmethod
    def request_api_list_episode(cls, program_id_string: str, payload: Payload) -> dict:
        request_url = cls.BASE_URL_DIRECTORY + cls.SLASH + cls.API_LIST_EPISODES
        print('request = ' + request_url)
        headers = {'Referer': cls.BASE_URL_DIRECTORY + cls.SLASH + program_id_string + cls.SLASH + 'episodes'}
        response = requests.get(request_url, params=asdict(payload), headers=headers)
        response.raise_for_status()
        return response.json()

    @classmethod
    def download(cls, url: str):
        response = requests.get(cls.BASE_URL_DIRECTORY + url)
        response.raise_for_status()
        return response.content

    @classmethod
    def ffmpeg(cls, playlist: Playlist, cookies_streaming: RequestsCookieJar, path_file: Path):
        cookies_string = CookieConverter.convert_requests_cookie_jar_to_string(cookies_streaming)
        stream = ffmpeg.input(playlist.uri, headers=f'Cookie: {cookies_string}\r\n', copytb='1')
        stream = ffmpeg.output(stream, str(path_file), f='mp4', c='copy')
        ffmpeg.run(stream)
