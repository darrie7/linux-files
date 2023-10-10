#!/usr/bin/python3

import sys
import os

if __name__ == "__main__":
    torrentid = sys.argv[1]
    torrentname = sys.argv[2]
    torrentpath = sys.argv[3]
    os.system(f"zenity --info --no-wrap --display=:0.0 --text='Started downloading {torrentname}, please wait a few minutes and go to Netflax';exit")
