# GrooveSync

GrooveSync is a Python-based tool designed to help DJs download playlists and more. This project uses Flask for the web interface and `youtube_dl` for downloading audio tracks from SoundCloud.

## Features

- Download playlists from SoundCloud and other sources.
- Skip tracks that have already been downloaded to avoid duplicates.
- Simple web interface with Bootstrap styling.
- Extensible and ready for future features like Rekordbox integration.

## Prerequisites

Before setting up this project, ensure you have the following installed on your machine:

- Python 3.7 or higher
- Git

For Windows users:
- Install Python from [python.org](https://www.python.org/downloads/).
- Ensure `pip` is included in your Python installation.
- Optionally, install [Git for Windows](https://gitforwindows.org/) for easier command line access to Git.

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine.

git clone https://github.com/yourusername/groovesync.git
cd groovesync

### 2. Create a Virtual Environment

#### For macOS/Linux
python3 -m venv venv
source venv/bin/activate

### For Windows
python -m venv venv
.\venv\Scripts\activate

### 3. Install the Package
pip install .

### 4. Run the application
python main.py



### 5. Access Web Interface
#### Open your web browser and navigate to http://127.0.0.1:5000 to access the GrooveSync interface.

### 6. Using the Application

1. Enter the playlist URL in the "Playlist URL" field.
2. Enter the download location in the "Download Location" field.
3. Click the "Download" button to start downloading the playlist.

### 7. Customizing and Extending GrooveSync

GrooveSync is designed to be extensible. You can add new features or modify existing ones by editing the Python scripts in the `scripts` directory and the HTML/CSS files in the `templates` and `static` directories.

### 8. Contributing

If you'd like to contribute to GrooveSync, feel free to fork the repository, make your changes, and submit a pull request. We welcome all improvements and new features.

### 9. License

This project is licensed under the MIT License. See the `LICENSE` file for details.