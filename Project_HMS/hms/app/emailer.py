import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.exceptions import EmailError
from app.logger import logger

# Configs (in real-world projects, load from env vars)
app_password = 'bervzctemfhfhaln'
from_address = 'stutisharma1409@gmail.com'
to_address = 'sharmastuti14901@gmail.com'


def send_email(to_address, subject, body):
    """Send an email using Gmail SMTP"""
    try:
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, app_password)
        server.send_message(msg)
        server.quit()

        logger.info(f"Email sent successfully to {to_address} with subject: {subject}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise EmailError(str(e))