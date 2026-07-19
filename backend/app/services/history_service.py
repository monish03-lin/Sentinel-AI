
from sqlalchemy.orm import Session
from backend.app.models.scan import ScanHistory

def get_history(db :Session):
    history= db.query(ScanHistory).all()
    return history