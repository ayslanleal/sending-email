from unicodedata import name
import pytest
from sending.spam.sending_email import Sending
from sending.spam.main import SendingSpam
from sending.spam.sending_email import User

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