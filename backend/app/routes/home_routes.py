from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "status": "Backend Running",
        "version": "1.0",
    }


@router.get("/about")
def about():
    return {
        "project": "Sentinel AI",
        "description": "Sentinel AI is a phishing detection platform.",
    }