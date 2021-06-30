import random


class Utils:
    """A class with utility functions."""

    def __init__(self):
        pass

    @staticmethod
    def get_random_video(videos):
        """Return video with at a random index."""
        if videos:  # If not empty
            return videos[random.randint(0, len(videos) - 1)]
        else:  # If the list is empty
            return None
