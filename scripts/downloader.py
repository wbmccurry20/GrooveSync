import os
import youtube_dl
import logging

def download_soundcloud(url, download_dir='downloads'):
    try:
        # Ensure the download directory exists
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Save directly to the target directory
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            logging.info(f"Downloading URL: {url}")
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            if title:
                file_path = os.path.join(download_dir, f"{title}.mp3")
                if os.path.isfile(file_path):
                    logging.info(f"Download successful: {file_path}")
                    return {"success": True, "message": f"Download completed successfully: {title}.mp3"}
                else:
                    logging.error("File not found after download.")
                    return {"success": False, "error": "File not found after download."}
            else:
                logging.error("Could not extract title from the URL.")
                return {"success": False, "error": "Could not extract title from the URL."}

    except Exception as e:
        logging.error(f"Error during download: {e}")
        return {"success": False, "error": str(e)}
