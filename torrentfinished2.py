#!/usr/bin/python3

import sys
import os

if __name__ == "__main__":
    torrentid = sys.argv[1]
    torrentname = sys.argv[2]
    torrentpath = sys.argv[3]
    data = str({ "username": "Emby", "content": f"{torrentname} finished downloading" }).replace("'", '"')
    apikey = "embyapi"
    os.system(f"/usr/bin/deluge-console 'rm -c {torrentid}; exit'")
    os.system(f"curl  --data '' http://localhost:8096/Emby/Library/Refresh?api_key={apikey}")
    os.system(f"curl -H 'Content-Type: application/json' -d '{data}' 'https://discord.com/api/webhooks/{server}/{webhook}'")
    os.system(f"zenity --info --no-wrap --display=:0.0 --text='{torrentname} finished downloading';exit")
