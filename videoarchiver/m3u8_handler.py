from typing import Optional

from m3u8 import M3U8, Playlist


class M3U8Handler:
    @classmethod
    def extract_highest_quality_streaming_url(cls, m3u8_object: M3U8) -> Playlist:
        playlist_highest_quality: Optional[Playlist] = None
        for playlist in m3u8_object.playlists:
            playlist_highest_quality = cls.return_higher_quality(playlist_highest_quality, playlist)

        return playlist_highest_quality

    @staticmethod
    def return_higher_quality(playlist_a: Playlist, playlist_b: Playlist) -> Playlist:
        if playlist_a is None or playlist_a.stream_info.bandwidth < playlist_b.stream_info.bandwidth:
            return playlist_b
        return playlist_a
