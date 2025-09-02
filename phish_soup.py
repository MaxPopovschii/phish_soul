import os
from emailgenerator import EmailGenerator
from landingpagegenerator import LandingPageGenerator

TEMPLATE_DIR = 'templates'
LANDING_DIR = 'landings'
os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(LANDING_DIR, exist_ok=True)

class PhishSoulCLI:
    LANDING_NAME_PROMPT = "Landing name: "

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
            print("Welcome to PHISH_SOUL!")
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
        print("\n--- Manage Email Templates ---")
        name = input("Template name: ")
        subject = input("Subject: ")
        body = input("Body: ")
        self.emailgen.generate_email_template(name, subject, body)

    def manage_landing_pages(self):
        print("\n--- Manage Landing Pages ---")
        print("1. Create custom landing page")
        print("2. Create Instagram clone landing page")
        print("3. Create Facebook clone landing page")
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
        else:
            print("Invalid option.")

    def send_email_cli(self):
        print("\n--- Send Email ---")
        smtp_host = input("SMTP host (e.g. smtp.gmail.com): ")
        smtp_port = int(input("SMTP port (e.g. 465): "))
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        subject = input("Subject: ")
        body = input("Body: ")
        use_auth = input("Use SMTP authentication? (y/n): ").lower() == 'y'
        if use_auth:
            os.environ['SMTP_USER'] = input("SMTP username: ")
            os.environ['SMTP_PASS'] = input("SMTP password: ")
        use_ssl = input("Use SSL? (y/n): ").lower() == 'y'
        use_tls = input("Use TLS? (y/n): ").lower() == 'y'
        os.environ['SMTP_SSL'] = 'true' if use_ssl else 'false'
        os.environ['SMTP_TLS'] = 'true' if use_tls else 'false'
        try:
            self.emailgen.send_email(smtp_host, smtp_port, sender, recipient, subject, body)
        except Exception as e:
            print(f"Error sending email: {e}")

if __name__ == "__main__":
    PhishSoulCLI().main_menu()
