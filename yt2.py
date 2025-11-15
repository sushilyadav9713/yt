import yt_dlp

def download_with_audio(url):
    ydl_opts = {
        # Choose best video >=480p + best audio (merged)
        "format": "bestvideo[height>=480]+bestaudio/best[height>=480]/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    download_with_audio(video_url)

