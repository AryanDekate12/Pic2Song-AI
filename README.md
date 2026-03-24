# 🎵 Pic2Song AI

Pic2Song AI is an AI-powered web application that recommends songs based on the vibe of an uploaded image.  
The system analyzes the image using AI and suggests songs that match the mood and scene — perfect for Instagram stories or social media posts.

---

## 🚀 Live Demo

Try the application here:

https://pic2song-ai.streamlit.app/

---

## 🎥 Demo Video

Watch the project demo here:


https://github.com/user-attachments/assets/6c32f7cb-5254-4eb0-838f-ca128a50cc3d


---

## 🧠 How It Works

1. User uploads an image  
2. AI analyzes the image using CLIP  
3. The detected vibe is used to generate a music search query  
4. Songs are fetched from YouTube  
5. The app displays:
   - Recommended songs
   - Video links
   - Lyrics preview (if available)

---

## ✨ Features

- Image-based music recommendation
- AI scene understanding using CLIP
- Multi-language song suggestions
  - Hindi
  - Punjabi
  - English
- Filters mashups, remixes, and YouTube shorts
- Lyrics preview (when available)
- Deployed using Streamlit Cloud

---

## 🛠 Tech Stack

- Python
- Streamlit
- OpenAI CLIP
- PyTorch
- YouTube Data API
- Genius API

---

## 📂 Project Structure

```
Pic2Song-AI
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
└── utils
    ├── youtube_api.py
    └── genius_api.py
```

---

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

---

## 🔑 API Setup

Create a `.env` file or use Streamlit secrets.

Example:

```
YOUTUBE_API_KEY=your_youtube_api_key
GENIUS_ACCESS_TOKEN=your_genius_token
```

---

## 📈 Future Improvements

- Instagram caption generator
- Spotify integration
- Better song recommendation using embeddings
- Built-in music player

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Aryan Dekate**

GitHub  
https://github.com/AryanDekate12

LinkedIn  
https://www.linkedin.com/in/aryan-dekate-1b1129288/
