'''
Crie uma função chamada atualizar_precos(precos, aumento) 
que recebe um dicionário onde as chaves são nomes de produtos
 e os valores são seus preços. 
 
 A função deve retornar um novo dicionário com os preços atualizados, 
 aplicando um aumento percentual especificado pelo usuário.

Exemplo de Entrada e Saída:

    Entrada: {"banana": 2.0, "maçã": 3.0}, 10
    Saída: {"banana": 2.2, "maçã": 3.3}
'''

def testar_atualizar_precos():
    assert atualizar_precos({"banana": 2.0, "maçã": 3.0}, 10) == {"banana": 2.2, "maçã": 3.3}
    assert atualizar_precos({"uva": 4.0, "laranja": 5.0}, 50) == {"uva": 6.0, "laranja": 7.5}
    assert atualizar_precos({}, 10) == {}
    

testar_atualizar_precos()
print("Todos os testes passaram")