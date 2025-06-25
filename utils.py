import os
import hashlib
from datetime import datetime

def save_file(uploaded_file):
    filename = uploaded_file.name
    ext = filename.split('.')[-1]
    filepath = os.path.join("uploads", filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())
    return filepath, ext

def get_metadata_id(text):
    return hashlib.sha1(text.encode()).hexdigest()[:10]

import os

def save_file(uploaded_file):
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)  # ✅ Create uploads/ if not present

    filename = uploaded_file.name
    ext = filename.split('.')[-1]
    filepath = os.path.join(uploads_dir, filename)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    return filepath, ext

