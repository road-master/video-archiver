from pathlib import Path

import ffmpeg
import requests
from requests.cookies import RequestsCookieJar

from videoarchiver import CONFIG
from videoarchiver.abstract_client_for_back_end import AbstractClientForBackEnd
from videoarchiver.cookie_converter import CookieConverter


class ClientForBackEnd(AbstractClientForBackEnd):
    HOST_NAME = "account.nicovideo.jp"
    BASE_URL = "https://" + HOST_NAME
    SLASH = "/"
    API_LOGIN = "api/v1/login"

    @classmethod
    def login(cls) -> RequestsCookieJar:
        data = {
            "LOGIN_ID": CONFIG.niconico.mail_address,
            "PASSWORD": CONFIG.niconico.password,
        }
        response = requests.post(
            ClientForBackEnd.BASE_URL + ClientForBackEnd.SLASH + ClientForBackEnd.API_LOGIN,
            data=data,
            allow_redirects=False,
        )
        response.raise_for_status()
        return response.cookies

    @classmethod
    def ffmpeg(cls, uri: str, cookies_streaming: RequestsCookieJar, path_file: Path):
        cookies_string = CookieConverter.convert_requests_cookie_jar_to_string(cookies_streaming)
        stream = ffmpeg.input(uri, headers=f"Cookie: {cookies_string}\r\n", copytb="1")
        stream = ffmpeg.output(stream, str(path_file), f="mp4", c="copy")
        ffmpeg.run(stream)
