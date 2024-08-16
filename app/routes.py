from flask import Flask, render_template, request, jsonify
from scripts.downloader import download_soundcloud

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/download', methods=['POST'])
    def download():
        url = request.form.get('playlist_url')
        download_location = request.form.get('download_location')
        
        if not url or not download_location:
            return jsonify({"success": False, "error": "Please provide both the URL and download directory."})
        
        result = download_soundcloud(url, download_location)
        
        if result["success"]:
            return jsonify({"success": True, "message": "Download completed successfully."})
        else:
            return jsonify({"success": False, "error": result.get("error", "Download failed.")})