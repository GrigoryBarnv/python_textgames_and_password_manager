from pathlib import Path
from urllib.parse import parse_qs, urlparse

try:
    import yt_dlp
except ImportError:
    yt_dlp = None


def normalize_youtube_url(url):
    parsed = urlparse(url.strip())

    if "youtu.be" in parsed.netloc:
        video_id = parsed.path.lstrip("/")
        return f"https://www.youtube.com/watch?v={video_id}"

    if "/shorts/" in parsed.path:
        video_id = parsed.path.split("/shorts/")[-1].split("/")[0]
        return f"https://www.youtube.com/watch?v={video_id}"

    if "watch" in parsed.path:
        query = parse_qs(parsed.query)
        video_id = query.get("v", [""])[0]
        if video_id:
            return f"https://www.youtube.com/watch?v={video_id}"

    return url.strip()

def download_video(url, save_path):
    if yt_dlp is None:
        print("yt-dlp is not installed in this Python environment.")
        print("Install it with:")
        print(r"C:\Users\grigo\AppData\Local\Programs\Python\Python312\python.exe -m pip install -U yt-dlp")
        return

    try:
        normalized_url = normalize_youtube_url(url)
        output_template = str(Path(save_path) / "%(title)s.%(ext)s")
        ydl_opts = {
            "format": "best[ext=mp4]/best",
            "outtmpl": output_template,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([normalized_url])

        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Download failed: {e}")


url = "https://www.youtube.com/watch?v=Sus8_2S4azg"
save_path = r"C:\Users\grigo\projekt_ordner\python_1_quiz_game_password_manager\youtube_download"

download_video(url, save_path)
