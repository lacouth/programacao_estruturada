'''
Uma função que conta o número de palavras em uma string. 
Por exemplo, contar_palavras(texto) que retorna o número de palavras no texto.  

'''

def test_contar_palavras():
    # Testando com uma string comum
    assert contar_palavras("Olá, mundo!") == 2
    assert contar_palavras("Isso é um teste.") == 4
    
    # Testando com múltiplos espaços
    assert contar_palavras("  Isso é um   teste.  ") == 4
    assert contar_palavras("   Muitos   espaços    entre palavras   ") == 4
    
    # Testando com string vazia
    assert contar_palavras("") == 0
    assert contar_palavras("   ") == 0  # Apenas espaços
    
    # Testando com uma única palavra
    assert contar_palavras("Palavra") == 1
    assert contar_palavras("    Palavra   ") == 1

# Executando os testes
test_contar_palavras()
print("Todos os testes para 'contar_palavras' passaram.")
