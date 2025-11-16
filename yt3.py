import yt_dlp

def download_with_audio(url, number):
    ydl_opts = {
        "format": "bestvideo[height>=480]+bestaudio/best[height>=480]/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
        "playlist_items": str(number),   # <-- download selected video number
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    number = input("Enter video number in playlist: ")

    download_with_audio(playlist_url, number)

