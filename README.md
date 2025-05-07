<p align="center">
  <img src="https://github.com/user-attachments/assets/007ac71a-66cc-45f7-a5df-13e1718ad252" alt="pytube-image" />
</p>

# YouTube Video Downloader
A simple and efficient command-line tool to download YouTube videos using Python and the `pytubefix` library.

### 🚀 Features
- 📥 Enter the video URL interactively via terminal and download YouTube videos in the highest available resolution.
- 📂 Automatically saves videos to a `downloads/` folder
- 🐋 Docker support for easy setup and deployment.

### 📦 Requirements
- Python 3.12
- PIP package manager
- Optional: Docker and Docker Compose for containerized execution

## Installation
- Local Python option:

  ```bash
  git clone https://github.com/mashisdev/youtube-video-downloader.git
  cd youtube-video-downloader
  pip install -r requirements.txt
  python main.py
  ```
- Docker option:

  ```bash
  git clone https://github.com/mashisdev/youtube-video-downloader.git
  cd youtube-video-downloader
  docker-compose run youtube-downloader
  ```
