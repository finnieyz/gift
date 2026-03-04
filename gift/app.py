import streamlit as st
from datetime import date
from PIL import Image

# 1. KONFIGURASI ESTETIKA
st.set_page_config(page_title="Pour Ma Sœur", page_icon="🦢", layout="centered")
st.markdown("""
    <style>
    .main {background-color: #fdfbf7;}
    h1, h2, h3 {color: #d4af37; font-family: 'Georgia', serif; text-align: center;}
    p {color: #5c5c5c; font-family: 'Georgia', serif; text-align: center; font-size: 16px;}
    .stAudio {margin: 0 auto; display: block; width: 50%;}
    </style>
    """, unsafe_allow_html=True)

# 2. NAVIGASI (Sidebar)
menu = st.sidebar.radio("Explore the Sanctuary", ["The Countdown", "The Poetry Art", "The Memory Gallery", "The Secret Vault"])

# 3. HALAMAN 1: THE COUNTDOWN
if menu == "The Countdown":
    st.title("A Beautiful Chapter Awaits 🕊️")
    st.write("For my dearest sister, a little countdown to our beautiful miracle.")
    
    # Asumsi perkiraan lahir (Silakan ubah tanggalnya)
    due_date = date(2026, 10, 13) 
    today = date.today()
    days_left = (due_date - today).days

    if days_left > 0:
        st.markdown(f"<h1>{days_left} Days</h1>", unsafe_allow_html=True)
        st.write("until we meet the little angel.")
    else:
        st.title("The beautiful miracle is here! 🤍")

# 4. HALAMAN 2: THE POETRY ART
elif menu == "The Poetry Art":
    st.title("Words of Love 🌸")
    st.write("Every word here is a prayer and a piece of my heart for you.")
    # Menampilkan gambar yang sudah di-generate di Tahap 1
    try:
        image = Image.open('gift/poetry_art.png')
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.write("Artwork is being curated...")
    st.write("""⋆ ˚｡⋆୨୧˚ 🎀 ˚୨୧⋆｡˚ ⋆
             
sisterhood unconditional irreplaceable deeply-rooted unbreakable forever mine
blooming life miracle tiny-heartbeat sacred creation divine
soft gentle pure peaceful radiant glowing mother-to-be
soulmate confidante my-first-friend my-forever-home
blooming life miracle pure peaceful unconditional sisterhood
L'amour éternel (cinta abadi) Ma douce (manisku) La vie (kehidupan)

destiny serendipity timeless cherished adored treasured
devotion grace elegance warmth tender embrace
starlight morning-sun quiet-whispers safe-haven
enduring unbreakable woven-together written-in-the-stars
miracle destiny serendipity timeless grace miracle destiny

healthy-baby peaceful-mind strong-body absolute-radiance
perfectly-unfolding divine-timing surrounded-by-love
effortless-grace natural-beauty deep-tranquility
safe protected cherished celebrated loved
healthy-baby peaceful-mind perfectly-unfolding safe loved
⋆ ˚｡⋆୨୧˚ 🌸 ˚୨୧⋆｡˚ ⋆""")

# 4.5. HALAMAN BARU: THE MEMORY GALLERY
elif menu == "The Memory Gallery":
    st.title("A Walk Down Memory Lane 🎞️")
    st.write("*A curated collection of our unconditional sisterhood.*")
    
    st.write("---")

    try:
        audio_file = open('gift/gooddays.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mpeg', autoplay=True)
    except FileNotFoundError:
        st.write("(Music will be added soon)")
    
    # Menata foto dalam dua kolom yang elegan
    col1, col2, col3 = st.columns(3) 
    
    with col1:

        try:
            # Pastikan nama file sesuai dengan foto yang Anda siapkan
            st.image("gift/f1.jpg", caption="My first friend", use_container_width=True)
            st.write("") # Memberikan sedikit ruang bernapas
            st.image("gift/f3.jpg", caption="Timeless grace", use_container_width=True)
            st.write("") # Memberikan sedikit ruang bernapas
            st.image("gift/f8.jpg", caption="", use_container_width=True)
        except FileNotFoundError:
            st.info("Curating visual memories... (Menyusun kenangan visual...)")
            
    with col2:
        try:
            st.image("gift/f2.jpg", caption="My forever home", use_container_width=True)
            st.write("")
            st.image("gift/f4.jpg", caption="Unbreakable bond", use_container_width=True)
            st.write("")
            st.image("gift/f9.jpg", caption="", use_container_width=True)
        except FileNotFoundError:
            st.empty()

    with col3:
        try:
            st.image("gift/f5.jpg", caption="", use_container_width=True)
            st.write("")
            st.image("gift/f6.jpg", caption="", use_container_width=True)
            st.write("")
            st.image("gift/f10.jpg", caption="", use_container_width=True)
        except FileNotFoundError:
            st.empty()

# 5. HALAMAN 3: THE SECRET VAULT
elif menu == "The Secret Vault":
    st.title("The Digital Vault 💌")
    password = st.text_input("Enter the secret date (DDMMYYYY) to unlock:", type="password")
    
    # Ganti dengan tanggal spesial kalian atau tanggal lahirnya
    if password == "04032000": 
        st.success("Vault Unlocked. Welcome, my exquisite sister.")
        st.write("---")
        # Pemutar Musik
        st.write("Listen to this while you read 🎧")
        try:
            audio_file = open('gift/anyone.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mpeg', autoplay=True)
        except FileNotFoundError:
            st.write("(Music will be added soon)")
            
        st.write("---")
        st.write("""⋆ ˚｡⋆୨୧˚ 🎀 ˚୨୧⋆｡˚ ⋆

To my dearest sister, my one and only... 💌🦢

Happy birthday to the most beautiful soul, the woman who holds half of my heart 🌸.

Ever since you stepped into your beautiful new chapter of marriage and built a warm home with your husband, I must confess that there is a quiet, lingering space in my heart that misses you endlessly 🥺🎀. I find myself constantly yearning for your comforting presence, your gentle laughter, and our seemingly endless, beautiful conversations. Even though our daily lives are now painted in different places, please know that my love and my sincere prayers are always holding you close, no matter the distance 🩰🩷.

And now, knowing that a precious, sacred little life is softly blooming within you... oh, it is a true miracle 👼🏼🌸. My heart is simply overflowing with an indescribable, pure joy. Watching you step into this radiant era of motherhood fills me with so much pride. May this beautiful chapter of creation be enveloped in divine tranquility, and may you and your little angel be blessed with absolute health, peace, and grace 🌷🕊️.

Though I miss you more than words could ever say, seeing you so deeply loved, cherished, and glowing with happiness brings me the greatest peace 💒. With all my heart, I already know you are going to be the most elegant, gentle, and extraordinary mother ✨.

Enjoy your beautifully curated day, my exquisite sister 🎂🎀. Please remember that Fiti will always be right here for you—whenever you need a shoulder to lean on, a safe space to share your stories, or just a moment to gracefully reminisce.

I love you with all my heart, forever and always 💗✨.

⋆ ˚｡⋆୨୧˚ 🌸 ˚୨୧⋆｡˚ ⋆""")
            
        st.write("---")
            
    elif password:
        st.error("Incorrect password. Try again, love.")

        
