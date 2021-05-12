from datetime import datetime
from pathlib import Path

from m3u8 import Playlist
from requests.cookies import create_cookie

from tests.testlibraries.cookie_jar_factory import RequestsCookieJarFactory
from videoarchiver.tvasahi.models import Episode


class InstanceResource:
    """This class implements fixture of instance."""

    PATH_TESTS: Path = Path(__file__).parent.parent
    PATH_TEST_RESOURCES: Path = PATH_TESTS / "testresources"
    PATH_FILE_CONFIG_FOR_TEST: Path = PATH_TEST_RESOURCES / "config.yml"
    PATH_PROJECT_HOME: Path = PATH_TESTS.parent


PATH_VIDEO_OUTPUT = Path("女子流♪/0142_中野サンプラザ公演振り返り！特別生配信")
FILE_PLAYLIST_TEST_DATA: Path = InstanceResource.PATH_TEST_RESOURCES / "test.m3u8"
FILE_HTML_PROGRAM_HOME: Path = InstanceResource.PATH_TEST_RESOURCES / "test_program_home.html"
FILE_HTML_EPISODE: Path = InstanceResource.PATH_TEST_RESOURCES / "test_episode.html"
FILE_JSON_EPISODE_DATA_EXAMPLE_01: Path = InstanceResource.PATH_TEST_RESOURCES / "episodes01.json"
FILE_JSON_EPISODE_DATA_EXAMPLE_02: Path = InstanceResource.PATH_TEST_RESOURCES / "episodes02.json"
FILE_JSON_EPISODE_DATA_EXAMPLE_03: Path = InstanceResource.PATH_TEST_RESOURCES / "episodes03.json"
FILE_JAVA_SCRIPT_TEST_DATA: Path = InstanceResource.PATH_TEST_RESOURCES / "test.js"
BINARY_JPEG_EXAMPLE = (
    b"\xff\xd8\xff\xe0\x00\x10"
    b"JFIF\x00\x01\x02\x00\x00d\x00d\x00\x00\xff\xec\x00\x11"
    b"Ducky\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\xff\xee\x00\x0e"
    b"Adobe\x00d\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x1b\x1a\x1a)\x1d)"
    b"A&&AB///BG?>>?GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\x01\x1d"
    b"))4&4?((?G?5?GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
    b'\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00'
    b"K\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x01\x01"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x01\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x01\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11"
    b"\x00?\x00\xa6\x00\x1f\xff\xd9"
)
COOKIES_DICTIONARY_LOGIN_EXAMPLE = {
    "SESSID": "abcdefghij0123456789",
    "UAEUUID": "ABCDEFGHIJ01",
    "Max-Age": "0",
    "domain": ".tv-asahi.co.jp",
    "CBSESSIONID": "abcdefghij0123456789abcdef",
    "RAKUTEN_LOGIN": "deleted",
    "YAHOO_LOGIN": "deleted",
    "GOOGLE_LOGIN": "deleted",
    "FACEBOOK_LOGIN": "deleted",
    "AUTO_LOGIN_ID_ENCLYPTED": "deleted",
    "AUTO_LOGIN_PASS_ENCLYPTED": "deleted",
    "LOGIN": "2019-06-27+01%3A20%3A26",
}
COOKIES_DICTIONARY_STREAMING_EXAMPLE = {
    "uliza_iphone_auth_11495464": (
        "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
        "guid=15a03256-2346-4c46-b308-3221376d20b2&"
        "allowurl=https://www2.uliza.jp/&"
        "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
        "_expire=1561108903"
    ),
    "uliza_iphone_auth_11495462": (
        "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
        "guid=15a03256-2346-4c46-b308-3221376d20b2&"
        "allowurl=https://www2.uliza.jp/&"
        "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
        "_expire=1561108903"
    ),
    "uliza_iphone_auth_11495463": (
        "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
        "guid=15a03256-2346-4c46-b308-3221376d20b2&"
        "allowurl=https://www2.uliza.jp/&"
        "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
        "_expire=1561108903"
    ),
}
COOKIES_LOGIN_EXAMPLE = RequestsCookieJarFactory.create(
    [
        create_cookie("SESSID", "abcdefghij0123456789", domain=".tv-asahi.co.jp", path="/"),
        create_cookie("UAEUUID", "ABCDEFGHIJ01", domain=".tv-asahi.co.jp", path="/"),
        create_cookie("CBSESSIONID", "abcdefghij0123456789abcdef", domain=".tv-asahi.co.jp", path="/"),
        create_cookie("LOGIN", "2019-06-27+01%3A20%3A26", domain=".tv-asahi.co.jp", path="/"),
    ]
)
COOKIES_STREAMING_EXAMPLE = RequestsCookieJarFactory.create(
    [
        create_cookie(
            "uliza_iphone_auth_11495464",
            (
                "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
                "guid=15a03256-2346-4c46-b308-3221376d20b2&"
                "allowurl=https://www2.uliza.jp/&"
                "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
                "_expire=1561108903"
            ),
            domain="www2.uliza.jp",
            path="/IF/iphone",
        ),
        create_cookie(
            "uliza_iphone_auth_11495462",
            (
                "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
                "guid=15a03256-2346-4c46-b308-3221376d20b2&"
                "allowurl=https://www2.uliza.jp/&"
                "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
                "_expire=1561108903"
            ),
            domain="www2.uliza.jp",
            path="/IF/iphone",
        ),
        create_cookie(
            "uliza_iphone_auth_11495463",
            (
                "z8uoLuqz+G97gH91i0iFe01ognvP1KZX11H0krLY+0c=?"
                "guid=15a03256-2346-4c46-b308-3221376d20b2&"
                "allowurl=https://www2.uliza.jp/&"
                "v=11495464:1561090903,11495462:1561090903,11495463:1561090903&"
                "_expire=1561108903"
            ),
            domain="www2.uliza.jp",
            path="/IF/iphone",
        ),
    ]
)
EPISODE_EXAMPLE = Episode(
    26230,
    """5月に中野サンプラザ公演を終え、デビュー10年目を迎えた東京女子流。

4人にとっても特別な日となった「10年目のはじまり」公演を振り返り！

セットリストに込められた意味、スタッフとバトルになった楽曲選びなど…今だから話せる裏話が満載。曲中の衣装チェンジもスタジオで再現！

そして、10年目の決意を書道で表現！4者4様の決意とは。


配信日：2019年6月17日　生配信

出演者：東京女子流（山邊未夢・新井ひとみ・中江友梨・庄司芽生）""",
    datetime.strptime("2019-06-19 18:00:00", "%Y-%m-%d %H:%M:%S"),
    "tgs",
    27637,
    27637,
    "中野サンプラザ公演振り返り！特別生配信",
    142,
    "/images/episode/27637/extra_large/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    "/images/episode/27637/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    "",
    "/images/episode/27637/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    "/images/episode/27637/large/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    "/images/episode/27637/medium/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    55,
    332,
    "女子流♪",
    "/images/episode/27637/small/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    "/images/episode/27637/small_medium/a4230f0775b8d8d252e9e530c7ed883b.jpg",
    142,
    None,
)
EXTRA_LARGE_IMAGE_URL_EXAMPLE = "/images/episode/27637/extra_large/a4230f0775b8d8d252e9e530c7ed883b.jpg"
URL_PLAYLIST = (
    "https://www2.uliza.jp/IF/iphone/iPhonePlaylist.m3u8?"
    "v=2fb62d67602bce9f6e0d8b225ce4975b&p=1631&d=750&n=1422&t=eb6364aa2b0749c58859ef503f880e81&cpv=1"
)
URI_EXAMPLE = "https://ex-d.tv-asahi.co.jp/suj/iphone/750/19362_11495462_20170317185130.m3u8"
M3U8_CONTENT_EXAMPLE = """#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2800000
https://ex-d.tv-asahi.co.jp/suj/iphone/750/19362_11495462_20170317185130.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1700000
https://ex-d.tv-asahi.co.jp/suj/iphone/750/19362_11495463_20170317185130.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000
https://ex-d.tv-asahi.co.jp/suj/iphone/750/19362_11495464_20170317185130.m3u8
"""
PLAYLIST_2800000 = Playlist(
    URI_EXAMPLE,
    {
        "bandwidth": 2800000,
        "closed_captions": None,
        "average_bandwidth": None,
        "program_id": 1,
        "resolution": None,
        "codecs": None,
        "audio": None,
        "video": None,
        "subtitles": None,
    },
    [],
    "https://ex-d.tv-asahi.co.jp/suj/iphone/750/",
)
PLAYLIST_1700000 = Playlist(
    "https://ex-d.tv-asahi.co.jp/suj/iphone/750/19362_11495463_20170317185130.m3u8",
    {
        "bandwidth": 1700000,
        "closed_captions": None,
        "average_bandwidth": None,
        "program_id": 1,
        "resolution": None,
        "codecs": None,
        "audio": None,
        "video": None,
        "subtitles": None,
    },
    [],
    "https://ex-d.tv-asahi.co.jp/suj/iphone/750/",
)
PATH_FILE = Path("女子流♪/0142_中野サンプラザ公演振り返り！特別生配信/中野サンプラザ公演振り返り！特別生配信.mp4")
