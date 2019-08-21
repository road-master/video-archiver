from pathlib import Path

from tests.testlibraries.instance_resource import PATH_VIDEO_OUTPUT, EPISODE_EXAMPLE, EXTRA_LARGE_IMAGE_URL_EXAMPLE, \
    InstanceResource
from videoarchiver import Directory
from videoarchiver.tvasahi.path_builder import PathBuilder


class TestPathBuilder:
    @staticmethod
    def test_build_path_archive_directory():
        assert PathBuilder.build_archive_directory(
            Directory.DOWNLOAD.value, EPISODE_EXAMPLE
        ) == InstanceResource.PATH_PROJECT_HOME / 'videooutput' / PATH_VIDEO_OUTPUT

    @staticmethod
    def test_build_archive_path_for_image():
        assert PathBuilder.build_archive_image_file(
            PATH_VIDEO_OUTPUT, EXTRA_LARGE_IMAGE_URL_EXAMPLE
        ) == Path(PATH_VIDEO_OUTPUT / 'a4230f0775b8d8d252e9e530c7ed883b_extra_large.jpg')
