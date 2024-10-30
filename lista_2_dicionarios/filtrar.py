'''
Crie uma função chamada filtrar_por_valor_minimo(dados, valor_minimo), que recebe 
um dicionário onde as chaves representam identificadores de itens e os valores 
são quantidades inteiras. 

A função deve retornar um novo dicionário contendo apenas os itens com valores 
maiores ou iguais ao valor mínimo especificado.

Exemplo de Entrada e Saída:

    Entrada: {"item1": 10, "item2": 3, "item3": 15}, 5
    Saída: {"item1": 10, "item3": 15}

'''

def testar_filtrar_por_valor_minimo():
    assert filtrar_por_valor_minimo({"item1": 10, "item2": 3, "item3": 15}, 5) == {"item1": 10, "item3": 15}
    assert filtrar_por_valor_minimo({"a": 1, "b": 7, "c": 10}, 8) == {"c": 10}
    assert filtrar_por_valor_minimo({"x": 2, "y": 4}, 5) == {}
    

testar_filtrar_por_valor_minimo()
print("Todos os testes passaram")