"""A video player class."""
from video_playlist import Playlist
from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""
    # class variable
    video_details = {}
    is_playing = 0
    current_play = "none"
    is_paused = 0

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")
        index = 1
        for video in self._video_library.get_all_videos():
            separator = " "
            merged_tag = separator.join(video._tags)
            VideoPlayer.video_details[index] = {}
            VideoPlayer.video_details[index]["title"] = video._title
            VideoPlayer.video_details[index]["identity"] = video._video_id
            VideoPlayer.video_details[index]["tags"] = merged_tag
            index = index + 1
        sorted_video_details = sorted(VideoPlayer.video_details.items(),
                                      key = lambda x:x[1]["title"])

        for vid_id, vid_info in sorted_video_details:
            print("  " + vid_info["title"] + " (" + vid_info["identity"] + ") [" + vid_info["tags"] + "]" )


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_exist = 0
        requested_vid_title = "none"
        for video in self._video_library.get_all_videos():
            if video_id == video.video_id:
                video_exist = 1
                requested_vid_title = video._title
            else:
                video_exist = 0
        if video_exist == 0:
            print("Cannot play video: Video does not exist")
        elif video_exist == 1 and VideoPlayer.is_playing == 1:
            print("Stopping video: " + VideoPlayer.current_play)
            print("Playing video: " + requested_vid_title)
            VideoPlayer.current_play = requested_vid_title
        elif video_exist == 1 and VideoPlayer.is_playing == 0:
            VideoPlayer.is_playing = 1
            print("Playing video: " + requested_vid_title)
            VideoPlayer.current_play = requested_vid_title


    def stop_video(self):
        """Stops the current video."""
        if VideoPlayer.is_playing == 1:
            print("Stopping video: " + VideoPlayer.current_play)
            VideoPlayer.is_playing = 0
            VideoPlayer.current_play = "none"
            VideoPlayer.is_paused = 0
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        titles = []
        for video in self._video_library.get_all_videos():
            titles.append(video._title)
        ran_int = random.randint(0, 4)
        if VideoPlayer.is_playing == 1:
            print("Stopping video: " + VideoPlayer.current_play)
        print("Playing video: " + titles[ran_int])
        VideoPlayer.is_playing = 1
        VideoPlayer.current_play = titles[ran_int]

    def pause_video(self):
        """Pauses the current video."""
        if VideoPlayer.is_paused == 1:
            print("Video already paused: " + VideoPlayer.current_play)
        elif VideoPlayer.is_playing == 1:
            print("Pausing video: " + VideoPlayer.current_play)
            VideoPlayer.is_paused = 1
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if VideoPlayer.is_paused == 1:
            print("Continuing video: " + VideoPlayer.current_play)
            VideoPlayer.is_paused = 0
        elif VideoPlayer.is_playing == 1:
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""
        if VideoPlayer.is_playing == 0:
            print("No video is currently playing")
        else:
            if VideoPlayer.is_paused == 1:
                pause_status = " - PAUSE"
            else:
                pause_status = ""
            for video in self._video_library.get_all_videos():
                if VideoPlayer.current_play == video._title:
                    separator = " "
                    merged_tag = separator.join(video._tags)
                    print("Currently playing: " + video._title + " (" + video.video_id
                          + ") [" + merged_tag + "]" + pause_status)
    all_playlist = []
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        is_existed = 0
        for playlist in VideoPlayer.all_playlist:
            if playlist_name.str.lower() == playlist.name.str.lower():
                is_existed = 1
            else:
                is_existed = 0
        if is_existed == 0:
            new_playlist_name = str(playlist_name)
            playlist_name = Playlist(new_playlist_name)
            VideoPlayer.all_playlist.append(playlist_name)
            print("Successfully created new playlist: " + playlist_name.name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

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
