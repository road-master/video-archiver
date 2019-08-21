from unittest.mock import patch

from bs4 import BeautifulSoup
import m3u8
from m3u8 import Playlist

from tests.testlibraries.additional_matcher_factory import AdditionalMatcherFactory
from tests.testlibraries.instance_resource import FILE_PLAYLIST_TEST_DATA, FILE_HTML_PROGRAM_HOME, FILE_HTML_EPISODE, \
    BINARY_JPEG_EXAMPLE, COOKIES_DICTIONARY_LOGIN_EXAMPLE, COOKIES_LOGIN_EXAMPLE, COOKIES_STREAMING_EXAMPLE, \
    EPISODE_EXAMPLE, EXTRA_LARGE_IMAGE_URL_EXAMPLE, URL_PLAYLIST, URI_EXAMPLE, M3U8_CONTENT_EXAMPLE, PATH_FILE
from tests.testlibraries.stream_factory import StreamFactory
from videoarchiver.tvasahi.client_for_back_end import ClientForBackEnd, Payload


class TestClientForBackEnd:
    @staticmethod
    def test_login(requests_mock):
        mail_address = 'mail@address.tv.asahi'
        password = 'password_tv_asahi'
        requests_mock.post(
            'https://mv.tv-asahi.co.jp/douga/login.php',
            # allow_redirects=False,
            cookies=COOKIES_LOGIN_EXAMPLE,
            additional_matcher=AdditionalMatcherFactory.create_request_data_matcher(
                {'LOGIN_ID': mail_address, 'PASSWORD': password}
            )
        )
        assert ClientForBackEnd.login() == COOKIES_LOGIN_EXAMPLE

    @staticmethod
    def test_request_program_home_page(requests_mock):
        html_episode = FILE_HTML_EPISODE.read_text(encoding='utf-8')
        program_id_string = 'tgs'
        requests_mock.get(
            f'https://mv.tv-asahi.co.jp/douga/{program_id_string}',
            text=html_episode,
            headers={
                'Referer': f'https://mv.tv-asahi.co.jp/douga/{program_id_string}',
                'Origin': 'https://mv.tv-asahi.co.jp',
            },
            cookies=None
        )
        assert ClientForBackEnd.request_program_home_page(
            program_id_string
        ) == BeautifulSoup(html_episode, "html.parser")

    @staticmethod
    def test_request_episode_home_page(requests_mock):
        html_program_home = FILE_HTML_PROGRAM_HOME.read_text(encoding='utf-8')
        requests_mock.get(
            f'https://mv.tv-asahi.co.jp/douga/{EPISODE_EXAMPLE.directory}/{str(EPISODE_EXAMPLE.episode_num)}',
            text=html_program_home,
            headers={
                'Referer': f'https://mv.tv-asahi.co.jp/douga/{EPISODE_EXAMPLE.directory}',
                'Origin': 'https://mv.tv-asahi.co.jp',
            },
            cookies=COOKIES_DICTIONARY_LOGIN_EXAMPLE
        )
        assert ClientForBackEnd.request_episode_page(
            EPISODE_EXAMPLE, COOKIES_DICTIONARY_LOGIN_EXAMPLE
        ) == BeautifulSoup(html_program_home, "html.parser")

    @staticmethod
    def test_request_html(requests_mock):
        request_url = 'https://mv.tv-asahi.co.jp/douga/tgs'
        html_program_home = FILE_HTML_PROGRAM_HOME.read_text(encoding='utf-8')
        program_id_string = 'tgs'
        requests_mock.get(
            request_url,
            text=html_program_home,
            headers={
                'Referer': f'https://mv.tv-asahi.co.jp/douga/{program_id_string}',
                'Origin': 'https://mv.tv-asahi.co.jp',
            },
            cookies=COOKIES_DICTIONARY_LOGIN_EXAMPLE
        )
        assert ClientForBackEnd.request_html(
            request_url, program_id_string, COOKIES_DICTIONARY_LOGIN_EXAMPLE
        ) == BeautifulSoup(html_program_home, "html.parser")

    @staticmethod
    def test_request_cookie(requests_mock):
        requests_mock.get(URL_PLAYLIST, cookies=COOKIES_STREAMING_EXAMPLE)
        cookies = ClientForBackEnd.request_cookies(URL_PLAYLIST)
        assert cookies == COOKIES_STREAMING_EXAMPLE

    @staticmethod
    def test_request_playlist(requests_mock):
        requests_mock.get(URL_PLAYLIST, text=M3U8_CONTENT_EXAMPLE)
        expected = m3u8.loads(FILE_PLAYLIST_TEST_DATA.read_text(), URL_PLAYLIST)
        actual = ClientForBackEnd.request_playlist(URL_PLAYLIST)
        assert actual.dumps() == expected.dumps()

    @staticmethod
    def test_request_api_list_episode(requests_mock):
        program_id_string = 'tgs'
        program_code = 332
        limit = 12
        sort = 12
        params = {
            'key': program_code,
            'limit': limit,
            'sort': sort,
            'page': 1,
            'bought': 1,
        }
        json_example = {'content': 'json'}
        requests_mock.get(
            'https://mv.tv-asahi.co.jp/douga/api/list/episodes?' + '&'.join(
                [f'{key}={value}' for key, value in params.items()]
            ),
            request_headers={'Referer': f'https://mv.tv-asahi.co.jp/douga/{program_id_string}/episodes'},
            json=json_example
        )
        assert ClientForBackEnd.request_api_list_episode(
            program_id_string, Payload(program_code, limit, sort)
        ) == json_example

    @staticmethod
    def test_download(requests_mock):
        requests_mock.get(
            f'https://mv.tv-asahi.co.jp/douga{EXTRA_LARGE_IMAGE_URL_EXAMPLE}',
            content=BINARY_JPEG_EXAMPLE
        )
        assert ClientForBackEnd.download(EXTRA_LARGE_IMAGE_URL_EXAMPLE) == BINARY_JPEG_EXAMPLE

    @staticmethod
    @patch(StreamFactory.RUN)
    def test_ffmpeg(mocked_run):
        playlist = Playlist(URI_EXAMPLE, {'bandwidth': 2800000}, None, None)
        ClientForBackEnd.ffmpeg(playlist, COOKIES_STREAMING_EXAMPLE, PATH_FILE)
        mocked_run.assert_called_once_with(StreamFactory.create_stream_expect(
            COOKIES_STREAMING_EXAMPLE, PATH_FILE, URI_EXAMPLE
        ))
