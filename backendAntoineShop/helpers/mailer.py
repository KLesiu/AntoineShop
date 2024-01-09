from fastapi.security import OAuth2PasswordBearer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

email_config = {
    "email_address": os.getenv('email_address'),
    "email_password": os.getenv('email_password'),
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def send_verification_email(email_to: str, verification_token: str):
    msg = MIMEMultipart()
    msg['From'] = email_config["email_address"]
    msg['To'] = email_to
    msg['Subject'] = 'Email Verification'

    body = f'Your verification code: {verification_token}'
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
        server.starttls()
        server.login(email_config["email_address"], email_config["email_password"])
        server.sendmail(email_config["email_address"], email_to, msg.as_string())

def send_email_after_purchase(email_to: str,price:float,items,address:str):
    msg = MIMEMultipart()
    msg['From'] = email_config["email_address"]
    msg['To'] = email_to
    msg['Subject'] = 'Thank You for your order from our store!'

    body = f'Your order:/n'
    for item in items:
        body += f'-{item["name"]}'
    for item in items:
        body += f'(size:{item["size"]}) /n'
    body += f'Price: {price} /n'
    body += f'Your order will be available to pick in 5 days at {address}'
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP(email_config["smtp_server"],email_config["smtp_port"]) as server:
        server.starttls()
        server.login(email_config["email_address"],email_config["email_password"])
        server.sendmail(email_config["email_address"],email_to,msg.as_string())

    


