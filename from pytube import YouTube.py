import yt_dlp
import os
import sys
import time
import threading

def spinner():
    """Affiche une animation de chargement dans la console."""
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(f'\r{cursor} Downloading...')
            sys.stdout.flush()
            time.sleep(0.1)

def download_youtube_video(url, output_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

        spinner_thread = threading.Thread(target=spinner)
        spinner_thread.daemon = True
        spinner_thread.start()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])

        sys.stdout.write('\rDownload completed successfully!           \n')
        sys.stdout.flush()
    except Exception as e:
        sys.stdout.write('\r')
        sys.stdout.flush()
        print(f"An error occurred during the download: {str(e)}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the directory where you want to save the video: ")

    download_youtube_video(video_url, output_directory)

