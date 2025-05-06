from pytubefix import YouTube

def download_video(url: str):
    try:
        # Clean the URL
        url = url.strip().split('&')[0]

        # Create YouTube object
        yt = YouTube(url)
        print(f"🎬 Video title: {yt.title}")

        # Select the best progressive stream in mp4
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

        # Download the video
        stream.download(output_path="downloads")
        print("✅ Download completed successfully")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)