# 📝 Text Summarizer Web App

This is a **Streamlit-based text summarizer web application** powered by the `t5-small` model from Hugging Face.  
The app allows you to input any text and generate concise summaries instantly.

---

## 🚀 Features
- Summarize large text into shorter versions
- Simple, user-friendly web interface using **Streamlit**
- Runs locally or can be deployed to **Streamlit Cloud**
- Lightweight model (`t5-small`) for faster inference

---

## 📂 Project Structure
text-summarizer/
│── models/ # Downloaded t5-small model files
│── main.py # Core summarization logic
│── streamlit.py # Streamlit web app
│── requirements.txt # Dependencies
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/WakeelDev/text-summarizer.git
cd text-summarizer
2. Create Virtual Environment (recommended)
bash
Copy code
conda create -n summarizer python=3.10 -y
conda activate summarizer
3. Install Requirements
bash
Copy code
pip install -r requirements.txt
4. Run Locally
bash
Copy code
streamlit run streamlit.py
🌐 Deployment on Streamlit Cloud
Push your project to GitHub (already done ✅).

Go to Streamlit Cloud.

Connect your GitHub repository.

Select streamlit.py as the entry point.

Add requirements.txt so Streamlit installs dependencies automatically.

Your app will be live in just a few minutes 🚀.

⚡ Requirements
Python 3.8+

Streamlit

Transformers

Torch

Git LFS (for handling large model files)

Install via:

bash
Copy code
pip install streamlit transformers torch
⚠️ Limitations of t5-small
While t5-small is lightweight and fast, it comes with some trade-offs:

Short context window: Handles only ~512 tokens (~400 words) at once. Long text must be chunked.

Generic summaries: Sometimes repeats input phrases (especially starting sentences).

Less accurate than larger models like t5-base or bart-large-cnn.

Not domain-specific: Works best for general text but may struggle with technical or niche content.

Summary length control: Options for minimum/maximum length don’t always produce strong variations.

👉 For more accurate and fluent summaries, consider upgrading to a larger model (e.g., t5-base, bart-large-cnn) — but note they require more memory and compute.

📌 Example
Input Text

pgsql
Copy code
Artificial Intelligence (AI) is a rapidly growing field of computer science
that focuses on creating intelligent machines that can perform tasks that
typically require human intelligence. These tasks include problem-solving,
learning, speech recognition, and decision-making.
Generated Summary

pgsql
Copy code
Artificial Intelligence is a fast-growing field focused on building
machines that perform tasks requiring human-like intelligence.
👤 Author
Developed by Wakeel Khan
🔗 GitHub Profile

yaml
Copy code

---

👉 Would you like me to also generate a **requirements.txt** file for you (so your README and deploym