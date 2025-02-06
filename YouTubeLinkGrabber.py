#! /usr/bin/python3
import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def grab_youtube(url: str):
    """
Grabs the live-streaming M3U8 file from YouTube
    :param url: The YouTube URL of the livestream
    """
    print(f'\n#url: {url}')
    if '&' in url:
        url = url.split('&')[0]

    requests.packages.urllib3.disable_warnings()
    stream_info = requests.get(url, timeout=15)
    response = stream_info.text
    soup = BeautifulSoup(stream_info.text, features="html.parser")


    if '.m3u8' not in response or stream_info.status_code != 200:
        print("https://github.com/ExperiencersInternational/tvsetup/raw/main/staticch/no_stream_2.mp4")
        print(f'\n#url: {url}')
        #print("response:")
        #print(response)
        return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner: end]:
            link = response[end - tuner: end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5

            stream_title = soup.find("meta", property="og:title")["content"]
            stream_desc = soup.find("meta", property="og:description")["content"]
            stream_image_url = soup.find("meta", property="og:image")["content"]
            channels.append((channel_name, channel_id, category, stream_title, stream_desc, stream_image_url))

            break
        else:
            tuner += 5
    print(f"{link[start: end]}")

channel_name = ''
channel_id = ''
category = ''

# Open text file and parse stream information and URL
with open('./youtubeLink.txt', encoding='utf-8') as f:
    print("#EXTM3U")
    for line in f:
        line = line.strip()
        if not line or line.startswith('##'):
            continue
        if not (line.startswith('https:') or line.startswith('http:')):
            line = line.split('||')
            channel_name = line[0].strip()
            channel_id = line[1].strip()
            category = line[2].strip().title()
            print(f'\n#EXTINF:-1 tvg-id="{channel_id}" tvg-name="{channel_name}" group-title="{category}", {channel_name}')
        else:
            if urlparse(line).netloc == 'www.youtube.com':
                grab_youtube(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
