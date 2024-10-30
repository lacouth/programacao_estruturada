'''
Crie uma função chamada contar_letras(texto: str) -> dict que recebe uma string 
e retorna um dicionário em que as chaves são as letras da string, 
e os valores são o número de vezes que cada letra aparece. 
A função deve ignorar espaços e diferenciar maiúsculas de minúsculas.

Exemplo de Entrada e Saída:

    Entrada: "programacao"
    Saída: {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 3, 'm': 1, 'c': 1}

'''

def testar_contar_letras():
    assert contar_letras("programacao") == {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 3, 'm': 1, 'c': 1}
    assert contar_letras("banana") == {'b': 1, 'a': 3, 'n': 2}
    assert contar_letras("") == {}
    assert contar_letras("A aa B") == {'A': 1, 'a': 2, 'B': 1}
    print("Todos os testes passaram")

testar_contar_letras()
