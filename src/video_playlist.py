"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        self._playlist_name = playlist_name
        self._videos = []

    def get_playlist_name(self):
        """Getter."""
        return self._playlist_name

    def get_all_videos(self):
        return self._videos

    def add_video(self, video):
        """Setter."""
        self._videos.append(video)
