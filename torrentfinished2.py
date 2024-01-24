#!/usr/bin/python3

import sys
import os
from glob import glob
import requests
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_video
from time import sleep
from asyncio import run, to_thread, sleep, gather
from random import randint

VIDEO_EXTENSIONS = [
    ".avi", ".mp4", ".mkv", ".mpg",
    ".mpeg", ".mov", ".rm", ".vob",
    ".wmv", ".flv", ".3gp",".3g2", ".swf", ".mswmm"
]

async def download_subs(file_path):
    await sleep(randint(2, 45))
    region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'}, replace_existing_backend=True)
    video = scan_video(file_path)
    subtitles = await to_thread(download_best_subtitles, [video], {Language('eng')})
    # save them to disk, next to the video
    save_subtitles(video, subtitles[video])
    return

async def funcsion(torrent):
    if os.path.isfile(torrent):
        if any(torrent.lower().endswith(ext) for ext in VIDEO_EXTENSIONS):
            await download_subs(torrent)
        return
    await gather(*[download_subs(file) for file in glob(fr'{torrent}/**/*', recursive=True) if (os.path.isfile(file) and any(file.lower().endswith(ext) for ext in VIDEO_EXTENSIONS))])
    return

if __name__ == "__main__":
    torrentid = sys.argv[1]
    torrentname = sys.argv[2]
    torrentpath = sys.argv[3]
    run(funcsion(f"{torrentpath}/{torrentname}"))
    # os.system(f"zenity --info --no-wrap --display=:0.0 --text='{torrentname} finished downloading';exit")
    data = str({ "username": "Emby", "content": f"{torrentname} finished downloading" }).replace("'", '"')
    apikey = "embyapi"
    os.system(f"/usr/bin/deluge-console 'rm -c {torrentid}; exit'")
    os.system(f"curl  --data '' http://localhost:8096/Emby/Library/Refresh?api_key={apikey}")
    os.system(f"curl -H 'Content-Type: application/json' -d '{data}' 'https://discord.com/api/webhooks/server/channel'")
