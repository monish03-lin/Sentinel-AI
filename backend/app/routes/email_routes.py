from fastapi import APIRouter
from backend.app.schemas.email_schema import emailrequest
from backend.app.services.email_service import scan_email

router = APIRouter()

@router.post("/scan_email")
def scan_email_route(request: emailrequest):
    result = scan_email(request)
    return result