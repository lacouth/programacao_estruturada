def filtrar_chaves_por_valor(dicionario, limite):
    pass

# Testes
assert filtrar_chaves_por_valor({"a": 10, "b": 5, "c": 15, "d": 3}, 10) == ["a", "c"]
assert filtrar_chaves_por_valor({"x": 8, "y": 12, "z": 7}, 9) == ["y"]
assert filtrar_chaves_por_valor({}, 5) == []
assert filtrar_chaves_por_valor({"p": 3, "q": 4, "r": 5}, 6) == []
print("Todos os testes da Questão 4 passaram!")
