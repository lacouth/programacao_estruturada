'''
Escreva uma função chamada divisao que receba dois números como parâmetros e 
retorne o resultado da divisão do primeiro pelo segundo. A função deve tratar 
o caso em que o divisor seja zero, retornando uma mensagem de erro 
"Divisão por zero não permitida.".

'''

def test_divisao():
    # Testando com divisões comuns
    assert divisao(10, 2) == 5.0
    assert divisao(9, 3) == 3.0
    assert divisao(100, 25) == 4.0
    
    # Testando com divisor zero
    assert divisao(7, 0) == "Divisão por zero não permitida."
    assert divisao(0, 0) == "Divisão por zero não permitida."
    
    # Testando com números negativos
    assert divisao(-10, 2) == -5.0
    assert divisao(10, -2) == -5.0
    assert divisao(-10, -2) == 5.0
    
    # Testando com números decimais
    assert divisao(7.5, 2.5) == 3.0
    assert divisao(-7.5, 2.5) == -3.0
    
# Chamada de execução dos testes
test_divisao()
print("Todos os testes passaram.")
