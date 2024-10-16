'''
Suponha que você seja um professor e queira calcular a média das notas de um aluno em uma lista. 
Escreva uma função chamada calcular_media que aceite uma lista de notas (números) e retorne a média.

'''

def test_calcular_media():
    # Testando com várias notas
    assert calcular_media([10, 8, 9]) == 9.0
    assert calcular_media([7, 7, 7, 7]) == 7.0
    assert calcular_media([9.5, 8.5, 7.0]) == 8.333333333333334
    
    # Testando com lista vazia
    assert calcular_media([]) == 0
    
    # Testando com uma única nota
    assert calcular_media([5]) == 5.0
    assert calcular_media([10]) == 10.0

# Executando os testes
test_calcular_media()
print("Todos os testes para 'calcular_media' passaram.")
