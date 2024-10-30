'''

Crie uma função chamada combinar_estoque(estoque1: dict, estoque2: dict) -> dict 
que recebe dois dicionários onde as chaves são nomes de produtos e os valores são 
as quantidades em estoque. 

A função deve retornar um novo dicionário com a soma das quantidades de produtos 
que estão em ambos os dicionários. Produtos presentes apenas em um dos dicionários 
devem ser incluídos com suas respectivas quantidades.

Exemplo de Entrada e Saída:

    Entrada: {"caneta": 10, "lápis": 5}, {"caneta": 7, "borracha": 3}
    Saída: {"caneta": 17, "lápis": 5, "borracha": 3}

'''

def testar_combinar_estoque():
    assert combinar_estoque({"caneta": 10, "lápis": 5}, {"caneta": 7, "borracha": 3}) == {"caneta": 17, "lápis": 5, "borracha": 3}
    assert combinar_estoque({"borracha": 2}, {"borracha": 3, "régua": 5}) == {"borracha": 5, "régua": 5}
    assert combinar_estoque({}, {"tesoura": 7}) == {"tesoura": 7}
    print("Todos os testes passaram")

testar_combinar_estoque()