from fastapi import APIRouter
from backend.app.schemas.url_schema import URLrequest
from backend.app.services.url_service import analyze
from sqlalchemy.orm import Session
from fastapi import Depends
from backend.app.dependencies import get_db


router = APIRouter()
@router.post("/analyze")
def analyze(request: URLrequest, db: Session=Depends(get_db)):
    return analyze(request,db)
   