'''
Você está criando uma aplicação de previsão do tempo. 
Dada uma lista de temperaturas dos últimos 7 dias, escreva uma função chamada previsao_tempo que 
aceite esta lista e retorne "Quente" se a média for maior que 25 graus, 
"Frio" se for menor que 15 graus e "Agradável" caso contrário.

'''


# Testes unitários para a função previsao_tempo
def test_previsao_tempo():
    # Testando com temperaturas altas (Quente)
    assert previsao_tempo([30, 32, 29, 28, 31, 33, 30]) == "Quente"
    
    # Testando com temperaturas baixas (Frio)
    assert previsao_tempo([10, 12, 14, 13, 11, 12, 10]) == "Frio"
    
    # Testando com temperaturas médias (Agradável)
    assert previsao_tempo([20, 22, 24, 23, 21, 22, 20]) == "Agradável"
    
    # Testando com temperaturas exatamente no limite (Agradável)
    assert previsao_tempo([15, 16, 17, 14, 15, 15, 16]) == "Agradável"
    assert previsao_tempo([25, 24, 26, 25, 24, 25, 24]) == "Agradável"

# Executando os testes
test_previsao_tempo()
print("Todos os testes para 'previsao_tempo' passaram.")
