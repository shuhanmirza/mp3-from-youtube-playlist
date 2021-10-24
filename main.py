from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
import argparse
import platform
import os

MODULE_INFO = "this script downloads youtube playlists and converts these to mp3 files"


def main():
    args = parse_args()
    playlist = gen_playlist_from_arg(args)

    # prints address of each YouTube object in the playlist
    for vid in playlist.videos:
        print(vid)


def parse_args():
    parser = argparse.ArgumentParser(description=MODULE_INFO)

    parser.add_argument("-ID", "--playlist_id", required=True,
                        help="provide your playlist id")

    return parser.parse_args()


def gen_playlist_from_arg(args):
    playlist_id = args.platlist_id
    playlist = Playlist("https://www.youtube.com/playlist?list=" + playlist_id)

    # prints each video url, which is the same as iterating through playlist.video_urls
    for url in playlist:
        print(url)

    return playlist


if __name__ == "__main__":
    main()
