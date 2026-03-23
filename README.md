# 🎵 Pic2Song AI

An AI-powered web app that recommends songs based on images.  
Upload a photo and get music suggestions matching the mood and scene of the image.

## 🚀 Features

- Image emotion detection
- Scene understanding using CLIP
- Song recommendations based on mood
- Supports Hindi, Punjabi, and English songs
- Filters mashups, remixes, and YouTube shorts
- Lyrics preview (when available)

## 🧠 Technologies Used

- Python
- Streamlit
- OpenAI CLIP
- FER (Facial Emotion Recognition)
- YouTube Data API
- Genius API

## 📸 How It Works

1. Upload an image
2. AI detects emotion and scene
3. Generates a music search query
4. Fetches songs from YouTube
5. Displays songs with thumbnails and lyrics

## 📂 Project Structure

```
Pic2Song-AI
│
├── app.py
├── api_keys.py
├── requirements.txt
├── utils
│   ├── youtube_api.py
│   └── genius_api.py
```

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/AryanDekate12/Pic2Song-AI.git
cd Pic2Song-AI
```

Install dependencies

```
pip install -r requirements.txt
```

Run the app

```
streamlit run app.py
```

## 📷 Demo

Upload an image and get song recommendations instantly.

## ⭐ Future Improvements

- Instagram caption generator
- Better song matching with embeddings
- Spotify integration
- Music player inside the app

---

Built with ❤️ using AI
