'''
Uma função que converte a temperatura de Celsius para Fahrenheit e vice-versa. Por exemplo, celsius_para_fahrenheit(c) e fahrenheit_para_celsius(f).
De Celsius para Fahrenheit: F = C × 9/5 + 32
De Fahrenheit para Celsius: C = ( F − 32 ) × 5 / 9

'''

def test_celsius_para_fahrenheit():
    # Testando conversões comuns
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40
    assert celsius_para_fahrenheit(37) == 98.6
    
    # Testando conversões decimais
    assert celsius_para_fahrenheit(25.5) == 77.9
    assert abs(celsius_para_fahrenheit(-17.8) + 0.04) < 0.01

def test_fahrenheit_para_celsius():
    # Testando conversões comuns
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(-40) == -40
    assert fahrenheit_para_celsius(98.6) == 37
    
    # Testando conversões decimais
    assert abs(fahrenheit_para_celsius(77.9) - 25.5) < 0.01
    assert fahrenheit_para_celsius(0) == -17.77777777777778

# Executando os testes
test_celsius_para_fahrenheit()
print("Todos os testes para 'celsius_para_fahrenheit' passaram.")

test_fahrenheit_para_celsius()
print("Todos os testes para 'fahrenheit_para_celsius' passaram.")
