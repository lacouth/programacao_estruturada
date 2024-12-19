def media_acima_de(alunos, nota_minima):
   pass # retirar ao resolver a questão

# Testes
alunos = [{"nome": "Ana", "nota": 8.5}, {"nome": "Bruno", "nota": 7.3}, {"nome": "Carla", "nota": 9.1}]
assert media_acima_de(alunos, 8) == ["Ana", "Carla"]
assert media_acima_de(alunos, 9) == ["Carla"]
assert media_acima_de(alunos, 10) == []
print("Todos os testes da Questão 3 passaram!")
