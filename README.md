# DJ Assistant

DJ Assistant is a tool to download and manage playlists from SoundCloud, process them for use with DJ equipment, and ensure high-quality storage on external drives.

## Features

- Download songs as MP3 from SoundCloud playlists
- Ensure high-quality downloads with threading
- Simple front-end for user input
- Automatically upload songs to Rekordbox and external drives
- Clean up local storage after processing

## Requirements

- Python 3.9
- Flask
- yt-dlp
- ffmpeg

## Installation

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd dj_assistant
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    pip install -r requirements.txt
    ```

4. Install ffmpeg (if not already installed):

    ```sh
    brew install ffmpeg
    ```

## Usage

1. Run the application:

    ```sh
    python app.py
    ```

2. Follow the prompts to enter the SoundCloud playlist URL and the download directory.

## Packaging

To create a standalone executable:

1. Ensure the virtual environment is activated.
2. Run `pyinstaller`:

    ```sh
    pyinstaller --onefile --name dj_assistant app.py
    ```

## Running the Executable

1. Locate the executable in the `dist` directory.
2. Run the executable:

    ```sh
    ./dist/dj_assistant
    ```

## License

This project is licensed under the MIT License.
