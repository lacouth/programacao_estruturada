'''
Crie uma função chamada alunos_aprovados(alunos) que recebe uma lista de dicionários e retorna apenas os alunos com nota maior ou igual a 7.
Exemplo de Entrada e Saída:
Entrada:
alunos = [ 
{"nome": "Ana", "idade": 20, "nota": 8.5}, 
{"nome": "Bruno", "idade": 22, "nota": 6.9} 
]
alunos_aprovados(alunos)
Saída:
[{"nome": "Ana", "idade": 20, "nota": 8.5}]
'''

def testar_alunos_aprovados():
    alunos = [
        {"nome": "Ana", "idade": 20, "nota": 8.5},
        {"nome": "Bruno", "idade": 22, "nota": 6.9}
    ]
    assert alunos_aprovados(alunos) == [{"nome": "Ana", "idade": 20, "nota": 8.5}]
    assert alunos_aprovados([]) == []  # Caso lista vazia
    
testar_alunos_aprovados()
print("Todos os testes passaram")
