from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.dependencies import get_db
from backend.app.models.scan import ScanHistory

def get_history(db :Session = Depends(get_db) ):
    history= db.query(ScanHistory).all()
    return history