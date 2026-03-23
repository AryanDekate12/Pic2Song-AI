from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY
import random
import isodate

youtube = build("youtube","v3",developerKey=YOUTUBE_API_KEY)


def is_bad_title(title):

    bad_words = [
        "mashup","mix","playlist","jukebox",
        "nonstop","medley","dance hits",
        "remix","dj","lofi","slowed",
        "reverb","status","shorts","edit"
    ]

    title = title.lower()

    return any(word in title for word in bad_words)


def search_youtube_music(query,max_results=5):

    variations = [
        "official video",
        "official song",
        "full song",
        "new song",
        "trending song"
    ]

    query = f"{query} {random.choice(variations)}"

    search = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoCategoryId="10",
        maxResults=40
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search["items"]]

    details = youtube.videos().list(
        part="contentDetails",
        id=",".join(video_ids)
    ).execute()

    durations = {
        item["id"]:item["contentDetails"]["duration"]
        for item in details["items"]
    }

    results = []

    for item in search["items"]:

        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]

        if is_bad_title(title):
            continue

        duration = durations.get(video_id)

        if duration is None:
            continue

        seconds = isodate.parse_duration(duration).total_seconds()

        if seconds < 120:
            continue

        results.append({
            "title":title,
            "url":f"https://youtube.com/watch?v={video_id}",
            "thumbnail":item["snippet"]["thumbnails"]["high"]["url"]
        })

    random.shuffle(results)

    return results[:max_results]