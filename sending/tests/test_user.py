import pytest
from sending.spam import User




def test_save_user(session):
    user =  User(name='Ney')
    session.save(user)
    assert isinstance(user.id, int)


def test_show_users(connect,session):
    users = [User(name="David"), User(name="Leal")]
    for user in users:
        session.save(user)

    assert users == session.show()






