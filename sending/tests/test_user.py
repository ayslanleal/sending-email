class Session:
    cont = 0
    users= []

    def save(self, user):
        Session.cont += 1
        user.id = Session.cont
        self.users.append(user)
    
    def show(self):
        return self.users

    def close(self):
        pass

    def roll_back(self):
        pass
    
    

class Connect:
    def init_session(self):
        return Session()

    def close(self):
        pass


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




