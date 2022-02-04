"""import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
"""


import pytest
from sending.spam import Sending

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