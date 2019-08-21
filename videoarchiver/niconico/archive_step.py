from videoarchiver import CONFIG
from videoarchiver.membership_site_archive_step import MembershipSiteArchiveStep
from videoarchiver.niconico.client_for_back_end import ClientForBackEnd


class ArchiveStep(MembershipSiteArchiveStep):
    """This class implements archiving steps for media files at some of web site."""
    def execute(self) -> None:
        """This method executes archive step for all target programs."""
        # pylint: disable=not-an-iterable
        for program_id_string in CONFIG.niconico.list_program_id:
            self.execute_per_program(program_id_string)

    def execute_per_program(self, program_id_string: str) -> None:
        """This method executes archive step per each target program."""
        url_watch_page = f'https://live2.nicovideo.jp/watch/{program_id_string}'
        ClientForBackEnd.ffmpeg(
            # TODO watch ページの embed-data タグ内から 'wss' で始まる WebSocket URL を取得し、通信して m3u8 を取得、
            # TODO m3u8 Playlist 内の最も画質の良い m3u8 で ffmpeg 実行
            # TODO ↓ 現状では開発者ツールの Network タブを 'master.m3u8' で検索してリンクをコピー
            '',
            self.cookies_login,
            self.path_directory_download / f'temporary.mp4'
        )
