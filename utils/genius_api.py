import lyricsgenius
import re
from difflib import SequenceMatcher
from config import GENIUS_ACCESS_TOKEN

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)", "(Translation)"]


def clean_title(title):

    title = re.sub(r"\(.*?\)", "", title)

    title = title.split("|")[0]

    title = title.split("-")[0]

    return title.strip()


def similarity(a, b):

    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def is_valid_language(text):

    # reject Korean, Japanese, Chinese etc
    non_latin = re.search(r"[^\x00-\x7F]", text)

    if non_latin:
        return False

    return True


def get_lyrics(title):

    try:

        cleaned = clean_title(title)

        song = genius.search_song(cleaned)

        if song is None:
            return "Lyrics unavailable"

        # verify title similarity
        if similarity(cleaned, song.title) < 0.6:
            return "Lyrics unavailable"

        lyrics = song.lyrics

        # remove section labels
        lyrics = re.sub(r"\[.*?\]", "", lyrics)

        # reject non-latin lyrics
        if not is_valid_language(lyrics):
            return "Lyrics unavailable"

        return lyrics[:400]

    except:
        return "Lyrics unavailable"