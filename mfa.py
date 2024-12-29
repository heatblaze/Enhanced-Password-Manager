import random
from twilio.rest import Client
from email.mime.text import MIMEText
import smtplib

# Twilio Setup (For SMS-based MFA)
TWILIO_PHONE = '+91 8418071066'
TWILIO_SID = 'AC6ab131ddc3cdc64c9023c1910a587c97'
TWILIO_AUTH_TOKEN = '9e753b49f71506a2b912bb39aa544e22'
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Email Setup (For Email-based MFA)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'  # Use App Password for Gmail


def send_email_otp(email):
    """Send OTP to the user's email."""
    otp = str(random.randint(100000, 999999))
    subject = "Your OTP for Enhanced Password Manager"
    body = f"Your OTP is: {otp}\nThis OTP will expire in 5 minutes."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email, msg.as_string())
        return otp
    except Exception as e:
        print(f"Failed to send OTP via email: {e}")
        return None


def send_sms_otp(phone_number):
    """Send OTP to the user's phone number via SMS using Twilio."""
    otp = str(random.randint(100000, 999999))

    message = client.messages.create(
        body=f"Your OTP is: {otp}. This OTP will expire in 5 minutes.",
        from_=TWILIO_PHONE,
        to=phone_number
    )

    return otp
