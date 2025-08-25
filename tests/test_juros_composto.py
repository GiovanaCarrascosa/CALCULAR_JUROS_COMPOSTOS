import pytest
from juros_composto import calcular_juros_compostos

# caso o valor da capital seja menor que 0 
def test_verificar_capital_menor_que_zero():

    #definindo a entrada
    capital = -15
    taxa_juros = 5
    tempo = 2
    
    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor da taxa seja menor que 0 
def test_verificar_taxa_de_juros_menor_que_zero():

    #definindo a entrada
    capital = 15
    taxa_juros = -5
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor do tempo seja menor que 0 
def test_verificar_tempo_menor_que_zero():

    #definindo a entrada
    capital = 15
    taxa_juros = 5
    tempo = -2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O tempo não pode ser negativo."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

####################################################################################################################

# caso o valor da capital nao seja um int ou float
def test_verificar_se_o_valor_da_capital_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = "ola"
    taxa_juros = 2
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match=r"O capital investido deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor da taxa nao seja um int ou float
def test_verificar_se_o_valor_da_taxa_de_juros_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = 15
    taxa_juros = "ola"
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = r"A taxa de juros deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor do tempo nao seja um int ou float
def test_verificar_se_o_valor_do_tempo_for_uma_string_ao_inves_de_int_ou_float():

    #definindo a entrada
    capital = 15
    taxa_juros = 2
    tempo = "ola"

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = r"O tempo deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, taxa_juros, tempo)

####################################################################################################################

# caso o valor da capital seja = 0
def test_verificar_se_o_valor_da_capital_for_igual_a_zero():

    #definindo a entrada
    capital = 0
    taxa_juros = 2
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser =  0"):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor da taxa de juros seja = 0
def test_verificar_se_o_valor_da_taxa_juros_for_igual_a_zero():

    #definindo a entrada
    capital = 1000
    taxa_juros = 0
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "A taxa de juros não pode ser =  0"):
        calcular_juros_compostos(capital, taxa_juros, tempo)

# caso o valor do tempo seja = 0
def test_verificar_se_o_valor_do_tempo_for_igual_a_zero():

    #definindo a entrada
    capital = 2000
    taxa_juros = 2
    tempo = 0

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O tempo não pode ser =  0"):
        calcular_juros_compostos(capital, taxa_juros, tempo)

####################################################################################################################

# caso o valor da capital nao tenha sido informado
def test_verificar_se_o_valor_da_capital__nao_foi_preenchida():

    #definindo a entrada
    taxa_juros = 2
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser =  0"):
        calcular_juros_compostos(taxa_juros, tempo)

# caso o valor da taxa nao tenha sido informado
def test_verificar_se_o_valor_da_taxa_juros_nao_foi_preenchida():

    #definindo a entrada
    capital = 20000
    tempo = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser =  0"):
        calcular_juros_compostos(capital, tempo)

# caso o valor do tempo nao tenha sido informado
def test_verificar_se_o_valor_do_tempo_nao_foi_preenchido():

    #definindo a entrada
    capital = 2000
    taxa_juros = 2

    #executando a funcao e esperando erro
    with pytest.raises(ValueError, match = "O capital investido não pode ser =  0"):
        calcular_juros_compostos(capital, taxa_juros)