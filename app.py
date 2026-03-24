import streamlit as st
import torch
import clip
from PIL import Image
import numpy as np

from utils.youtube_api import search_youtube_music
from utils.genius_api import get_lyrics


device = "cuda" if torch.cuda.is_available() else "cpu"

model, preprocess = clip.load("ViT-B/32", device=device)


vibes = [
    "happy smiling selfie",
    "romantic couple photo",
    "friends party celebration",
    "gym workout selfie",
    "travel mountains photo",
    "sunset beach aesthetic",
    "night city aesthetic",
    "sad emotional portrait",
    "car driving photo",
    "cafe aesthetic photo",
    "festival celebration photo",
    "nature landscape photo",
]


def detect_vibe(image):

    image_input = preprocess(image).unsqueeze(0).to(device)

    text = clip.tokenize(vibes).to(device)

    with torch.no_grad():

        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text)

        similarity = (image_features @ text_features.T).softmax(dim=-1)

    values, indices = similarity[0].topk(1)

    return vibes[indices[0]]


st.title("🎵 Pic2Song AI")

st.write("Upload an image and get songs matching the vibe.")


language = st.selectbox(
    "Select Song Language",
    ["hindi", "punjabi", "english", "any"]
)


uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, use_container_width=True)

    vibe = detect_vibe(image)

    st.subheader("Detected Vibe")

    st.write(vibe)


    language_map = {
        "hindi": "bollywood hindi song",
        "punjabi": "punjabi song",
        "english": "english pop song",
        "any": "official music video"
    }


    language_query = language_map.get(language, "")

    query = f"{language_query} {vibe}"


    if st.button("🎵 Get Songs"):

        songs = search_youtube_music(query)

        for song in songs:

            st.image(song["thumbnail"], width=300)

            st.write(song["title"])

            st.write(song["url"])

            lyrics = get_lyrics(song["title"])

            st.text(lyrics)

            st.write("---")
