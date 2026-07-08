from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "status": "Backend Running",
        "version": "1.0"
    }