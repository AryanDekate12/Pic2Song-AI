import streamlit as st
import torch
import clip
from PIL import Image
import numpy as np
import cv2
from fer import FER

from utils.youtube_api import search_youtube_music
from utils.genius_api import get_lyrics


device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

emotion_detector = FER(mtcnn=True)


vibes = [
    "a smiling selfie photo",
    "a mirror selfie",
    "a couple romantic photo",
    "friends group photo",
    "people dancing at a party",
    "gym workout selfie",
    "travel photo with mountains",
    "sunset beach aesthetic photo",
    "night city lights aesthetic",
    "sad emotional portrait",
    "car driving photo",
    "cafe aesthetic photo",
    "festival celebration photo",
    "nature landscape photo",
    "road trip travel photo",
    "college friends photo",
    "wedding celebration photo",
    "romantic date photo",
    "holiday vacation photo"
]


def detect_scene(image):

    image_input = preprocess(image).unsqueeze(0).to(device)

    text = clip.tokenize(vibes).to(device)

    with torch.no_grad():

        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text)

        similarity = (image_features @ text_features.T).softmax(dim=-1)

    values, indices = similarity[0].topk(1)

    return vibes[indices[0]]


def detect_emotion(image_np):

    try:

        img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        result = emotion_detector.detect_emotions(img)

        if result:
            emotions = result[0]["emotions"]
            return max(emotions, key=emotions.get)

        return "neutral"

    except:
        return "neutral"


st.title("🎵 Pic2Song AI")
st.write("Upload a photo and get songs matching your Instagram story vibe")


language = st.selectbox(
    "Select Song Language",
    ["hindi","punjabi","english","any"]
)


uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg","jpeg","png"]
)


if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, use_container_width=True)

    image_np = np.array(image)

    emotion = detect_emotion(image_np)

    scene = detect_scene(image)

    st.subheader("Detected Emotion")
    st.write(emotion)

    st.subheader("Detected Scene")
    st.write(scene)


    emotion_to_music = {
        "happy":"party dance",
        "sad":"sad emotional",
        "neutral":"chill relaxing",
        "angry":"energetic workout",
        "surprise":"trending viral"
    }

    music_mood = emotion_to_music.get(emotion,"chill")


    language_map = {
        "hindi":"bollywood hindi song t-series",
        "punjabi":"punjabi song ap dhillon sidhu moosewala",
        "english":"english pop official music video",
        "any":"official music video"
    }

    language_query = language_map.get(language,"")

    query = f"{language_query} {music_mood}"


    if st.button("🎵 Get Songs"):

        songs = search_youtube_music(query)

        for song in songs:

            st.image(song["thumbnail"], width=300)

            st.write(song["title"])

            st.write(song["url"])

            lyrics = get_lyrics(song["title"])

            st.text(lyrics)

            st.write("---")