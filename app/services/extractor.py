import pandas as pd
import pdfplumber
from docx import Document
import io

def extract_file_content(filename: str, content: bytes) -> str:
    ext = filename.split(".")[-1].lower()

    if ext == "pdf":
        return extract_pdf(content)
    elif ext == "docx":
        return extract_docx(content)
    elif ext == "txt":
        return extract_txt(content)
    elif ext in ["xls", "xlsx"]:
        return extract_excel(content)
    elif ext == "csv":
        return extract_csv(content)
    else:
        raise ValueError("Unsupported file type.")

def extract_pdf(content: bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                text += f"[Page {i+1} has no extractable text]\n"
    return text.strip()


def extract_docx(content: bytes) -> str:
    doc = Document(io.BytesIO(content))
    return "\n".join([para.text for para in doc.paragraphs])

def extract_txt(content: bytes) -> str:
    return content.decode("utf-8", errors="ignore")

def extract_excel(content: bytes) -> str:
    df = pd.read_excel(io.BytesIO(content), engine="openpyxl")
    return df.to_string(index=False)

def extract_csv(content: bytes) -> str:
    df = pd.read_csv(io.BytesIO(content))
    return df.to_string(index=False)
