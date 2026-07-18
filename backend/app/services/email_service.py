from backend.app.schemas.email_schema import emailrequest


def scan_email(emrequest: emailrequest):
    
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