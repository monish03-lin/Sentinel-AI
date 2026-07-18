from datetime import datetime

from backend.app.schemas.url_schema import URLrequest
from backend.app.database import SessionLocal
from backend.app.models.scan import ScanHistory


def analyze(request: URLrequest):

    db= SessionLocal()

    scan = ScanHistory(
        scan_type="URL",
        input_data=request.url,
        risk_score=92,
        explanation="High Risk: Misspelled domain, looks like a login page, requests credentials",
        scan_date=datetime.utcnow()
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)
    db.close()

    return {
        "url" : request.url,
        "username": request.username,
        "risk_score": 92,
        "status": "High Risk",
        "reason": [
            "Misspelled domain",
            "Looks like a login page",
            "Requests credentials"
        ]
    }