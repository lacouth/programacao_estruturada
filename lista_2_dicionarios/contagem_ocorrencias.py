'''
Crie uma função chamada contar_ocorrencias(palavras), que recebe uma lista de palavras 
e retorna um dicionário em que as chaves são as palavras da lista, 
e os valores representam o número de vezes que cada palavra aparece. 

A função deve ser capaz de contar tanto palavras repetidas quanto palavras únicas.

Exemplo de Entrada e Saída:

    Entrada: ["gato", "cachorro", "gato", "pássaro"]
    Saída: {"gato": 2, "cachorro": 1, "pássaro": 1}
'''

def testar_contar_ocorrencias():
    assert contar_ocorrencias(["gato", "cachorro", "gato", "pássaro"]) == {"gato": 2, "cachorro": 1, "pássaro": 1}
    assert contar_ocorrencias(["a", "b", "a", "a", "b"]) == {"a": 3, "b": 2}
    assert contar_ocorrencias([]) == {}
    

testar_contar_ocorrencias()
print("Todos os testes passaram")