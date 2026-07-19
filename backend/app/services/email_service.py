from backend.app.schemas.email_schema import emailrequest
from sqlalchemy.orm import Session
from backend.app.models.scan import ScanHistory
from datetime import datetime

def scan_email(emrequest: emailrequest, db :Session):

    scan = ScanHistory(
        scan_type="Email",
        input_data=emrequest.subject,
        risk_score=85,
        explanation="Suspicious sender domain, urgent language, contains links",
        scan_date=datetime.utcnow()
    
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)

    return{
            "sender": emrequest.sender,
            "subject": emrequest.subject,
            "body": emrequest.body,
            "risk_score": 85,
            "status": "Potential Phishing",
            "reason": [
            "Suspicious sender domain",
            "Urgent language in subject",
            "Contains links to unknown sites"
            ]
        }