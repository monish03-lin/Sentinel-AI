from pydantic import BaseModel

class emailrequest(BaseModel):
    sender: str
    subject: str
    body: str