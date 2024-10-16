'''
Crie uma função que recebe dois números e retorna a soma deles. 
Por exemplo, soma(a, b) que retorna a soma de a e b.

'''

def test_soma():
    # Testando com números inteiros positivos
    assert soma(3, 5) == 8
    assert soma(0, 0) == 0
    assert soma(100, 200) == 300
    
    # Testando com números negativos
    assert soma(-3, -5) == -8
    assert soma(-10, 5) == -5
    assert soma(7, -2) == 5
    
    # Testando com números decimais
    assert soma(1.5, 2.5) == 4.0
    assert soma(-1.5, -2.5) == -4.0
    assert soma(10.5, -5.5) == 5.0
    
    # Testando com números mistos
    assert soma(5, 3.5) == 8.5
    assert soma(-5, 2.5) == -2.5

# Chamada de execução dos testes
test_soma()
print("Todos os testes passaram.")
