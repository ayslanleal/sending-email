
class Sending:
    def send(self,sender,to,title,body):
        if '@' not in to:
            raise InvalidEmail("Email inválido")
        return to

class InvalidEmail(Exception):
    pass

