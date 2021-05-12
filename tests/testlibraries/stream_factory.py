from pathlib import Path

# noinspection PyPackageRequirements
import ffmpeg
from requests.cookies import RequestsCookieJar

from videoarchiver.cookie_converter import CookieConverter


class StreamFactory:
    RUN = "ffmpeg.run"

    @staticmethod
    def create_stream_expect(cookies_streaming: RequestsCookieJar, path_file: Path, uri: str):
        cookies_string = CookieConverter.convert_requests_cookie_jar_to_string(cookies_streaming)
        stream = ffmpeg.input(uri, headers=f"Cookie: {cookies_string}\r\n", copytb="1")
        stream = ffmpeg.output(stream, str(path_file), f="mp4", c="copy")
        return stream
