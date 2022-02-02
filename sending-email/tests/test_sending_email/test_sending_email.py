import email
from sending_email.spam.sending_email import Sending

def test_send_email():
    sending = Sending()
    assert sending is not None