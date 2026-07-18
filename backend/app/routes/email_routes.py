from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.dependencies import get_db
from backend.app.schemas.email_schema import emailrequest
from backend.app.services.email_service import scan_email

router = APIRouter()

@router.post("/scan_email")
def scan_email_route(request: emailrequest, db: Session = Depends(get_db)):
     return scan_email(request, db)
    