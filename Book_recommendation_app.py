import streamlit as st
import pickle
import pandas as pd

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Folio — Book Recommender",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CUSTOM CSS  — warm editorial / bookstore feel
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Lato:wght@300;400;700&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: #f5f0e8;
    color: #2c2c2c;
}

.main .block-container {
    padding: 2rem 4rem 4rem 4rem;
    max-width: 1400px;
}

/* ── Hero ── */
.hero-wrap {
    text-align: center;
    padding: 3.5rem 1rem 2rem 1rem;
    position: relative;
}
.hero-wrap::before {
    content: "";
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 700px; height: 260px;
    background: radial-gradient(ellipse at center, rgba(74,103,65,0.13) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(74,103,65,0.12);
    border: 1px solid rgba(74,103,65,0.35);
    color: #4a6741;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 0.28rem 0.9rem;
    border-radius: 100px;
    margin-bottom: 1.2rem;
    font-family: 'Lato', sans-serif;
    font-weight: 700;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: clamp(3.2rem, 8vw, 6rem);
    letter-spacing: 0.02em;
    line-height: 1;
    color: #1e2d1a;
    margin: 0 0 0.5rem 0;
}
.hero-title em {
    font-style: italic;
    color: #4a6741;
}
.hero-sub {
    color: #7a7060;
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 0.02em;
    margin-bottom: 2.5rem;
}

/* ── Decorative line ── */
.deco-line {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin: 0.5rem 0 2rem 0;
    color: #b0a898;
    font-size: 0.85rem;
    letter-spacing: 0.3em;
}
.deco-line::before, .deco-line::after {
    content: "";
    width: 80px;
    height: 1px;
    background: linear-gradient(to right, transparent, #b0a898);
}
.deco-line::after {
    background: linear-gradient(to left, transparent, #b0a898);
}

/* ── Search label ── */
.search-label {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7a7060;
    font-weight: 700;
    margin-bottom: 0.4rem;
}

/* ── Selectbox ── */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1.5px solid #d4ccbc !important;
    border-radius: 10px !important;
    color: #2c2c2c !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.55rem 1rem !important;
    min-height: 52px !important;
    transition: border-color 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
}
div[data-baseweb="select"] > div:hover {
    border-color: #4a6741 !important;
    box-shadow: 0 2px 12px rgba(74,103,65,0.15) !important;
}
div[data-baseweb="select"] svg { fill: #7a7060 !important; }

/* dropdown list */
div[data-baseweb="popover"] * {
    background-color: #ffffff !important;
    color: #2c2c2c !important;
    font-family: 'Lato', sans-serif !important;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #4a6741 0%, #2e4228 100%) !important;
    color: #f5f0e8 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.75rem 2rem !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(74,103,65,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(74,103,65,0.45) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Selected banner ── */
.selected-banner {
    background: linear-gradient(135deg, rgba(74,103,65,0.1) 0%, rgba(46,66,40,0.05) 100%);
    border: 1px solid rgba(74,103,65,0.25);
    border-radius: 12px;
    padding: 0.9rem 1.4rem;
    margin: 1.2rem 0;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 0.9rem;
    color: #5a5248;
}
.selected-banner .book-icon { font-size: 1.3rem; }
.selected-banner .book-name {
    color: #1e2d1a;
    font-weight: 700;
}

/* ── Section heading ── */
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    font-style: italic;
    color: #1e2d1a;
    margin: 2.5rem 0 1.4rem 0;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.section-heading::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, #c8bfaf, transparent);
    margin-left: 0.5rem;
}

/* ── Book card ── */
.book-card {
    background: #ffffff;
    border: 1px solid #e2d9cc;
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    height: 100%;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.book-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.13);
    border-color: #4a6741;
}
.book-card-img-wrap {
    background: #f0ebe0;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    min-height: 220px;
}
.book-card-img-wrap img {
    max-height: 200px;
    width: auto;
    max-width: 100%;
    display: block;
    border-radius: 4px;
    box-shadow: 4px 6px 20px rgba(0,0,0,0.18);
}
.book-card-body {
    padding: 0.85rem 1rem 1rem 1rem;
    border-top: 1px solid #f0ebe0;
}
.book-card-rank {
    font-size: 0.62rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #4a6741;
    font-weight: 700;
    margin-bottom: 0.3rem;
}
.book-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 0.92rem;
    color: #1e2d1a;
    line-height: 1.4;
    margin: 0;
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #ddd5c8;
    margin: 1.5rem 0;
}

/* ── No-image placeholder ── */
.no-img {
    width: 100%;
    height: 200px;
    background: linear-gradient(135deg, #e8e0d0, #d4ccbc);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    border-radius: 4px;
}

/* ── Footer ── */
.footer {
    text-align: center;
    color: #b0a898;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid #ddd5c8;
}

/* hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    books = pickle.load(open('books.pkl', 'rb'))
    similarity = pickle.load(open('similarity1.pkl', 'rb'))
    return books, similarity

books, similarity = load_data()

# ─────────────────────────────────────────────
# RECOMMEND FUNCTION  (unchanged logic)
# ─────────────────────────────────────────────
def recommend(book_name):
    if book_name not in books['title'].values:
        return [], []

    book_index = books[books['title'] == book_name].index[0]
    distances = similarity[book_index]

    books_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_books, recommended_images = [], []
    for i in books_list:
        recommended_books.append(books.iloc[i[0]].title)
        recommended_images.append(books.iloc[i[0]].thumbnail)

    return recommended_books, recommended_images

# ─────────────────────────────────────────────
# UI LAYOUT
# ─────────────────────────────────────────────

# ── Hero ──
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">✦ Content-Based Recommendation</div>
    <h1 class="hero-title"><em>Folio</em></h1>
    <p class="hero-sub">Tell us a book you love — we'll find five more worth reading.</p>
    <div class="deco-line">✦</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Search row ──
col_select, col_btn = st.columns([5, 1.2], gap="medium")

with col_select:
    st.markdown('<p class="search-label">📖 Choose a Book</p>', unsafe_allow_html=True)
    selected_book = st.selectbox(
        label="",
        options=books['title'].values,
        label_visibility="collapsed"
    )

with col_btn:
    st.markdown('<p class="search-label">&nbsp;</p>', unsafe_allow_html=True)
    recommend_clicked = st.button("✦ Recommend")

# ── Selected banner ──
if selected_book:
    st.markdown(f"""
    <div class="selected-banner">
        <span class="book-icon">📗</span>
        <span>Currently selected: <span class="book-name">{selected_book}</span></span>
    </div>
    """, unsafe_allow_html=True)

# ── Results ──
if recommend_clicked:
    with st.spinner("Turning the pages…"):
        names, images = recommend(selected_book)

    if names:
        st.markdown('<div class="section-heading">Recommended For You</div>', unsafe_allow_html=True)

        cols = st.columns(5, gap="medium")
        rank_labels = ["Top Pick", "2nd Pick", "3rd Pick", "4th Pick", "5th Pick"]

        for i, col in enumerate(cols):
            with col:
                # Poster or fallback
                img_html = (
                    f'<img src="{images[i]}" alt="{names[i]}" />'
                    if images[i] and str(images[i]).startswith("http")
                    else '<div class="no-img">📚</div>'
                )
                st.markdown(f"""
                <div class="book-card">
                    <div class="book-card-img-wrap">
                        {img_html}
                    </div>
                    <div class="book-card-body">
                        <div class="book-card-rank">{rank_labels[i]}</div>
                        <p class="book-card-title">{names[i]}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Book not found in our library!")

# ── Footer ──
st.markdown("""
<div class="footer">
    FOLIO &nbsp;·&nbsp; Content-Based Book Recommendation Engine &nbsp;·&nbsp; Books Dataset
</div>
""", unsafe_allow_html=True)