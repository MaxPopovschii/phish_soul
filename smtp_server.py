import aiosmtpd.controller
import asyncio

class CustomHandler:
    async def handle_data(self, server, session, envelope):
        await asyncio.sleep(0)
        print(f"Email ricevuta da: {envelope.mail_from}")
        print(f"Destinatari: {envelope.rcpt_tos}")
        print(f"Contenuto:\n{envelope.content.decode('utf8', errors='replace')}")
        return '250 Message accepted for delivery'

def run_smtp_server(host='localhost', port=1025):
    controller = aiosmtpd.controller.Controller(CustomHandler(), hostname=host, port=port)
    controller.start()
    print(f"SMTP server in ascolto su {host}:{port}")
    try:
        while True:
            asyncio.sleep(1)
    except KeyboardInterrupt:
        controller.stop()

if __name__ == "__main__":
    run_smtp_server()
