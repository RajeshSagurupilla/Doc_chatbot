from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.extractor import extract_file_content

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = extract_file_content(file.filename, content)
        return JSONResponse(content={"text": text})
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
