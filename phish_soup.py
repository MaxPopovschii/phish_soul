import os
from emailgenerator import EmailGenerator
from landingpagegenerator import LandingPageGenerator
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_DIR = 'templates'
LANDING_DIR = 'landings'
os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(LANDING_DIR, exist_ok=True)

class PhishSoulCLI:
    LANDING_NAME_PROMPT = "Landing name: "
    SUBJECT_PROMPT = "Subject: "
    BODY_PROMPT = "Body: "

    def __init__(self):
        self.emailgen = EmailGenerator()
        self.landinggen = LandingPageGenerator()

    def print_ascii_logo(self):
        print(r"""

 ██▓███   ██░ ██  ██▓  ██████  ██░ ██      ██████  ▒█████   █    ██  ██▓███  
▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒   ▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██░  ██▒
▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░   ░ ▓██▄   ▒██░  ██▒▓██  ▒██░▓██░ ██▓▒
▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██      ▒   ██▒▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒
▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓   ▒██████▒▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░
▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░     
░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░   ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░ ░░       
          ░  ░  ░ ░        ░   ░  ░  ░         ░      ░ ░     ░              

 """)

    def main_menu(self):
        while True:
            self.print_ascii_logo()
            print("Welcome to PHISH_SOUP!")
            print("1. Manage email templates")
            print("2. Manage landing pages")
            print("3. Send email")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.manage_email_templates()
            elif choice == '2':
                self.manage_landing_pages()
            elif choice == '3':
                self.send_email_cli()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")

    def manage_email_templates(self):
        name = input("Template name: ")
        subject = input(self.SUBJECT_PROMPT)
        body = input(self.BODY_PROMPT)
        self.emailgen.generate_email_template(name, subject, body)

    def manage_landing_pages(self):
        print("\n--- Manage Landing Pages ---")
        print("1. Create custom landing page")
        print("2. Create Instagram clone landing page")
        print("3. Create Facebook clone landing page")
        print("4. Open a landing page in browser")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input(self.LANDING_NAME_PROMPT)
            title = input("Title: ")
            message = input("Message: ")
            self.landinggen.generate_landing(name, title, message)
        elif choice == '2':
            name = input(self.LANDING_NAME_PROMPT)
            self.landinggen.generate_instagram_clone(name)
        elif choice == '3':
            name = input(self.LANDING_NAME_PROMPT)
            self.landinggen.generate_facebook_clone(name)
        elif choice == '4':
            self.open_landing_in_browser()
        else:
            print("Invalid option.")

    def open_landing_in_browser(self):
        landings = [f for f in os.listdir(LANDING_DIR) if f.endswith('.html')]
        if not landings:
            print("No landing pages found.")
            return
        print("Available landing pages:")
        for idx, l in enumerate(landings):
            print(f"{idx+1}. {l}")
        sel = input("Choose the landing page number: ").strip()
        try:
            sel_idx = int(sel) - 1
            landing_path = os.path.abspath(os.path.join(LANDING_DIR, landings[sel_idx]))
            os.system(f'$BROWSER "file://{landing_path}"')
        except Exception as e:
            print(f"Error opening landing page: {e}")

    def send_email_cli(self):
        print("\n--- Send Email ---")
        use_template = input("Do you want to use a pre-made template? (y/n): ").strip().lower() == 'y'
        if use_template:
            templates = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith('.txt')]
            if not templates:
                print("No templates found.")
                return
            print("Available templates:")
            for idx, t in enumerate(templates):
                print(f"{idx+1}. {t}")
            sel = input("Choose the template number: ").strip()
            try:
                sel_idx = int(sel) - 1
                template_path = os.path.join(TEMPLATE_DIR, templates[sel_idx])
                with open(template_path, 'r') as f:
                    lines = f.readlines()
                    subject = lines[0].strip() if lines else ""
                    body = "".join(lines[1:]).strip() if len(lines) > 1 else ""
            except Exception as e:
                print(f"Error selecting template: {e}")
                return
        else:
            subject = input(self.SUBJECT_PROMPT).strip() or os.getenv("SMTP_SUBJECT")
            body = input(self.BODY_PROMPT).strip() or os.getenv("SMTP_BODY")

        smtp_host = input("SMTP host (e.g. smtp.gmail.com): ").strip() or os.getenv("SMTP_HOST")
        smtp_port_input = input("SMTP port (e.g. 587): ").strip()
        smtp_port = int(smtp_port_input) if smtp_port_input else int(os.getenv("SMTP_PORT", "587"))
        sender = input("Sender: ").strip() or os.getenv("SMTP_SENDER")
        recipient = input("Recipient: ").strip() or os.getenv("SMTP_RECIPIENT")
        use_auth_input = input("Use SMTP authentication? (y/n): ").strip()
        use_auth = (use_auth_input or os.getenv("SMTP_USE_AUTH", "n")).lower() == 'y'
        if use_auth:
            os.environ['SMTP_USER'] = input("SMTP username: ").strip() or os.getenv("SMTP_USER")
            os.environ['SMTP_PASS'] = input("SMTP password: ").strip() or os.getenv("SMTP_PASS")
        use_ssl_input = input("Use SSL? (y/n): ").strip()
        use_ssl = (use_ssl_input or os.getenv("SMTP_SSL", "n")).lower() == 'y'
        use_tls_input = input("Use TLS? (y/n): ").strip()
        use_tls = (use_tls_input or os.getenv("SMTP_TLS", "n")).lower() == 'y'
        os.environ['SMTP_SSL'] = 'true' if use_ssl else 'false'
        os.environ['SMTP_TLS'] = 'true' if use_tls else 'false'
        try:
            self.emailgen.send_email(smtp_host, smtp_port, sender, recipient, subject, body)
        except Exception as e:
            print(f"Error sending email: {e}")

if __name__ == "__main__":
    PhishSoulCLI().main_menu()
