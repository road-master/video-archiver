import os
from pathlib import Path

from requests.cookies import RequestsCookieJar

from videoarchiver.m3u8_handler import M3U8Handler
from videoarchiver.tvasahi.path_builder import PathBuilder
from videoarchiver.tvasahi.client_for_back_end import ClientForBackEnd
from videoarchiver.tvasahi.html_analyzer import HtmlAnalyzer
from videoarchiver.tvasahi.models import Episode


class EpisodeMediaArchiver:
    def __init__(self, episode: Episode, path_directory_download: Path):
        self.episode = episode
        self.path_archive_directory = PathBuilder.build_archive_directory(path_directory_download, episode)
        os.makedirs(str(self.path_archive_directory), exist_ok=True)

    def archive_large_image_if_has_not_archived(self):
        self.archive_image_if_has_not_archived(self.episode.large_image_url)

    def archive_extra_large_image_if_has_not_archived(self):
        self.archive_image_if_has_not_archived(self.episode.extra_large_image_url)

    def archive_image_if_has_not_archived(self, url: str):
        path = PathBuilder.build_archive_image_file(self.path_archive_directory, url)
        if path.exists():
            print(f'Image is already archived. file = {str(path)}')
            return
        with path.open("wb") as file_image:
            file_image.write(ClientForBackEnd.download(url))

    def archive_video_if_has_not_archived(self, cookies_login: RequestsCookieJar):
        path_file = self.path_archive_directory / f'{self.episode.episode_name_for_windows_path}.mp4'
        if path_file.exists():
            print(f'Video is already archived. file = {str(path_file)}')
            return
        soup = ClientForBackEnd.request_episode_page(self.episode, cookies_login)
        url_playlist = HtmlAnalyzer.extract_url_playlist(soup)
        cookies_streaming = ClientForBackEnd.request_cookies(url_playlist)
        m3u8_object = ClientForBackEnd.request_playlist(url_playlist)
        playlist_highest_quality = M3U8Handler.extract_highest_quality_streaming_url(m3u8_object)
        ClientForBackEnd.ffmpeg(playlist_highest_quality, cookies_streaming, path_file)
