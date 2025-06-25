import pdfplumber
from pdf2image import convert_from_path
import docx
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(file_path, file_ext):
    if file_ext == "pdf":
        return extract_text_from_pdf(file_path)
    elif file_ext == "docx":
        return extract_text_from_docx(file_path)
    elif file_ext == "txt":
        return open(file_path, "r", encoding="utf-8").read()
    elif file_ext in ["jpg", "jpeg", "png"]:
        return pytesseract.image_to_string(file_path)
    return ""

def extract_text_from_pdf(file_path):
    # Try digital text extraction first
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        # Fallback to OCR if no digital text found
        print("No digital text found in PDF. Using OCR...")
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"

    return text.strip()

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
