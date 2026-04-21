from fastapi import FastAPI
import uvicorn
from src.routes.chat_router import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "DishaAI Backend Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)