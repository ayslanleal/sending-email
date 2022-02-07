import imp
from pickletools import pyset

import pytest
from sending.spam import Connect, Session, User


@pytest.fixture
def connect():
    connect_obj = Connect()
    yield connect_obj
    connect_obj.close()

@pytest.fixture
def session(connect):
    session_init = connect.init_session()
    yield session_init
    session_init.close()
    session_init.roll_back()

def test_save_user(session):
    user =  User(name='Ney')
    session.save(user)
    assert isinstance(user.id, int)


def test_show_users(connect,session):
    users = [User(name="David"), User(name="Leal")]
    for user in users:
        session.save(user)

    assert users == session.show()






