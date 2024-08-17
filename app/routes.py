from flask import Flask, render_template, request, jsonify
from scripts.downloader import download_soundcloud
import os

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/download', methods=['POST'])
    def download():
        url = request.form.get('playlist_url')
        playlist_name = request.form.get('playlist_name')
        
        if not url or not playlist_name:
            return jsonify({"success": False, "error": "Please provide both the URL and playlist name."})
        
        # Define the GrooveSync directory on the desktop
        groove_sync_dir = os.path.expanduser("~/Desktop/GrooveSync")
        
        # Ensure the GrooveSync directory exists
        os.makedirs(groove_sync_dir, exist_ok=True)
        
        # Create the full path by adding the playlist name as a subdirectory
        download_location = os.path.join(groove_sync_dir, playlist_name)
        
        # Ensure the playlist directory exists
        os.makedirs(download_location, exist_ok=True)
        
        # Call the download function
        result = download_soundcloud(url, download_location)
        
        if result["success"]:
            return jsonify({"success": True, "message": "Download completed successfully."})
        else:
            return jsonify({"success": False, "error": result.get("error", "Download failed.")})
