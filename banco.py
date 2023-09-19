class criar_conta:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

#################################################################################
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')

    def verificar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

##################################################################################
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

def main():
    contas = []

    while True:
        print('\nMenu:')
        print('1. Criar conta')
        print('2. Acessar conta')
        print('3. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do titular da conta: ')
            saldo_inicial = float(input('Digite o saldo inicial: '))
            conta = criar_conta(nome, saldo_inicial)
            contas.append(conta)
            print('Conta criada com sucesso.')

        elif opcao == '2':
            if not contas:
                print('Nenhuma conta disponível.')
                continue

            print('Contas disponíveis:')
            for i, conta in enumerate(contas):
                print(f'{i + 1}. {conta.nome}')

            escolha = int(input('Escolha o número da conta: ')) - 1

            if 0 <= escolha < len(contas):
                conta_atual = contas[escolha]
                while True:
                    print(f'\nMenu da conta de {conta_atual.nome}:')
                    print('1. Depositar')
                    print('2. Sacar')
                    print('3. Verificar saldo')
                    print('4. Voltar')

                    opcao_conta = input('Escolha uma opção: ')

                    if opcao_conta == '1':
                        valor = float(input('Digite o valor para depósito: '))
                        conta_atual.depositar(valor)
                    elif opcao_conta == '2':
                        valor = float(input('Digite o valor para saque: '))
                        conta_atual.sacar(valor)
                    elif opcao_conta == '3':
                        conta_atual.verificar_saldo()
                    elif opcao_conta == '4':
                        break
                    else:
                        print('Opção inválida.')

            else:
                print('Escolha inválida.')

        elif opcao == '3':
            print('Saindo do sistema.')
            break

        else:
            print('Opção inválida.')


if __name__ == '__main__':
    main()