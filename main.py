from pytubefix import YouTube

def download_video(url: str):
    try:
        # Limpiar la URL
        url = url.strip().split('&')[0]

        # Crear objeto YouTube
        yt = YouTube(url)
        print(f"🎬 Título del video: {yt.title}")

        # Seleccionar el mejor stream progresivo en mp4
        stream = (
            yt.streams
            .filter(progressive=True, file_extension='mp4')
            .order_by('resolution')
            .desc()
            .first()
        )

        if not stream:
            print("⚠️ No se encontró un stream válido")
            return

        # Descargar el video
        stream.download()
        print("✅ Descarga completada con éxito")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    download_video(url)