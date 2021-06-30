"""A video player class."""

from .video_library import VideoLibrary
from .utils import Utils


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()  # "_" to enforce encapsulation
        self._currently_playing_video = None
        self._currently_paused_video = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos()
                         )  # Returns a list
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = sorted(self._video_library.get_all_videos(),  # Sort by title
                        key=lambda video: video.title)
        print("Here's a list of all available videos:")
        for video in videos:
            formatted_tags = Utils.format_tags(video)
            print(f" {video.title} ({video.video_id}) {formatted_tags}")

    def play_video(self, video_id):
        video = self._video_library.get_video(video_id)
        if not video:  # No video
            print("Cannot play video: Video does not exist")
        elif self._currently_playing_video is not None:  # A video is already playing
            print(f"Stopping video: {self._currently_playing_video.title}")
            self._currently_playing_video = video  # Re-adjust
            print(f"Playing video: {video.title}")
        else:  # Normal case
            self._currently_playing_video = video
            print(f"Playing video: {video.title}")

    def stop_video(self):
        """Stops the current video."""
        if self._currently_playing_video:  # Stop if it is already playing
            print(f"Stopping video: {self._currently_playing_video.title}")
            # We stopped it, nothing is playling anymore
            self._currently_playing_video = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        videos = self._video_library.get_all_videos()  # List
        random_video = Utils.get_random_video(videos)
        if random_video is None:
            print("No videos available")
        elif self._currently_playing_video:
            print(f"Stopping video: {self._currently_playing_video.title}")
            print(f"Playing video: {random_video.title}")
        else:  # Just get the random video
            print(f"Playing video: {random_video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if not self._currently_playing_video:
            print("Cannot pause video: No video is currently playing")
        elif self._currently_paused_video is not None:  # = IS PAUSED
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
        elif self._currently_paused_video:
            formatted_tags = Utils.format_tags(
                self._currently_paused_video)  # Get the tags
            print(
                f"Currently playing: {self._currently_paused_video.title} ({self._currently_paused_video.video_id}) {formatted_tags} - PAUSED")
        else:  # Normal case
            formatted_tags = Utils.format_tags(
                self._currently_playing_video)
            print(
                f"Currently playing: {self._currently_playing_video.title} ({self._currently_playing_video.video_id}) {formatted_tags}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

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
