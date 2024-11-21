'''
Crie uma função chamada adicionar_aluno(alunos, nome, idade, nota) que recebe uma lista de dicionários e adiciona um novo aluno com os dados fornecidos à lista.
Exemplo de Entrada e Saída:
Entrada:
alunos = [] 
adicionar_aluno(alunos, "Diego", 23, 8.0)
Saída:
[{"nome": "Diego", "idade": 23, "nota": 8.0}]

'''


def testar_adicionar_aluno():
    alunos = []
    adicionar_aluno(alunos, "Diego", 23, 8.0)
    assert alunos == [{"nome": "Diego", "idade": 23, "nota": 8.0}]
    adicionar_aluno(alunos, "Ana", 21, 9.0)
    assert alunos == [
        {"nome": "Diego", "idade": 23, "nota": 8.0},
        {"nome": "Ana", "idade": 21, "nota": 9.0}
    ]
    
testar_adicionar_aluno()
print("Todos os testes passaram")
