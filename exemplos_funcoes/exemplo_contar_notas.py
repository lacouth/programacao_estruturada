'''
Escreva uma função chamada contar_notas_acima_de_70 que receba uma lista de notas (números) 
e retorne quantas dessas notas são maiores que 70. A função deve contar apenas as notas que 
são estritamente maiores que 70, ou seja, notas iguais a 70 não devem ser contadas.

'''

def test_contar_notas_acima_de_70():
    assert contar_notas_acima_de_70([80, 65, 90, 70, 75]) == 3
    assert contar_notas_acima_de_70([60, 55, 45]) == 0
    assert contar_notas_acima_de_70([71, 72, 70, 69]) == 2
    assert contar_notas_acima_de_70([70, 70, 70]) == 0  # Nenhuma nota é estritamente maior que 70

# Executando os testes
test_contar_notas_acima_de_70()
print("Todos os testes passaram.")
