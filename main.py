from fastapi import FastAPI
from app import routes

app = FastAPI()

app.include_router(routes.router, tags=["DocChatbot"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
