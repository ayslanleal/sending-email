
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
        self.users.clear()
    
    

class Connect:
    def init_session(self):
        return Session()

    def close(self):
        pass
