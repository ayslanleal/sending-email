from sending.spam.sending_email import Sending
from sending.spam.main import SendingSpam


def test_send_span(session):
    sending_spam = SendingSpam(session, Sending())
    sending_spam.send_emails(
        'foobar@gmail.com',
        'Notas fiscas',
        'Lista de notas'
    )