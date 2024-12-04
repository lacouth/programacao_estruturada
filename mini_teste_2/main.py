import pickle
import os

ARQUIVO_ESTOQUE = 'estoque.pkl'

def carregar_estoque():
    """Carrega o estoque de um arquivo usando pickle"""
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'rb') as f:
            return pickle.load(f)
    return []

def salvar_estoque(estoque):
    """Salva o estoque em um arquivo usando pickle"""
    with open(ARQUIVO_ESTOQUE, 'wb') as f:
        pickle.dump(estoque, f)

def exibir_menu():
    """Exibe o menu principal"""
    print('''
    Controle de Estoque - Loja de Jogos
    1. Exibir Estoque
    2. Adicionar Jogo
    3. Atualizar Quantidade
    4. Planejar Reabastecimento
    5. Mostrar Jogos com Preços Menores
    6. Sair
    ''')

# Função a ser implementada
def exibir_estoque(estoque):
    """
    Exibe o estoque atual, mostrando o nome de cada jogo, quantidade e preço.
    Caso o estoque esteja vazio, exiba 'Estoque vazio'.
    """
    pass  #retirar quando completar a função


# Função a ser implementada
def adicionar_jogo(estoque, nome, quantidade, preco):
    """
    Adiciona um novo jogo ao estoque.
    Caso o jogo já exista, exibe 'Jogo já cadastrado'.
    """
    pass  #retirar quando completar a função


def atualizar_quantidade(estoque, nome, quantidade):
    """
    Atualiza a quantidade de um jogo no estoque.
    Se o jogo não estiver no estoque, exibe 'Jogo não encontrado'.
    """
    for jogo in estoque:
        if jogo["nome"].lower() == nome.lower():
            jogo["quantidade"] += quantidade
            print(f'Quantidade de {nome} atualizada para {jogo["quantidade"]}')
            return
    print("Jogo não encontrado")

def planejar_reabastecimento(estoque):
    """
    Mostra os jogos que possuem menos de 10 unidades e a quantidade necessária
    para atingir 10 unidades.
    """
    print("Jogos que precisam de reabastecimento:")
    for jogo in estoque:
        if jogo["quantidade"] < 10:
            faltam = 10 - jogo["quantidade"]
            print(f'{jogo["nome"]}: Faltam {faltam} unidades para atingir 10')

# Função a ser implementada
def mostrar_jogos_com_precos_menores(estoque, valor):
    """
    Mostra todos os jogos com preços menores que o valor informado.
    Caso nenhum jogo atenda ao critério, exibe 'Nenhum jogo encontrado com preço menor que o valor informado.'
    """
    pass  #retirar quando completar a função


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sistema():
    """Função principal do sistema"""
    estoque = carregar_estoque()
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            exibir_estoque(estoque)
        elif opcao == '2':
            nome = input("Nome do jogo: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço do jogo: "))
            adicionar_jogo(estoque, nome, quantidade, preco)
        elif opcao == '3':
            nome = input("Nome do jogo: ")
            quantidade = int(input("Quantidade a adicionar: "))
            atualizar_quantidade(estoque, nome, quantidade)
        elif opcao == '4':
            planejar_reabastecimento(estoque)
        elif opcao == '5':
            valor = float(input("Informe o valor limite: "))
            mostrar_jogos_com_precos_menores(estoque, valor)
        elif opcao == '6':
            salvar_estoque(estoque)
            print("Estoque salvo. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input('pressione ENTER para continuar...')

# Inicia o sistema
sistema()
