from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.dependencies import get_db
from backend.app.services.history_service import get_history

router = APIRouter()

@router.get("/history")
def get_history_route(db: Session = Depends(get_db)):
    history = get_history(db)
    return history