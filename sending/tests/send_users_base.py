from unicodedata import name
import pytest
from sending.spam.sending_email import Sending
from sending.spam.main import SendingSpam
from sending.spam.sending_email import User

class MockSend(Sending):
    def __init__(self):
        super().__init__()
        self.qtd_sending_email = 0
        self.param_send = None

    def send(self, sender, to, title, body):
        self.param_send = (sender, to, title, body)
        self.qtd_sending_email += 1

@pytest.mark.parametrize(
    'users', [
        [
            User(name="David", email="davidayslan10@outlook.com"),
            User(name="Leal", email="davidleal@gmail.com")
        ],
        [
            User(name="Leal", email="davidleal@gmail.com")
        ]
    ]
)
def test_send_span(session, users):
    for user in users:
        session.save(user)
    sending = Sending()
    sending_spam = SendingSpam(session, sending)
    sending_spam.send_emails(
        'foobar@gmail.com',
        'Notas fiscas',
        'Lista de notas'
    )

    assert len(users) == sending.qtd_sending_email()

def test_param_span(session, users):
    user = User(name="David", email="davidayslan10@outlook.com")
    session.save(user)
    sending = Sending()
    sending_spam = SendingSpam(session, sending)
    sending_spam.send_emails(
        'foobar@gmail.com',
        'foobar@gmail.com'
        'Notas fiscas',
        'Lista de notas'
    )

    assert sending.param_send == ('foobar@gmail.com','Notas fiscas','Lista de notas')