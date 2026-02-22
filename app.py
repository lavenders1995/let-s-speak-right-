import streamlit as st
from streamlit_mic_recorder import mic_recorder
import random

# 1. Sayfa Ayarları
st.set_page_config(page_title="Let's Speak Right!", page_icon="📖")

# 2. Şık Tasarım Ayarları
st.markdown("""
    <style>
    .stApp { background-color: #fdfaf0; }
    .word-box {
        background-color: white;
        padding: 40px;
        border-radius: 25px;
        border: 4px solid #ffcc00;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .word-text {
        font-size: 70px !important;
        color: #2c3e50;
        font-weight: bold;
        margin: 0;
    }
    /* Butonları özelleştirme */
    .stButton>button {
        border-radius: 15px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Kelime Havuzu
words = [
    "the", "think", "thought", "about", "are", "refuse", "use", "she", "chat", 
    "accept", "language", "country", "umbrella", "quick", "who", "what", 
    "where", "three", "speak", "sign", "join", "jump", "location", "bathroom", 
    "today", "wednesday", "thursday", "watch", "rarely", "usually", "generally"
]

# 4. Hafıza Sistemi (Kelimelerin ve Yıldızların Kaybolmaması İçin)
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(words)
if 'stars' not in st.session_state:
    st.session_state.stars = 0

# 5. Başlık ve Kelime Kartı
st.title("Let's Speak Right! ✍️📖")

st.markdown(f'<div class="word-box"><p class="word-text">{st.session_state.current_word}</p></div>', unsafe_allow_html=True)
st.write(f"### ⭐ Başarı Yıldızlarım: {st.session_state.stars}")

st.divider()

# 6. Oynat / Durdur ve Kayıt Bölümü
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Doğrusunu Dinle")
    
    # Ses Dosyası Linki
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={st.session_state.current_word}&tl=en&client=tw-ob"
    
    # iPhone ve Android'de %100 çalışan Oynat/Durdur Butonları (HTML/JS)
    play_html = f"""
    <div style="display: flex; gap: 10px; margin-top: 10px;">
        <button onclick="document.getElementById('audio-player').play()" 
            style="flex:1; padding: 15px; background-color: #4CAF50; color: white; border: none; border-radius: 12px; font-weight: bold; cursor: pointer;">
            ▶️ OYNAT
        </button>
        <button onclick="document.getElementById('audio-player').pause(); document.getElementById('audio-player').currentTime = 0;" 
            style="flex:1; padding: 15px; background-color: #f44336; color: white; border: none; border-radius: 12px; font-weight: bold; cursor: pointer;">
            ⏹️ DURDUR
        </button>
    </div>
    <audio id="audio-player" src="{tts_url}"></audio>
    """
    st.components.v1.html(play_html, height=100)
    st.caption("İstediğin kadar tekrar tekrar dinleyebilirsin.")

with col2:
    st.subheader("2. Senin Sesin")
    # Mikrofon Kaydedici
    audio = mic_recorder(
        start_prompt="🎤 Kayda Başla",
        stop_prompt="🛑 Durdur",
        key='recorder'
    )
    if audio:
        st.audio(audio['bytes'])

st.divider()

# 7. Ana Kontroller
if st.button("✨ BU KELİMEYİ BAŞARDIM!", use_container_width=True, type="primary"):
    st.session_state.stars += 1
    st.balloons()
    st.session_state.current_word = random.choice(words)
    st.rerun()

if st.button("🎲 Başka Kelime Getir", use_container_width=True):
    st.session_state.current_word = random.choice(words)
    st.rerun()
