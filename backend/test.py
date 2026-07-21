from app.AI.preprocessing import preprocess_email
from app.schemas.email_schema import emailrequest

email = emailrequest(
    sender="attacker@evil.com",

    subject="""
        <h1>URGENT</h1>

        Verify your account at

        https://fake-login.com
    """,

    body="""
        Dear User,

        Contact us at support@evil.com

        Click here:

        https://fake-login.com

        Thank you.
    """
)

result = preprocess_email(email)

print(result)
