import sys
from pathlib import Path
from typing import Type

from videoarchiver import CONFIG
from videoarchiver.membership_site_archive_step import MembershipSiteArchiveStep
from videoarchiver.tvasahi.episode_loader import EpisodeLoader
from videoarchiver.tvasahi.client_for_back_end import ClientForBackEnd
from videoarchiver.tvasahi.episode_media_archiver import EpisodeMediaArchiver


class ArchiveStep(MembershipSiteArchiveStep):
    """This class implements archiving steps for media files at some of web site."""
    def __init__(
            self,
            client_for_back_end: Type[ClientForBackEnd],
            path_directory_download: Path,
            path_directory_cache: Path,
    ):
        super().__init__(client_for_back_end, path_directory_download)
        self.episode_loader = EpisodeLoader(path_directory_cache)

    def execute(self) -> None:
        """This method executes archive step for all target programs."""
        # pylint: disable=not-an-iterable
        for program_id_string in CONFIG.tv_asahi.list_program_id:
            self.execute_per_program(program_id_string)

    def execute_per_program(self, program_id_string: str) -> None:
        """This method executes archive step per each target program."""
        list_episode = self.episode_loader.list_up_episode(
            program_id_string
        ) if len(sys.argv) >= 1 and '--no-cache' in sys.argv else self.episode_loader.load_backup(program_id_string)
        for episode in list_episode:
            media_archiver = EpisodeMediaArchiver(episode, self.path_directory_download)
            media_archiver.archive_extra_large_image_if_has_not_archived()
            media_archiver.archive_large_image_if_has_not_archived()
            media_archiver.archive_video_if_has_not_archived(self.cookies_login)
