#!/bin/bash
python3 -m pip install requests
python3 -m pip install beautifulsoup4

python3 YouTubeLinkGrabber.py > ./youtube.m3u8

echo M3U8 grabbed complete.
