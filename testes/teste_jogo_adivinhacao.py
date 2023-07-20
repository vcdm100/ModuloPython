from POO2_Jogo_da_Adivinhacao import Adivinhacao;
import pytest;

@pytest.fixture
def jogo():
    return Adivinhacao(1,100,3);

def test_constructor(jogo):
    assert jogo.limite_inferior == 1;
    assert jogo.limite_superior == 100;
    assert jogo.max_tentativas == 3;

""" RESULTADO (TERMINAL) - TESTE:

pytest teste_jogo_adivinhacao.py

======================================================================================= test session starts ========================================================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir:
collected 1 item

teste_jogo_adivinhacao.py .                                                                                                                                                                   [100%]

======================================================================================== 1 passed in 0.01s =========================================================================================

"""