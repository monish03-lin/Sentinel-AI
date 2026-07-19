from pydantic import BaseModel

class URLrequest(BaseModel):
    url: str
    username : str