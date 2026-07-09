from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "status": "Backend Running",
        "version": "1.0"
    }

@app.get("/about")
def about():
    return {
        "project": "Sentinel AI",
        "description": "Sentinel AI is a cutting-edge artificial intelligence platform designed to provide advanced analytics and insights for various industries. Our mission is to empower businesses with intelligent solutions that drive innovation and efficiency.",

    }
    