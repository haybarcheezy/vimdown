import os
import requests
import vimeo
import json
import time

# Personal access token
token = "PERSONAL_ACCESS_TOKEN"


client = vimeo.VimeoClient(token=token)


def download_video(video):
    video_id = video["uri"].split("/")[-1]
    video_title = video["name"]
    download_links = video.get("download", [])

    if not download_links:
        print(f"No downloadable links for video {video_title} (ID: {video_id})")
        return

    os.makedirs(video_title, exist_ok=True)

    link = sorted(download_links, key=lambda x: x["quality"], reverse=True)[0]["link"]

    response = requests.get(link)
    if response.status_code == 200:
        with open(os.path.join(video_title, video_title + ".mp4"), "wb") as file:
            file.write(response.content)
        print(f"Downloaded video {video_title} (ID: {video_id})")

    with open(os.path.join(video_title, video_title + "_info.txt"), "w") as file:
        json.dump(video, file, indent=4)


def list_and_download_videos(page=1):
    response = client.get("/me/videos", params={"page": page, "per_page": 10})
    if response.status_code == 200:
        data = response.json()

        for video in data["data"]:
            download_video(video)

        if data["paging"]["next"]:
            time.sleep(1)  # rate limit
            list_and_download_videos(page + 1)


list_and_download_videos()
