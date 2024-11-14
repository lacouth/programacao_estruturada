import os
estoque = {
    'Xadrez': 6,
    'Dominó': 12,
    'Uno': 3,
    'Pôquer': 8
}

def exibir_menu():
    print('\nMenu de Controle de Estoque')
    print('''
          1. Exibir Estoque
          2. Adicionar Novo Jogo
          3. Atualizar Quantidade de Jogo
          4. Planejar Reabastecimento
          5. Sair
          ''')

def exibir_estoque(estoque):
    '''Função para exibir o estoque atual'''
    pass #retirar quando completar a função

def adicionar_jogo(estoque, nome, quantidade):
    '''Função para adicionar um novo jogo ao estoque'''
    pass #retirar quando completar a função

def atualizar_quantidade(estoque, nome, quantidade):
    '''Função para atualizar a quantidade de um jogo existente'''
    if nome in estoque:
        estoque[nome] = quantidade
        print(f'A quantidade de {nome} foi atualizada para {quantidade}')
    else:
        print(f'O {nome} não foi encontrado no estoque')
    

def planejar_reabastecimento(estoque):
    '''Função para sugerir reabastecimento de jogos com menos de 10 unidades'''
    pass #retirar quando completar a função

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sistema():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            exibir_estoque(estoque)
        elif opcao == '2':
            nome = input('Nome do jogo: ')
            quantidade = int(input('Quantidade inicial: '))
            adicionar_jogo(estoque, nome, quantidade)
        elif opcao == '3':
            nome = input('Nome do jogo: ')
            quantidade = int(input('Nova quantidade: '))
            atualizar_quantidade(estoque, nome, quantidade)
        elif opcao == '4':
            planejar_reabastecimento(estoque)
        elif opcao == '5':
            print('Desligando...')
            break
        else:
            print('Opção inválida. Tente novamente.')
        input('Pressione ENTER para continuar...')

# Inicie o sistema
sistema()
