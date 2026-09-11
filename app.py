import streamlit as st
import base64
import os
import random

# Set page configuration
st.set_page_config(
    page_title="Selamat Ulang Tahun Ke-22, Nur Hidayah! 🌸",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.html(f"<style>{f.read()}</style>")

load_css()

# Convert image to base64
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            return f"data:image/png;base64,{base64.b64encode(data).decode()}"
    return None

sasuke_sakura_b64 = get_image_base64(os.path.join("assets", "sasuke_sakura.png"))

# Initialize Session State
if "poked" not in st.session_state:
    st.session_state.poked = False

if "candle_blown" not in st.session_state:
    st.session_state.candle_blown = False

if "wishes" not in st.session_state:
    st.session_state.wishes = [
        {
            "sender": "Hasim",
            "wish": "Barakallah Fii Umrik Nur Hidayah! Semoga sehat selalu, makin sukses, dan tercapai semua impianmu! Semoga hari-harimu selalu secerah senyummu. Tetap jadi pribadi yang baik dan menginspirasi! 🌸✨",
            "time": "Hari ini"
        }
    ]

# Sakura Petals Animation (Pure CSS)
def render_sakura_petals(count=30):
    petals_html = '<div class="sakura-container">'
    for _ in range(count):
        left = random.randint(1, 98)
        size = random.randint(10, 20)
        duration = round(random.uniform(5.5, 12.0), 2)
        delay = round(random.uniform(0.0, 7.0), 2)
        petals_html += f'<div class="petal" style="left: {left}%; width: {size}px; height: {size*1.3}px; animation-duration: {duration}s; animation-delay: {delay}s;"></div>'
    petals_html += '</div>'
    st.html(petals_html)

render_sakura_petals(30)

# Sidebar Controls & Audio
with st.sidebar:
    st.markdown("### 🌸 Kotak Pengaturan & Musik")
    st.write("Atur suasana perayaan ulang tahun Nur Hidayah:")

    # Background Music Settings
    enable_music = st.checkbox("Putar Musik Latar (BGM) 🎵", value=True)
    if enable_music:
        music_source = st.radio(
            "Pilihan Sumber Musik:",
            ["Default: Sal Priadi - Serta Mulia 🌸", "Upload File MP3 Sendiri", "Gunakan Link/URL Musik"],
            index=0
        )
        
        audio_bytes = None
        audio_mime = "audio/mp3"
        audio_caption = ""

        # Check local audio files in assets
        local_candidates = [
            os.path.join(os.path.dirname(__file__), "assets", "Serta Mulia-Sal Priadi Lyrics.mp3"),
            os.path.join(os.path.dirname(__file__), "assets", "bgm.mp3")
        ]
        local_bgm_path = next((p for p in local_candidates if os.path.exists(p)), None)

        if music_source == "Upload File MP3 Sendiri":
            uploaded_audio = st.file_uploader("Pilih file lagu (.mp3 / .wav):", type=["mp3", "wav", "ogg"], key="audio_uploader")
            if uploaded_audio is not None:
                audio_bytes = uploaded_audio.read()
                audio_mime = uploaded_audio.type
                audio_caption = f"🎶 Sedang memutar: {uploaded_audio.name}"
            else:
                st.info("💡 Silakan upload lagu kesukaan Nur Hidayah.")
        elif music_source == "Gunakan Link/URL Musik":
            custom_url = st.text_input(
                "Masukkan URL file audio (.mp3):",
                placeholder="https://contoh.com/lagu-romantis.mp3"
            )
            if custom_url.strip():
                st.html(
                    f"""
                    <audio controls loop autoplay style="width: 100%; margin-top: 8px; border-radius: 12px;">
                        <source src="{custom_url.strip()}" type="audio/mp3">
                    </audio>
                    """
                )
                audio_caption = "🎶 Memutar dari URL kustom"
        else: # Default (Sal Priadi - Serta Mulia)
            if local_bgm_path and os.path.exists(local_bgm_path):
                with open(local_bgm_path, "rb") as f:
                    audio_bytes = f.read()
                audio_caption = "🎶 *BGM: Sal Priadi — Serta Mulia 🌸*"
            else:
                default_bgm_url = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=romantic-piano-112199.mp3"
                st.html(
                    f"""
                    <audio controls loop autoplay style="width: 100%; margin-top: 8px; border-radius: 12px;">
                        <source src="{default_bgm_url}" type="audio/mp3">
                    </audio>
                    """
                )
                audio_caption = "🎶 *BGM: Sal Priadi — Serta Mulia 🌸*"

        if audio_bytes is not None:
            st.audio(audio_bytes, format=audio_mime, loop=True, autoplay=True)
            if audio_caption:
                st.caption(audio_caption)
        elif audio_caption and music_source != "Gunakan Link/URL Musik":
            st.caption(audio_caption)
    
    st.markdown("---")
    st.markdown("### 💡 Tentang Tema Website")
    st.info(
        "Website ini terinspirasi dari momen paling ikonik dan romantis antara **Sasuke & Sakura** (*The Forehead Poke*). "
        "Di balik sifat dinginnya, sentuhan dua jari di dahi adalah bahasa cinta Sasuke yang paling tulus — tanda perlindungan, "
        "janji untuk kembali, dan rasa terima kasih yang tak terhingga."
    )
    st.markdown("---")
    if st.button("🔄 Reset Interaksi (Tiup Lilin & Poke)"):
        st.session_state.poked = False
        st.session_state.candle_blown = False
        st.rerun()

# ----------------- MAIN CONTENT -----------------

# Header section
st.html(
    """
    <div class="japanese-quote">「また今度な... ありがとう」</div>
    <div class="birthday-title">HAPPY 22ND BIRTHDAY<br>NUR HIDAYAH 🌸</div>
    <p style="text-align: center; color: #ffd1dc; font-size: 1.15rem; margin-top: 0.5rem; font-style: italic;">
        “Seperti mekarnya bunga sakura di musim semi, kehadiranmu selalu membawa keindahan dan ketenangan.”
    </p>
    """
)

# Hero Image Card
if sasuke_sakura_b64:
    st.html(
        f"""
        <div class="hero-card">
            <img src="{sasuke_sakura_b64}" class="hero-img" alt="Sasuke Sakura Forehead Poke">
            <div class="hero-badge">🌸 Sasuke & Sakura — The Promise of Love</div>
        </div>
        """
    )

# ----------------- INTERACTION 1: THE FOREHEAD POKE -----------------
with st.container(border=True):
    st.html('<div class="card-title">👆 Sentuhan Paling Ikonik: The Forehead Poke</div>')
    st.write(
        "Dalam cerita Naruto, Sasuke tidak banyak berkata-kata. Namun saat ia menyentuhkan dua jarinya ke dahi Sakura, "
        "itu adalah ungkapan cinta dan rasa syukur terdalam yang melampaui ribuan kata. "
        "Coba klik tombol di bawah untuk merasakan momen spesial ini:"
    )

    col_poke1, col_poke2, col_poke3 = st.columns([1, 2, 1])
    with col_poke2:
        if st.button("👉 Sentuh Dahi (Forehead Poke) 🌸", key="poke_btn"):
            st.session_state.poked = True
            st.balloons()

    if st.session_state.poked:
        st.html(
            """
            <div class="poke-result">
                <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">👆✨🌸</div>
                <div style="font-family: 'Noto Serif JP', serif; font-size: 1.35rem; color: #ffb6c1; letter-spacing: 2px;">
                    「また今度な... ありがとう」
                </div>
                <div style="font-size: 1.08rem; color: #ffe4e1; font-weight: 500; margin-top: 0.9rem; line-height: 1.75;">
                    <i>*Sasuke perlahan mendekat, menatap dengan tatapan teduh, lalu menyentuhkan dua jarinya ke dahimu dengan lembut...*</i><br><br>
                    <b>"Sampai nanti... dan terima kasih banyak sudah hadir di dunia ini, Nur Hidayah."</b>
                </div>
                <div style="margin-top: 1rem; font-size: 0.98rem; color: #ffd1dc; opacity: 0.95; line-height: 1.65;">
                    Sebagaimana Sakura yang selalu setia menyinari perjalanan hidup Sasuke, 
                    semoga kamu selalu tahu bahwa keberadaanmu sangat berharga dan berarti bagi orang-orang yang menyayangimu.
                </div>
            </div>
            """
        )

# ----------------- INTERACTION 2: MAKE A WISH & TIUP LILIN -----------------
with st.container(border=True):
    st.html('<div class="card-title">🎂 Kue Ulang Tahun & Make a Wish</div>')
    st.write("Pejamkan mata, panjatkan doa terbaik dalam hati, lalu tiup lilin ulang tahun ke-22 kamu!")

    # Candle flame styling & status
    flame_style = "display: none;" if st.session_state.candle_blown else "display: block;"
    flame_class = "" if st.session_state.candle_blown else "candle-flame"
    smoke_style = "display: block;" if st.session_state.candle_blown else "display: none;"
    cake_status_text = "🎉 Lilin telah ditiup! Harapan indahmu melesat ke angkasa..." if st.session_state.candle_blown else "🕯️ Lilin ke-22 menyala hangat dengan untaian doa dan harapan..."

    cake_html = f"""
    <div class="cake-container">
        <svg width="220" height="210" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="margin: 0 auto; display: block;">
            <!-- Plate -->
            <ellipse cx="100" cy="180" rx="90" ry="14" fill="#3a2f55" stroke="#ffb7c5" stroke-width="2"/>
            
            <!-- Bottom Cake Layer -->
            <path d="M 25 140 A 15 8 0 0 0 175 140 L 175 170 A 15 8 0 0 1 25 170 Z" fill="#2d1b40"/>
            <ellipse cx="100" cy="140" rx="75" ry="15" fill="#4a2c68"/>
            <path d="M 25 140 Q 40 155 55 140 Q 70 155 85 140 Q 100 155 115 140 Q 130 155 145 140 Q 160 155 175 140" fill="none" stroke="#ff80bf" stroke-width="4" stroke-linecap="round"/>

            <!-- Middle/Top Cake Layer -->
            <path d="M 45 95 A 15 8 0 0 0 155 95 L 155 130 A 15 8 0 0 1 45 130 Z" fill="#ff758c"/>
            <ellipse cx="100" cy="95" rx="55" ry="12" fill="#ff9ebb"/>
            
            <!-- Cherry & Sakura Blossom decorations -->
            <circle cx="70" cy="95" r="5" fill="#ff4081"/>
            <circle cx="100" cy="98" r="5" fill="#ff4081"/>
            <circle cx="130" cy="95" r="5" fill="#ff4081"/>
            
            <!-- Candle Stick -->
            <rect x="96" y="55" width="8" height="40" rx="4" fill="#ffffff" stroke="#ff80bf" stroke-width="1.5"/>
            <line x1="100" y1="55" x2="100" y2="46" stroke="#444" stroke-width="2"/>

            <!-- Flame -->
            <g class="{flame_class}" style="{flame_style}">
                <ellipse cx="100" cy="38" rx="7" ry="12" fill="#ffa726" opacity="0.95"/>
                <ellipse cx="100" cy="40" rx="4" ry="7" fill="#fff59d"/>
            </g>
            
            <!-- Smoke when blown -->
            <g style="{smoke_style}">
                <path d="M 100 45 Q 92 35 104 25 Q 112 15 100 5" fill="none" stroke="#dcdde1" stroke-width="2.5" stroke-dasharray="3,3" opacity="0.85"/>
                <text x="100" y="28" font-size="14" fill="#ffeb3b" text-anchor="middle">✨</text>
            </g>
        </svg>
        <div style="margin-top: 15px; font-weight: 500; font-size: 1.05rem; color: #ffd1dc;">
            {cake_status_text}
        </div>
    </div>
    """
    st.html(cake_html)

    col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
    with col_c2:
        if not st.session_state.candle_blown:
            if st.button("✨ Tiup Lilin & Make a Wish! 🕯️", key="blow_btn"):
                st.session_state.candle_blown = True
                st.balloons()
                st.rerun()
        else:
            st.success("🤲 Aamiin! Doa dan harapan terindahmu sedang diantarkan ke langit.")
            if st.button("🔄 Nyalakan Lilin Kembali", key="relight_btn"):
                st.session_state.candle_blown = False
                st.rerun()

# ----------------- SPECIAL BIRTHDAY LETTER -----------------
with st.container(border=True):
    st.html('<div class="card-title">💌 Sepucuk Surat untuk Nur Hidayah</div>')
    
    letter_html = """
    <div class="letter-box">
        <p><b>Dear Nur Hidayah,</b></p>
        
        <p>
        Selamat bertambah usia yang ke-22. Di hari yang istimewa ini, semoga setiap kebaikan yang pernah kau tebarkan 
        kembali kepadamu dalam bentuk kebahagiaan yang berlipat ganda.
        </p>
        
        <p>
        Sesuai dengan namamu yang begitu indah — <b>Nur Hidayah</b> (<i>Cahaya Petunjuk</i>) — kehadiranmu 
        di dunia ini selalu membawa kehangatan, ketenangan, dan keceriaan bagi siapa pun yang mengenalmu. 
        Terkadang dunia terasa begitu cepat dan melelahkan, namun caramu tersenyum dan bertahan selalu mampu 
        mengingatkan akan indahnya harapan.
        </p>
        
        <p>
        Teruslah mekar dengan anggun, jangan pernah ragu akan potensimu, dan ingatlah bahwa kamu sangat disayangi 
        dan berharga apa adanya.
        </p>
        
        <div class="letter-sign">
            Dengan segenap doa terbaik & kasih sayang,<br>
            <span style="font-size: 1.15rem; color: #ff69b4; font-weight: 700;">🌸 Happy 22nd Birthday! 🌸</span>
        </div>
    </div>
    """
    st.html(letter_html)

# ----------------- 5 HAL ISTIMEWA TENTANG NUR HIDAYAH -----------------
with st.container(border=True):
    st.html('<div class="card-title">✨ 5 Hal Istimewa Tentang Nur Hidayah</div>')
    st.write("Inilah alasan mengapa dunia terasa lebih manis dan berarti dengan kehadiranmu:")

    reasons = [
        ("🌸 Senyuman Manis & Menenangkan", "Senyummu punya daya magis tersendiri. Di saat suasana sedang rumit atau melelahkan, senyumanmu selalu mampu membawa kelegaan seketika."),
        ("💖 Ketulusan & Kebaikan Hati", "Kamu memiliki hati yang lembut dan empati yang tulus. Caramu peduli pada orang lain membuatmu selalu istimewa di mata mereka."),
        ("🌟 Jiwa yang Kuat & Bersemangat", "Seperti Sakura yang tak pernah menyerah untuk tumbuh menjadi sosok hebat, kamu juga selalu berjuang pantang menyerah untuk hal-hal yang kamu impikan."),
        ("🕊️ Kehadiran yang Menyejukkan", "Berada di dekatmu memberikan rasa nyaman layaknya menemukan rumah tempat beristirahat setelah perjalanan yang panjang."),
        ("✨ Cahaya Penuntun (Nur Hidayah)", "Namamu adalah doa yang nyata. Kehadiranmu membawa cahaya positif dan bimbingan kebaikan ke mana pun kamu melangkah.")
    ]

    reasons_html = ""
    for title, desc in reasons:
        reasons_html += f"""
        <div class="reason-card">
            <b style="color: #ffb7c5; font-size: 1.08rem;">{title}</b><br>
            <span style="color: #e0e0e0; font-size: 0.96rem; line-height: 1.65; display: inline-block; margin-top: 4px;">{desc}</span>
        </div>
        """
    st.html(reasons_html)

# ----------------- INTERACTIVE WISH WALL (BUKU DOA & HARAPAN) -----------------
with st.container(border=True):
    st.html('<div class="card-title">📝 Dinding Doa & Harapan untuk Hidayah</div>')
    st.write("Tuliskan doa atau pesan manis untuk menambah kebahagiaan Nur Hidayah hari ini:")

    with st.form("wish_form", clear_on_submit=True):
        col_w1, col_w2 = st.columns([1, 2])
        with col_w1:
            sender_name = st.text_input("Nama Pengirim:", placeholder="Misal: Hasim / Teman")
        with col_w2:
            user_wish = st.text_input("Pesan / Doa Ulang Tahun:", placeholder="Tulis ucapan tulusmu di sini...")
        
        submit_wish = st.form_submit_button("💌 Kirimkan Doa & Ucapan 🌸")
        
        if submit_wish:
            if user_wish.strip():
                final_sender = sender_name.strip() if sender_name.strip() else "Pengagum Rahasia"
                st.session_state.wishes.insert(0, {
                    "sender": final_sender,
                    "wish": user_wish.strip(),
                    "time": "Baru saja"
                })
                st.success("Doa berhasil dipajang di dinding harapan! 🌸✨")
                st.rerun()
            else:
                st.warning("Mohon tuliskan pesan atau doamu terlebih dahulu.")

    # Display all wishes
    wishes_html = "<div style='margin-top: 1.2rem;'>"
    for item in st.session_state.wishes:
        wishes_html += f"""
        <div style="background: rgba(22, 18, 33, 0.75); border-left: 3px solid #ff758c; padding: 14px 20px; border-radius: 12px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <b style="color: #ff9ebb; font-size: 0.98rem;">🌸 {item['sender']}</b>
                <span style="color: #8395a7; font-size: 0.78rem;">{item['time']}</span>
            </div>
            <div style="color: #f1f2f6; font-size: 0.95rem; line-height: 1.55;">{item['wish']}</div>
        </div>
        """
    wishes_html += "</div>"
    st.html(wishes_html)

# ----------------- FOOTER -----------------
st.html(
    """
    <div class="footer-text">
        Dibuat dengan segenap cinta & kehangatan untuk merayakan hari kelahiran ke-22 <b>Nur Hidayah</b> 🌸<br>
        <span style="font-family: 'Noto Serif JP', serif; color: #ffb7c5; font-size: 0.92rem; letter-spacing: 2px;">
            「また今度な... ありがとう」 (Mata kondo na... Arigatou)
        </span>
    </div>
    """
)
