"""A video player class."""

from .video_library import VideoLibrary
from .utils import Utils
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._currently_playing_video = None
        self._currently_paused_video = None
        self._playlists = []
        self._playlists_names = []
        self._playlists_names_cleaned = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos()
                         )
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = sorted(self._video_library.get_all_videos(),
                        key=lambda video: video.title)
        print("Here's a list of all available videos:")
        for video in videos:
            formatted_tags = Utils.format_tags(video)
            print(f" {video.title} ({video.video_id}) {formatted_tags}")

    def play_video(self, video_id):
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
        elif self._currently_playing_video is not None:
            print(f"Stopping video: {self._currently_playing_video.title}")
            self._currently_playing_video = video
            print(f"Playing video: {video.title}")
        else:
            self._currently_playing_video = video
            print(f"Playing video: {video.title}")

    def stop_video(self):
        """Stops the current video."""
        if self._currently_playing_video:  # Stop if it is already playing
            print(f"Stopping video: {self._currently_playing_video.title}")
            self._currently_playing_video = None
            self._currently_paused_video = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        videos = self._video_library.get_all_videos()
        random_video = Utils.get_random_video(videos)
        if random_video is None:
            print("No videos available")
        elif self._currently_playing_video:
            print(f"Stopping video: {self._currently_playing_video.title}")
            print(f"Playing video: {random_video.title}")
        else:
            print(f"Playing video: {random_video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if not self._currently_playing_video:
            print("Cannot pause video: No video is currently playing")
        elif self._currently_paused_video is not None:  # Video is paused
            print(
                f"Video already paused: {self._currently_playing_video.title}")
        else:
            self._currently_paused_video = self._currently_playing_video
            print(f"Pausing video: {self._currently_playing_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if not self._currently_playing_video:
            print("Cannot continue video: No video is currently playing")
        elif self._currently_paused_video is None:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self._currently_paused_video.title}")
            self._currently_paused_video = None

    def show_playing(self):
        if not self._currently_playing_video:
            print("No video is currently playing")
        elif self._currently_paused_video is self._currently_playing_video:
            formatted_tags = Utils.format_tags(
                self._currently_paused_video)  # Get the tags
            print(
                f"Currently playing: {self._currently_paused_video.title} ({self._currently_paused_video.video_id}) {formatted_tags} - PAUSED")
        else:
            formatted_tags = Utils.format_tags(
                self._currently_playing_video)
            print(
                f"Currently playing: {self._currently_playing_video.title} ({self._currently_playing_video.video_id}) {formatted_tags}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        playlist = Playlist(playlist_name)
        if playlist.get_playlist_name().lower() in self._playlists_names_cleaned:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print(
                f"Successfully created new playlist: {playlist.get_playlist_name()}")
            self._playlists_names_cleaned.append(
                playlist.get_playlist_name().lower())
            self._playlists_names.append(playlist.get_playlist_name())
            self._playlists.append(playlist)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in self._playlists_names_cleaned:
            print(
                f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video_id not in self._video_library.get_all_video_urls():
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            # Find desired playlist by name
            playlist = self._playlists[self._playlists_names_cleaned.index(
                playlist_name.lower())]
            # Find video by id
            video = self._video_library.get_video(video_id)
            if video not in playlist.get_all_videos():
                playlist.add_video(video)
                print(f"Added video to {playlist_name}: {video.title}")
            else:
                print(
                    f"Cannot add video to {playlist_name}: Video already added")

    def show_all_playlists(self):
        """Display all playlists sorted lexicographically."""
        if len(self._playlists_names) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist_name in sorted(self._playlists_names):
                print(f" {playlist_name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name."""
        if playlist_name.lower() not in self._playlists_names_cleaned:
            print(
                f"Cannot show playlist {playlist_name}: Playlist does not exist")
        elif len(self._playlists_names_cleaned) == 0:
            print("No videos here yet")
        else:
            print(f"Showing playlist: {playlist_name}")
            # Get playlist by name, show all its videos
            playlist = self._playlists[self._playlists_names_cleaned.index(
                playlist_name.lower())]
            for video in playlist.get_all_videos():
                formatted_tags = Utils.format_tags(video)
                print(f" {video.title} ({video.video_id}) {formatted_tags}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        videos = self._playlists[self._playlists_names_cleaned.index(
            playlist_name.lower())].get_all_videos()
        is_in_videos = False
        for video in videos:
            if video.video_id == video_id:
                is_in_videos = True
        if playlist_name.lower() not in self._playlists_names_cleaned and is_in_videos == True:
            print(
                f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif playlist_name.lower() not in self._playlists_names_cleaned:
            print(
                f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif is_in_videos == True:
            print(
                f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            for video in videos:
                if video.video_id == video_id:
                    print(f"Removed video from {playlist_name}: {video.title}")
                    videos.remove(video)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
