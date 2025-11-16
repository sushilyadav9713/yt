import yt_dlp

def download_with_audio(url, number):
    ydl_opts = {
        "format": "bestvideo[height>=480]+bestaudio/best[height>=480]/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
        "playlist_items": str(number),

        # --- FIX FRAGMENT ERRORS ---
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        ),
        "fragment_retries": 20,          # retry missing fragments
        "http_chunk_size": 10485760,     # 10MB chunks (avoids 403 throttling)
        "compat_opts": ["no-keep-fragments"],  # prevents fragment skipping
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    number = input("Enter video number in playlist: ")

    download_with_audio(playlist_url, number)

