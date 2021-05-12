import m3u8

from tests.testlibraries.instance_resource import (
    FILE_PLAYLIST_TEST_DATA,
    PLAYLIST_1700000,
    PLAYLIST_2800000,
    URI_EXAMPLE,
    URL_PLAYLIST,
)
from videoarchiver.m3u8_handler import M3U8Handler


class TestM3U8Handler:
    @staticmethod
    def test_extract_highest_quality_streaming_url():
        m3u8_object = m3u8.loads(FILE_PLAYLIST_TEST_DATA.read_text(), URL_PLAYLIST)
        assert M3U8Handler.extract_highest_quality_streaming_url(m3u8_object).uri == URI_EXAMPLE

    @staticmethod
    def test_return_higher_quality():
        M3U8Handler.return_higher_quality(PLAYLIST_2800000, PLAYLIST_1700000)
