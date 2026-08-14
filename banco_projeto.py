menu = ''''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITESAQUE = 3

while (True):

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito de {valor:.2f} realizado \n'
            print(f'Deposito de {valor} realizado com sucesso')

        else:
            print('Deposite um valor valido')

    elif opcao == 's':
        valor = float(input('Digite o valor a ser sacado: '))
        if valor > saldo:
            print('Saldo insuficiente')

        elif valor > limite:
            print(f'Valor de saque {valor}, e maior que o limite de {limite}')

        elif numero_de_saques >= LIMITESAQUE:
            print('Limite de saques atingido')

        elif valor > 0:
            saldo -= valor
            print(f'Saque de {valor} realizado com sucesso')
            extrato += f'Saque de {valor:.2f} realizado \n'
            numero_de_saques +=1

        else:
            print('Saque um valor valido')

    elif opcao == 'e':
        print(extrato)
        print(f'Saldo atual e de: {saldo}')

    elif opcao == 'q':
        print('Programa está se fechando')
        break

    else:
        print('Escolha uma opção valida')
