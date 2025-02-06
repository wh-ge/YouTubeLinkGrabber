# YouTubeLinkGrabber
The program allows you to convert serval YouTube lives into a M3U file that can play in serval IPTV apps.

With thanks to [@victorlish](https://github.com/victorlish/YouTubeLinkGrabber) for the original project.

## Motivation
Play YouTube live using IPTV app. That's it.

## Usage
1. Put YouTube live link into `YouTubeLink.txt` with the following format
```
Channel Name - Language
https://www.youtube.com/watch?v=idC4ZAleKtc
```
2. Run the cron job in GitHub
3. Put the link `https://raw.githubusercontent.com/<username>/YouTubeLinkGrabber/main/youtube.m3u8` to your IPTV app.

You can also run the program locally by `python YouTubeLinkGrabber.py > youtube.m3u8` or by `chmod +x exec_grabber.sh && ./exec_grabber.sh`.
