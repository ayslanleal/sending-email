
class Sending:

    def __init__(self):
        self.qtd_sending_email = 0

    def send(self,sender,to,title,body):
        if '@' not in to:
            raise InvalidEmail("Email inválido")
        self.qtd_sending_email += 1
        return to

class InvalidEmail(Exception):
    pass

