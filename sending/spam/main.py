

class SendingSpam:

    def __init__(self, session, sending): 
        self.session = session
        self.sending = sending

    def send_emails(self, to, title, body):
        for user in self.session.show():
            self.sending.send(
                to,
                title,
                body
            )

