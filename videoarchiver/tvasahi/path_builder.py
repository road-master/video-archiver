from pathlib import Path

from videoarchiver.tvasahi.models import Episode


class PathBuilder:
    @classmethod
    def build_archive_directory(cls, path_directory_cache: Path, episode: Episode):
        return path_directory_cache / episode.program_name / (
            f'{episode.episode_num:04}_{episode.episode_name_for_windows_path}'
        )

    @classmethod
    def build_archive_image_file(cls, path_archive_directory: Path, url: str):
        list_part_url = url.rsplit('/', 2)
        list_part_file_name = list_part_url[2].rsplit('.', 1)
        return path_archive_directory / f'{list_part_file_name[0]}_{list_part_url[1]}.{list_part_file_name[1]}'
