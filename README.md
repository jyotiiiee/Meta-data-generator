 # Metadata-Generator

An intelligent system that automatically extracts and generates semantically rich metadata from various document formats (PDF, DOCX, TXT, images) using advanced OCR and the Mistral LLM API. This improves document discoverability, classification, and analysis with minimal manual effort.

---

## Features

- *Multi-format support:* Extract text from PDF, DOCX, TXT, and image files (JPG, PNG) using OCR.
- *Semantic metadata generation:* Use Mistral API to generate structured metadata including title, summary, keywords, document type, and main topics.
- *User-friendly UI:* Streamlit-based web interface for easy document upload, metadata preview, and download.
- *Download metadata:* Download generated metadata as a JSON file.
- *Extensible and modular:* Clear separation of extraction, metadata generation, and UI layers for easy enhancement.

---

## Getting Started

### Prerequisites
- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and configured
- Mistral API key ([sign up here](https://mistral.ai))

### Installation

1. Clone the repo:
    bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    

2. Create and activate a virtual environment:
    bash
    python -m venv venv
    source venv/bin/activate      # Linux/macOS
    venv\Scripts\activate         # Windows
    

3. Install dependencies:
    bash
    pip install -r requirements.txt
    
4. Create a .env file and add your Mistral API key:
    env
    MISTRAL_API_KEY=your_api_key_here
    

5. Install Tesseract OCR:
   - *Windows:* Download the installer from [here](https://github.com/tesseract-ocr/tesseract/wiki)
   - *macOS:* Use brew install tesseract
   - *Linux:* Use sudo apt install tesseract-ocr

6. Configure the Tesseract executable path in extractor.py if needed:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract.exe'
