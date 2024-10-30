'''
Crie uma função chamada inverter_dicionario(dicionario), que recebe um dicionário 
onde os valores são únicos e retorna um novo dicionário em que as chaves e os 
valores foram trocados. 

Isso significa que cada valor original se torna uma chave, e cada chave original 
se torna um valor no novo dicionário.

Exemplo de Entrada e Saída:

    Entrada: {"a": 1, "b": 2, "c": 3}
    Saída: {1: "a", 2: "b", 3: "c"}

'''

def testar_inverter_dicionario():
    assert inverter_dicionario({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
    assert inverter_dicionario({"gato": "animal", "rosa": "flor"}) == {"animal": "gato", "flor": "rosa"}
    assert inverter_dicionario({}) == {}
    

testar_inverter_dicionario()
print("Todos os testes passaram")