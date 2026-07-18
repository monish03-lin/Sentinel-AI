from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.database import engine, base
from backend.app.models.scan import ScanHistory


app = FastAPI()

base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "status": "Backend Running",
        "version": "1.0"
    }

@app.get("/about")
def about():
    return {
        "project": "Sentinel AI",
        "description": "Sentinel AI is a cutting-edge artificial intelligence platform designed to provide advanced analytics and insights for various industries. Our mission is to empower businesses with intelligent solutions that drive innovation and efficiency.",

    }

class URLrequest(BaseModel):
    url: str
    username : str

@app.post("/analyze")
def analyze(request: URLrequest):
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
    
class emailrequest(BaseModel):
    sender: str
    subject: str
    body: str
    
@app.post("/scan_email")
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

