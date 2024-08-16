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
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', None)

            if title:
                file_path = os.path.join(download_dir, f"{title}.mp3")
                if os.path.isfile(file_path):
                    logging.info(f"File '{title}.mp3' already exists. Skipping download.")
                    return {"success": True, "message": f"'{title}.mp3' already exists. Skipping."}
                
                # Proceed with the download since the file does not exist
                ydl.download([url])
                logging.info(f"Download completed successfully: {title}.mp3")
                return {"success": True, "message": f"Download completed successfully: {title}.mp3"}
            else:
                logging.error("Could not extract title from the URL.")
                return {"success": False, "error": "Could not extract title from the URL."}

    except Exception as e:
        logging.error(f"Error during download: {e}")
        return {"success": False, "error": str(e)}