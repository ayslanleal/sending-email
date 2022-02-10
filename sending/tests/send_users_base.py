from unicodedata import name
import pytest
from sending.spam.sending_email import Sending
from sending.spam.main import SendingSpam
from sending.spam.sending_email import User
from unittest.mock import Mock

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
    sending = Mock()
    sending_spam = SendingSpam(session, sending)
    sending_spam.send_emails(
        'foobar@gmail.com',
        'Notas fiscas',
        'Lista de notas'
    )

    assert len(users) == sending.send.call_count

def test_param_span(session, users):
    user = User(name="David", email="davidayslan10@outlook.com")
    session.save(user)
    sending = Mock()
    sending_spam = SendingSpam(session, sending)
    sending_spam.send_emails(
        'foobar@gmail.com',
        'foobar@gmail.com'
        'Notas fiscas',
        'Lista de notas'
    )

    sending.param_send.assert_called_once_with('foobar@gmail.com','Notas fiscas','Lista de notas')