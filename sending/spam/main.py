

class SendingSpam:

    def __init__(self, session, sending): 
        self.session = session
        self.sending = sending

    def send_emails(self, to, title, body):
        self.to = to
        self.title = title
        self.body = body
