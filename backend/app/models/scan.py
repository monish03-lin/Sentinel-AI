from sqlalchmey import Column, Integer, String, DateTime
from app.database import base

class ScanHistory(base):
    __tablename__ = "Scan_History"

    id = Column(Integer, primary_key=True, index=True)
    scan_type = Column(String)
    input_data = Column(String)
    risk_score = Column(Integer)
    explanation = Column(String)
    scan_date = Column(DateTime)