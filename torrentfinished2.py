#!/usr/bin/python3

import sys
import os
from glob import glob
import requests
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_video

VIDEO_EXTENSIONS = [
    ".avi", ".mp4", ".mkv", ".mpg",
    ".mpeg", ".mov", ".rm", ".vob",
    ".wmv", ".flv", ".3gp",".3g2", ".swf", ".mswmm"
]

def download_subs(file_path):
    region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
    subtitles = download_best_subtitles([file_path], {Language('eng')})
    # save them to disk, next to the video
    save_subtitles(file_path, subtitles[file_path])

def func(torrent):
    if os.path.isfile(torrent):
        if any(torrent.lower().endswith(ext) for ext in VIDEO_EXTENSIONS):
            video = scan_video(torrent)
            download_subs(video)
        return
    for filename in glob(f'{torrent}/**', recursive=True):
        if os.path.isfile(filename) and any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS):
            video = scan_video(filename)
            download_subs(video)
    return

if __name__ == "__main__":
    torrentid = sys.argv[1]
    torrentname = sys.argv[2]
    torrentpath = sys.argv[3]
    func(f"{torrentpath}/{torrentname}")
    data = str({ "username": "Emby", "content": f"{torrentname} finished downloading" }).replace("'", '"')
    apikey = "embyapi"
    os.system(f"/usr/bin/deluge-console 'rm -c {torrentid}; exit'")
    os.system(f"curl  --data '' http://localhost:8096/Emby/Library/Refresh?api_key={apikey}")
    os.system(f"curl -H 'Content-Type: application/json' -d '{data}' 'https://discord.com/api/webhooks/{server}/{webhook}'")
    # os.system(f"zenity --info --no-wrap --display=:0.0 --text='{torrentname} finished downloading';exit")
