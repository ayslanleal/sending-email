from sending.spam import Sending

def test_send_email():
    sending = Sending()
    assert sending is not None