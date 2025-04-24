from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import pdfplumber
from docx import Document
import io

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        file_ext = file.filename.split(".")[-1].lower()
        
        if file_ext == "pdf":
            return JSONResponse(content={"text": extract_pdf(content)})
        elif file_ext == "docx":
            return JSONResponse(content={"text": extract_docx(content)})
        elif file_ext == "txt":
            return JSONResponse(content={"text": extract_txt(content)})
        elif file_ext in ["xls", "xlsx"]:
            return JSONResponse(content={"text": extract_excel(content)})
        elif file_ext == "csv":
            return JSONResponse(content={"text": extract_csv(content)})
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def extract_pdf(content: bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
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
