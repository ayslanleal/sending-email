import imp
from sending.spam import Connect, Session

class User:
    def __init__(self, name):
        self.name = name
        self.id = None


def test_save_user():
    conection = Connect()
    session = conection.init_session()
    user =  User(name='Ney')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    conection.close()

"""
def test_show_users():
    conection = Connect()
    session = conection.init_session()
    users = [User(name="David"), User(name="Leal")]
    for user in users:
        session.save(user)

    assert users == session.show()
    session.roll_back()
    session.close()
    conection.close()

"""




