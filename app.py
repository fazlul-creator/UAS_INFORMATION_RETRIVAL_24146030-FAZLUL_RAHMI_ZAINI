import streamlit as st
import json
import os

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Book Search (Scraped via Scrapy)",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Search (Scraped via Scraped)")

# 2. Lokasi File Data
DATA_PATH = "data/books.json"

# 3. Load Data JSON
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# 4. Form Input Pencarian
query = st.text_input("Cari..", "")

# 5. Logika Filter Pencarian
if query.strip():
    filtered = [
        item for item in data 
        if item.get("title") and query.lower() in item["title"].lower()
    ]
else:
    filtered = data

# 6. Menampilkan Jumlah Hasil
st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")

# 7. Menampilkan Daftar Buku
for item in filtered:
    title = item.get("title", "No Title")
    price = item.get("price", "N/A")
    rating = item.get("rating", "N/A")
    availability = item.get("availability", "N/A")
    link = item.get("link", "#")

    st.markdown(f"### [{title}]({link})")
    st.markdown(f"**Price:** `{price}` | **Rating:** `{rating}` | **Availability:** `{availability}`")
    st.markdown("---")