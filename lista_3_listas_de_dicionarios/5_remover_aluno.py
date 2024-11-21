'''
Crie uma função chamada remover_aluno(alunos, nome) que recebe uma lista de dicionários e remove o aluno pelo nome, se ele existir.
Exemplo de Entrada e Saída:
Entrada:
alunos = [ 
{"nome": "Ana", "idade": 20, "nota": 8.5},
 {"nome": "Bruno", "idade": 22, "nota": 7.3} 
] 
remover_aluno(alunos, "Ana")
Saída:
[{"nome": "Bruno", "idade": 22, "nota": 7.3}]

'''

def testar_remover_aluno():
    alunos = [
        {"nome": "Ana", "idade": 20, "nota": 8.5},
        {"nome": "Bruno", "idade": 22, "nota": 7.3}
    ]
    remover_aluno(alunos, "Ana")
    assert alunos == [{"nome": "Bruno", "idade": 22, "nota": 7.3}]
    remover_aluno(alunos, "Carlos")  # Nome não encontrado, lista não muda
    assert alunos == [{"nome": "Bruno", "idade": 22, "nota": 7.3}]
    
testar_remover_aluno()
print("Todos os testes passaram")
