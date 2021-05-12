from pathlib import Path
from typing import Type

from videoarchiver.abstract_client_for_back_end import AbstractClientForBackEnd


class MembershipSiteArchiveStep:
    """This class implements archiving steps for media files at some of web site."""

    def __init__(self, client_for_back_end: Type[AbstractClientForBackEnd], path_directory_download: Path):
        self.client_for_back_end = client_for_back_end
        self.cookies_login = client_for_back_end.login()
        self.path_directory_download = path_directory_download

    def execute(self) -> None:
        """This method executes all CSV converters."""
        raise NotImplementedError()
