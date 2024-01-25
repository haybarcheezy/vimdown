# Vimeo Video Downloader

## Description

This Python script uses the PyVimeo library to download all videos from a Vimeo user's account. For each video, the script creates a directory named after the video's title, saves the video in MP4 format within this directory, and creates a text file containing the video's metadata.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- PyVimeo library installed. You can install it using `pip install PyVimeo`.
- A personal access token from Vimeo. See Vimeo's API documentation for how to obtain this token.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine or download the script directly.

git clone https://github.com/haybarcheezy/vimdown.git

2. **Navigate to the Script Directory**: Change directory to where the script is located.

cd path/to/script

3. **Install Dependencies**: Ensure all required packages are installed.

pip install -r requirements.txt

## Usage

To run the script, execute the following command in the terminal:

python videodownloader.py

Make sure to replace the placeholder token in the script with your actual Vimeo personal access token.

## How It Works

- The script authenticates with the Vimeo API using your personal access token.
- It then fetches all videos associated with the authenticated user's account.
- For each video, it creates a directory named after the video's title.
- The video is downloaded and saved into this directory along with a text file containing the video's metadata.

## Important Notes

- Ensure you have the necessary rights and permissions to download videos from the specified Vimeo account.
- This script is intended for personal use and should be used in accordance with Vimeo's terms of service and copyright laws.
- Downloading large numbers of videos or very large videos may take a significant amount of time.

## Acknowledgments

- This script was created using the PyVimeo library, a Python wrapper for the Vimeo API.
