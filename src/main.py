# TODO: Here is the main, call the llm from the server
import uvicorn
from fastapi import FastAPI
from api.route import router

app = FastAPI(title="BEON.tech AI Assistant")
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)