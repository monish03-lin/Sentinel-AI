"""Every incoming email passes through this module before being processed by the AI model. It is responsible for cleaning and preprocessing the email content to ensure that the AI model receives data in a consistent and usable format."""


import re
from dataclasses import dataclass
from typing import List
from app.schemas.email_schema import emailrequest 
@dataclass
class preprocessing_result:
    """A dataclass to hold the results of the preprocessing step."""
    sender: str
    clean_subject: str
    clean_body: str
    email_addresses: List[str]
    urls: List[str] 
    
def normalize_whitespace(text:str) -> str:
        if not text:
            return ""
        normalized_text= re.sub(r"\s+", " ", text)
        return normalized_text.strip()

def remove_html(text:str) -> str:
        if not text:
            return ""
        return re.sub(r"<[^>]+>", "", text)
    
def extract_urls_text(text:str) -> list:
        if not text:
            return[]
        return re.findall(r"https?://[^\s]+", text)
    
def extract_email_addresses(text : str) ->list:
        if not text:
            return []
        email_pattern = (r"\b[a-zA-Z0-9._%+-]+"
                       r"@[a-zA-Z0-9.-]+"
                       r"\.[a-zA-Z]{2,}\b")
        return re.findall(email_pattern, text)
    
def preprocess_email(email : emailrequest) -> preprocessing_result:
        

        subject_urls = extract_urls_text(email.subject)
        body_urls = extract_urls_text(email.body)

        urls = list(set(subject_urls + body_urls))

        subject_email_addresses = extract_email_addresses(email.subject)
        body_email_addresses = extract_email_addresses(email.body)

        email_addresses = list(
        set(subject_email_addresses + body_email_addresses)
    )


        clean_subject = remove_html(email.subject)
        clean_subject = normalize_whitespace(clean_subject)



        clean_body = remove_html(email.body)
        clean_body = normalize_whitespace(clean_body)

    
        return preprocessing_result(
        sender=email.sender,
        clean_subject=clean_subject,
        clean_body=clean_body,
        urls=urls,
        email_addresses=email_addresses,
    )


        
        return preprocessing_result(cleaned_text=cleaned_text, 
                                    email_addresses=email_addresses,
                                    urls=urls)















