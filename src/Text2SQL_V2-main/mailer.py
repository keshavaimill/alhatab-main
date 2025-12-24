import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()


import logging

def setup_logger():
    """
    Sets up a logger with a console handler.
    """
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set minimum log level

    # Prevent adding multiple handlers if setup_logger is called multiple times
    if not logger.handlers:
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Handler log level

        # Create formatter for log messages
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(console_handler)

    return logger
logger = setup_logger()
try:
    logger.info("📧 Mailer configuration loaded")
    SMTP_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("MAIL_PORT", 587))
    SMTP_USER = os.getenv("MAIL_USERNAME")
    SMTP_PASSWORD = os.getenv("MAIL_PASSWORD")

except:
    logger.error("❌ Failed to load mailer configuration")
    

ALERT_EMAILS = [
    e.strip()
    for e in os.getenv("ALERT_EMAILS", "").split(",")
    if e.strip()
]

def send_success_email(subject, body):
    if not ALERT_EMAILS:
        logger.info("⚠️ ALERT_EMAILS not configured")
        return

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = ", ".join(ALERT_EMAILS)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        logger.info("✅ Email sent")
    except Exception as e:
        logger.info("❌ Email failed:", e)

