from setuptools import setup, find_packages

setup(
    name="dj_assistant",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "yt-dlp",
        "ffmpeg-python",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "dj_assistant=app:main",
        ],
    },
)
