'''
Crie uma função chamada combinar_dicionarios(d1, d2), que recebe dois dicionários 
onde as chaves são nomes de produtos e os valores são as quantidades de cada produto 
em estoque. 

A função deve combinar esses dicionários em um novo dicionário único, 
somando as quantidades para produtos com o mesmo nome.

Exemplo de Entrada e Saída:

    Entrada: {"banana": 10, "maçã": 5}, {"banana": 3, "laranja": 8}
    Saída: {"banana": 13, "maçã": 5, "laranja": 8}

'''

def testar_combinar_dicionarios():
    assert combinar_dicionarios({"banana": 10, "maçã": 5}, {"banana": 3, "laranja": 8}) == {"banana": 13, "maçã": 5, "laranja": 8}
    assert combinar_dicionarios({"item1": 2}, {"item1": 3, "item2": 5}) == {"item1": 5, "item2": 5}
    assert combinar_dicionarios({}, {"produto": 7}) == {"produto": 7}
    

testar_combinar_dicionarios()
print("Todos os testes passaram")