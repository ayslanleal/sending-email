import pytest
from sending.spam import Sending, InvalidEmail

def test_create_send():
    sending = Sending()
    assert sending is not None


@pytest.mark.parametrize('receive', ["luciano@gmail.com","ayskanleal15@gmail.com"] )
def test_remetente(receive):
    sending = Sending()
    resultado = sending.send(
        "neymarjr@gmail.com",
        receive,
        "Notas fiscais",
        "Notas fiscais das compras a pgar",
    )

    assert receive in resultado

@pytest.mark.parametrize('receive', ["","ayskanleal15gmail.com"] )
def test_remetente_invalid(receive):
    sending = Sending()
    with pytest.raises(InvalidEmail):
        sending.send(
            "neymarjr@gmail.com",
            receive,
            "Notas fiscais",
            "Notas fiscais das compras a pgar",
        )