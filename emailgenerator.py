import os
from email.message import EmailMessage
import smtplib

TEMPLATE_DIR = 'templates'
os.makedirs(TEMPLATE_DIR, exist_ok=True)

class EmailGenerator:
    def __init__(self, template_dir=TEMPLATE_DIR):
        self.template_dir = template_dir
        os.makedirs(self.template_dir, exist_ok=True)

    def generate_email_template(self, name, subject, body):
        template = f"Subject: {subject}\n\n{body}"
        path = os.path.join(self.template_dir, f"{name}.eml")
        with open(path, 'w') as f:
            f.write(template)
        print(f"Template email generato: {path}")

    def send_email(self, smtp_host, smtp_port, sender, recipient, subject, body):
        msg = EmailMessage()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.set_content(body)

        smtp_user = os.environ.get('SMTP_USER')
        smtp_pass = os.environ.get('SMTP_PASS')
        use_tls = os.environ.get('SMTP_TLS', 'false').lower() == 'true'
        use_ssl = os.environ.get('SMTP_SSL', 'false').lower() == 'true'

        if use_ssl:
            server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port)
            if use_tls:
                server.starttls()
        if smtp_user and smtp_pass:
            server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        print(f"Email inviata a {recipient}")
