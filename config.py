import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASS = os.getenv('SMTP_PASS')
    SMTP_HOST = os.getenv('SMTP_HOST', 'localhost')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '1025'))
    SMTP_SSL = os.getenv('SMTP_SSL', 'false').lower() == 'true'
    SMTP_TLS = os.getenv('SMTP_TLS', 'false').lower() == 'true'
    TEMPLATE_DIR = os.getenv('TEMPLATE_DIR', 'templates')
    LANDING_DIR = os.getenv('LANDING_DIR', 'landings')
