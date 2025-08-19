import pytest
from juros_composto import calcular_juros_compostos

@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada",
                         [
                             (1000, 20, 1, (200, 1200)),                
                             (2000, 40, 2, (3600, 5600))                                         
                                            
                         ]
                    )

def test_verificar_juros_compostos(capital, juros, tempo, situacao_esperada):

    resultado = calcular_juros_compostos(capital, juros, tempo)

    assert resultado == situacao_esperada

