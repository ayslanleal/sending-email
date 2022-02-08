import pytest
from sending.spam import Connect, Session, User

@pytest.fixture(scope='session')
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