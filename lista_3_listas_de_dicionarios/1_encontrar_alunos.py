'''
Crie uma função chamada encontrar_aluno(alunos, nome) que recebe uma lista de dicionários onde cada dicionário representa um aluno (com nome, idade e nota) e uma string com o nome a ser procurado. A função deve retornar o dicionário do aluno correspondente ou None se não for encontrado.
Exemplo de Entrada e Saída:
Entrada:
alunos = [
	{"nome": "Ana", "idade": 20, "nota": 8.5},
	{"nome": "Bruno", "idade": 22, "nota": 7.3}
]
encontrar_aluno(alunos, "Ana")
Saída:
{"nome": "Ana", "idade": 20, "nota": 8.5}
'''

def testar_encontrar_aluno():
    alunos = [
        {"nome": "Ana", "idade": 20, "nota": 8.5},
        {"nome": "Bruno", "idade": 22, "nota": 7.3}
    ]
    assert encontrar_aluno(alunos, "Ana") == {"nome": "Ana", "idade": 20, "nota": 8.5}
    assert encontrar_aluno(alunos, "Carlos") is None
    assert encontrar_aluno([], "Ana") is None
    
testar_encontrar_aluno()
print("Todos os testes passaram")
