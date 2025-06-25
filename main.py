import streamlit as st
from extractor import extract_text
from mistral_api import call_mistral
from utils import save_file
from utils import get_metadata_id
import os
from dotenv import load_dotenv
import json

# ✅ Page configuration — must be first
st.set_page_config(page_title="Automated Metadata Generator", layout="wide")

# # 🎨 Custom CSS — soft skin-colored background + improved widgets
# st.markdown("""
# <style>
#     body {
#         background-color: #fff5e6; /* Soft peach/skin color */
#     }
#     .stTextArea textarea {
#         background-color: #fffaf2;  /* Slightly lighter skin tone */
#         border: 1px solid #f1d6c6;
#         border-radius: 10px;
#         font-size: 15px;
#         padding: 12px;
#         color: #333;
#     }
#     .stCode {
#         background-color: #fff8dc;  /* Light cream for metadata box */
#         border-left: 6px solid #ffb74d;
#         border-radius: 8px;
#         padding: 10px;
#         font-size: 14px;
#         color: #3e3e3e;
#     }
#     .stSpinner > div > div {
#         color: #ff7043 !important;  /* Warm coral spinner text */
#         font-weight: bold;
#     }
#     .stDownloadButton {
#         background-color: #ffe0b2;
#         color: black;
#         font-weight: bold;
#         border-radius: 8px;
#         padding: 10px 20px;
#         border: none;
#         box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
#         transition: 0.3s ease-in-out;
#     }
#     .stDownloadButton:hover {
#         background-color: #ffcc80;
#     }
# </style>
# """, unsafe_allow_html=True)

load_dotenv()

# 🧾 Title
st.title("📄 Automated Metadata Generator (Mistral-powered)")

# 📁 Upload
uploaded = st.file_uploader("Upload Document", type=["pdf", "docx", "txt", "jpg", "jpeg", "png"])

if uploaded:
    with st.spinner("🔍 Processing... Please wait..."):
        file_path, ext = save_file(uploaded)
        text = extract_text(file_path, ext)

        if not text.strip():
            st.error("🚫 No text could be extracted from the file.")
        else:
            # Call Mistral API
            metadata_json = call_mistral(text)

            # ✅ Try parsing it
            try:
                metadata_dict = json.loads(metadata_json)
                is_valid_json = True
            except json.JSONDecodeError:
                metadata_dict = {"error": "⚠️ Failed to parse metadata."}
                is_valid_json = False

            # Display
            st.subheader("📌 Generated Metadata")
            if is_valid_json:
                st.json(metadata_dict)  # Pretty viewer
            else:
                st.code(metadata_json, language="text")  # Just show raw text fallback

            # ✅ Download button
            st.subheader("📖 Extracted Document Preview")
            st.text_area("Text Preview", text[:3000])
else:
    st.info("📎 Please upload a file to begin.")
