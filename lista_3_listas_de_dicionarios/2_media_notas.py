'''
Crie uma função chamada media_notas(alunos) que recebe uma lista de dicionários e calcula a média das notas de todos os alunos.
Exemplo de Entrada e Saída:
Entrada:
alunos = [
	{"nome": "Ana", "idade": 20, "nota": 8.5},
	{"nome": "Bruno", "idade": 22, "nota": 7.3},
	{"nome": "Carla", "idade": 21, "nota": 9.1}
]
media_notas(alunos)
Saída:
8.3

'''

def testar_media_notas():
    alunos = [
        {"nome": "Ana", "idade": 20, "nota": 8.5},
        {"nome": "Bruno", "idade": 22, "nota": 7.3},
        {"nome": "Carla", "idade": 21, "nota": 9.1}
    ]
    assert abs(media_notas(alunos) - 8.3) < 0.01
    assert media_notas([]) == 0  # Caso lista vazia

testar_media_notas()
print("Todos os testes passaram")
