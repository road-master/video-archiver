from unittest.mock import patch

from tests.testlibraries.instance_resource import PATH_VIDEO_OUTPUT, FILE_HTML_EPISODE, BINARY_JPEG_EXAMPLE, \
    COOKIES_STREAMING_EXAMPLE, EPISODE_EXAMPLE, EXTRA_LARGE_IMAGE_URL_EXAMPLE, URL_PLAYLIST, URI_EXAMPLE, \
    M3U8_CONTENT_EXAMPLE, PATH_FILE
from tests.testlibraries.stream_factory import StreamFactory
from videoarchiver.tvasahi.episode_media_archiver import EpisodeMediaArchiver


class TestEpisodeMediaArchiver:
    @staticmethod
    def test_archive_image_if_has_not_archived(requests_mock, tmp_path):
        requests_mock.get(
            f'https://mv.tv-asahi.co.jp/douga{EXTRA_LARGE_IMAGE_URL_EXAMPLE}', content=BINARY_JPEG_EXAMPLE
        )
        EpisodeMediaArchiver(EPISODE_EXAMPLE, tmp_path).archive_image_if_has_not_archived(EXTRA_LARGE_IMAGE_URL_EXAMPLE)
        assert (
            tmp_path / PATH_VIDEO_OUTPUT / 'a4230f0775b8d8d252e9e530c7ed883b_extra_large.jpg'
        ).read_bytes() == BINARY_JPEG_EXAMPLE

    @staticmethod
    @patch(StreamFactory.RUN)
    def test_archive_video_if_has_not_archived(mocked_run, requests_mock, tmp_path):
        requests_mock.get('https://mv.tv-asahi.co.jp/douga/tgs/142', text=FILE_HTML_EPISODE.read_text(encoding='utf-8'))
        requests_mock.get(URL_PLAYLIST, cookies=COOKIES_STREAMING_EXAMPLE, text=M3U8_CONTENT_EXAMPLE)
        EpisodeMediaArchiver(EPISODE_EXAMPLE, tmp_path).archive_video_if_has_not_archived(COOKIES_STREAMING_EXAMPLE)
        mocked_run.assert_called_once_with(
            StreamFactory.create_stream_expect(COOKIES_STREAMING_EXAMPLE, tmp_path / PATH_FILE, URI_EXAMPLE)
        )
