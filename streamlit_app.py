import streamlit_app as st
from main import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Text Summarizer (T5-small)")

# Input text
text_input = st.text_area("Enter text to summarize:", height=200)

# Slider for summary length
max_len = st.slider("Maximum summary length", 30, 200, 100)
min_len = st.slider("Minimum summary length", 10, 80, 30)

if st.button("Summarize"):
    if text_input.strip():
        summary = summarize_text(text_input, max_length=max_len, min_length=min_len)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize.")
