# <img src="https://github.com/user-attachments/assets/27f0e6f9-b491-4848-89b8-5445fe6d93a2" alt="youtube-logo" width=32 />🎥 YouTube Video Downloader
A simple and efficient command-line tool to download YouTube videos using Python and the `pytubefix` library.

### 🚀 Features
- 📥 Enter the video URL interactively via terminal and download YouTube videos in the highest available resolution.
- 📂 Automatically saves videos to a `downloads/` folder
- 🐋 Docker support for easy setup and deployment.

### 📦 Requirements
- Python 3.12
- PIP package manager
- Optional: Docker and Docker Compose for containerized execution

### 🧰 Packages
| Logo | Package      | Description                              |
|------|--------------|------------------------------------------|
| <p align="center"><img src="https://github.com/user-attachments/assets/007ac71a-66cc-45f7-a5df-13e1718ad252" alt="pytube-logo" /><p /> | `pytubefix` | Enables downloading videos from YouTube. |
| <p align="center"><img src="https://github.com/user-attachments/assets/4125a8bb-7508-44dc-a819-359dd61e3c39" alt="tqdm-logo" width=120/><p />         | `tqdm`      | Provides a customizable progress bar in the terminal. |

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
