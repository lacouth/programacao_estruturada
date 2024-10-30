'''
Crie uma função chamada maiores_de_idade(idades: dict) -> dict que recebe um dicionário
onde as chaves são os nomes das pessoas e os valores são suas idades. 

A função deve retornar um novo dicionário contendo apenas as pessoas com idade maior ou igual a 18 anos.

Exemplo de Entrada e Saída:

    Entrada: {"Ana": 20, "João": 16, "Carlos": 25}
    Saída: {"Ana": 20, "Carlos": 25}

'''

def testar_maiores_de_idade():
    assert maiores_de_idade({"Ana": 20, "João": 16, "Carlos": 25}) == {"Ana": 20, "Carlos": 25}
    assert maiores_de_idade({"Maria": 18, "José": 17}) == {"Maria": 18}
    assert maiores_de_idade({"João": 16, "Pedro": 14}) == {}
    print("Todos os testes passaram")

testar_maiores_de_idade()