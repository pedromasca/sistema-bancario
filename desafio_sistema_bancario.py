#### Sistem Bancário ####

### Regras:

# 3 operações: Depósito / Saque /  Extrato

# Depósito - Deve ser possível depositar valores positivos,
# e o valor do depósito deve ser armazenado e exibido no extrato.

# Saque - O sistema deve permitir 3 saques diários de no máximo R$500 cada,
# caso o usuário não tenha o valor em conta, o sistema deve exibir uma
# mensagem informando que não será possível sacar por falta de saldo.
# Todos os saques devem ser armazenados e exibidos no extrato.

# Extrato - Deve listar todos os depósitos e saques, além do saldo em conta.
# Se estiver em branco, deve exibir mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos no formato R$xxxx.xx .

# Codado por Pedro Mascarenhas para o Desafio da DIO para a Jornada Python Developer.

import re
from datetime import datetime

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(
        input(
            "\nInforme uma opção: \n[1] Depósito \n[2] Saque \n[3] Extrato \n[0] Sair \n \n->:"
        )
    )

    if opcao == 1:
        valor = float(input("\nInforme a quantia para depósito: "))
        if valor >= 100:
            print("\nDepósito realizado!\n")
            saldo += valor
            extrato += f"Data: {datetime.now()} Depósito: R${valor:.2f} - Saldo: R${saldo:.2f}\n"

        else:
            print(
                "\nValor inválido, este caixa aceita apenas depósitos mínimos de R$100. Tente novamente!\n"
            )

    elif opcao == 2:
        valor = float(input("\nInforme a quantia para o saque: "))
        if 0 < valor <= limite and valor % 10 == 0:
            if valor <= saldo:
                saldo -= valor
                extrato += f"Data: {datetime.now()} Saque: R${valor:.2f} - Saldo: R${saldo:.2f}\n"
                if num_saques < LIMITE_SAQUES:
                    print("\nSaque realizado com sucesso!\n")
                num_saques += 1
                if num_saques >= LIMITE_SAQUES:
                    print("\nO número de tentativas de saques diários foi excedido, tente novamente amanhã ou ligue para a Central de Relacionamento no 4004-2020!")

            else:
                print("\nSaldo insuficiente!")
        else:
            print("\n Você só pode realizar saques de até R$500 por saque.")

    elif opcao == 3:
        if not extrato:
            print("\nNão foram realizadas movimentações.\n")
        else:
            print(f"\nExtrato: \n")
            extrato += f"Data: {datetime.now()} Saldo: R${saldo:.2f}\n"
            print(extrato)

    elif opcao == 0:
        print("\nSaindo do sistema...Tenha um bom dia!")
        break

    else:
        print("\nOpção inválida, tente novamente!\n")

        opcao2 = int(
            input(
                "\nGostaria de voltar ao menu anterior?\n Digite [1] para SIM e [2] para NAO: "
            )
        )
        if opcao2 == 1:
            print(opcao)
        elif opcao2 == 2:
            print("\nConsulta encerrada!\nTenha um bom dia!\n")
            break
