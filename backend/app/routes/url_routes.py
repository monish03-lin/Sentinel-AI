from fastapi import APIRouter
from backend.app.schemas.url_schema import URLrequest
from backend.app.services.url_service import analyze

router = APIRouter()
def analyze_url(request: URLrequest):
    result = analyze(request)
    return result