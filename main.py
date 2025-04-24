from fastapi import FastAPI
from app.routes import upload

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["Upload"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
