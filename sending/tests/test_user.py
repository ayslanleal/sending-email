import email
import pytest
from sending.spam import User



def test_save_user(session):
    user =  User(name='Ney', email="neymarjr@gmail.com")
    session.save(user)
    assert isinstance(user.id, int)


def test_show_users(session):
    users = [User(name="David", email="davidayslan10@outlook.com"), User(name="Leal", email="davidleal@gmail.com")]
    for user in users:
        session.save(user)

    assert users == session.show()






