from pytubefix import YouTube
from tqdm import tqdm

# Global tqdm progress bar
progress_bar = None

def progress_function(stream, chunk, bytes_remaining):
    global progress_bar
    total_size = stream.filesize

    if progress_bar is None:
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc='⬇️ Downloading', ncols=80)

    progress_bar.update(len(chunk))

    if bytes_remaining == 0 and progress_bar is not None:
        progress_bar.close()
        print("✅ Download completed successfully")

def download_video(url: str):
    global progress_bar
    try:
        url = url.strip().split('&')[0]
        yt = YouTube(url, on_progress_callback=progress_function)
        print(f"🎬 Video title: {yt.title}")

        stream = (
            yt.streams
            .filter(progressive=True, file_extension='mp4')
            .order_by('resolution')
            .desc()
            .first()
        )

        if not stream:
            print("⚠️ No valid stream found")
            return

        # Reset tqdm progress bar
        progress_bar = None
        stream.download(output_path="downloads")

    except Exception as e:
        if progress_bar:
            progress_bar.close()
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)