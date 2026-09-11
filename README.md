# 🌸 Website Ucapan Ulang Tahun Nur Hidayah (Tema Sasuke & Sakura)

Website Streamlit interaktif bertema romantis **Sasuke & Sakura (*The Forehead Poke*)** yang dibuat khusus untuk merayakan ulang tahun **Nur Hidayah**.

---

## ✨ Fitur Utama
1. **Visual Sasuke & Sakura Forehead Poke**: Momen ikonik dengan styling frame bercahaya (*glow*).
2. **Animasi Kelopak Sakura Berguguran (Cherry Blossom Shower)**: Efek kelopak bunga sakura melayang lembut di latar belakang.
3. **Sentuhan Dahi Ikonik (Forehead Poke Interaktif) 👆**:
   - Menampilkan kutipan legendaris: `「また今度な... ありがとう」` (*Mata kondo na... Arigatou*).
   - Pesan romantis tulus dan kejutan balon.
4. **Kue Ulang Tahun Digital & Tiup Lilin 🎂**:
   - Lilin berkedip realistis.
   - Tombol "Make a Wish & Tiup Lilin" yang mematikan api dan memunculkan perayaan serta doa.
5. **Sepucuk Surat untuk Nur Hidayah 💌**:
   - Pesan mendalam mengenai makna nama *Nur Hidayah* (Cahaya Petunjuk) dan doa kebaikan.
6. **5 Hal Istimewa Tentang Nur Hidayah ✨**:
   - Kartu apresiasi sifat dan kebaikan hatinya.
7. **Dinding Doa & Harapan (Live Wish Wall) 📝**:
   - Tempat teman/keluarga/kamu menuliskan doa selamat ulang tahun.
8. **Musik Latar Romantis (BGM) 🎵**:
   - Pemutar musik piano yang menenangkan di bilah samping (*sidebar*).

---

## 🚀 Cara Menjalankan Website

Buka terminal (Command Prompt atau PowerShell) di folder project ini:

```bash
streamlit run app.py
```

Setelah itu, browser akan otomatis terbuka di alamat:
`http://localhost:8501`

---

## 🎨 Kustomisasi
- **Mengganti Musik (BGM)** (Ada 3 cara mudah):
  1. **Lewat Website Langsung**: Buka sidebar di kiri website, pilih **"Upload File MP3 Sendiri"** dan unggah file lagu kesukaan Anda/Nur Hidayah.
  2. **File Lokal Otomatis**: Letakkan file lagu MP3 Anda di dalam folder `assets/` dan beri nama `bgm.mp3` (`assets/bgm.mp3`). Website akan otomatis memutarnya!
  3. **Menggunakan Link/URL**: Pilih opsi **"Gunakan Link/URL Musik"** di sidebar atau ubah URL default di [app.py](file:///d:/Hasim/app.py).
- **Mengganti Gambar**: Letakkan gambar baru di folder `assets/sasuke_sakura.png`.
- **Menyesuaikan Ucapan**: Buka [app.py](file:///d:/Hasim/app.py) dan edit teks ucapan di bagian `Sepucuk Surat untuk Nur Hidayah`.

