from setuptools import setup, find_packages

setup(
    name="GrooveSync",  # Updated project name
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.3.2",
        "youtube_dl>=2021.12.17",
        "flask_cors>=3.0.10",
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'groovesync=app.main:create_app',  # Replace with the appropriate entry point, or remove if not needed
        ],
    },
    author="Will McCurry",
    author_email="wbmccurry20@gmail.com",
    description="A DJ assistant tool for downloading playlists and more.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/groovesync",  # Update with your actual GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)