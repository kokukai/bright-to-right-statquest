import yt_dlp
from youtubesearchpython import VideosSearch

def download_video(title, output_folder=r"./"):
    video_search = VideosSearch(title, limit=1)
    results = video_search.result()
    url = results['result'][0]['link']

    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s'  # Set the output template
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

