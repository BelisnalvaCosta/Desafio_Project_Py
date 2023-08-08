"""
Desafio - Sistema Bancário - DIO
"""

# Dicionário do MENU
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
====> Digite sua opção: """

# Declaração das variáveis e constantes
saldo = 2500
limite = 800
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3
contador_saque = 0
saques_acumulados = 0
contador_deposito = 0
depositos_acumulados = 0

while True:  # Laço infinito

    opcao = input(menu)  # Faz a leitura do comando de entrada

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que você deseja depositar?: "))
        if (deposito > 0):  # Verificar se o valor a ser depositado é positivo
            saldo = saldo + deposito
            contador_deposito += 1
            depositos_acumulados = depositos_acumulados + deposito
            extrato = extrato + f"\nDepósito nº{contador_deposito}: + R$ {deposito:.2f}"  # f Faz a adição da string ao texto que irá aparecer no extrato
        else:  # Se o valor a ser depositado for negativo
            print("Valor de saque inválido. Tente novamente!")


    elif opcao == "s":
        print("Saque")
        saque = float((input("Quanto você deseja sacar?: ")))

        if (saldo < saque):  # Verificar se há saldo
            print("Saldo insuficiente!")
        elif (saldo > saque):  # Se tiver saldo, continue
            contador_saque += 1  # Contador de saque. O limite é de 3 saques no máximo
            if (saque > limite):  # Se o saque for acima do limite diário de R$800,00
                print(f"Saque acima de R$ {limite:.2f} não permitido")
            elif (saque < limite):  # Se for menor que o limite diário, continue
                if (contador_saque > numero_saques):  # Verifica se atingiu a quantidade máximo de saques diários.
                    print("\nExcedeu o limite de saques diário! Não é possível realizar mais de 3 saques ao dia!")
                else:
                    print("\nSaque realizado com sucesso!")
                    saques_acumulados = saques_acumulados + saque
                    extrato = extrato + f"\nSaque nº{contador_saque}: - R$ {saque:.2f}"  # Faz a adição da string ao texto que irá aparecer no extrato
                    saldo = saldo - saque


    elif opcao == "e":
        print("*************** Extrato ***************")  # Exibe o extrato completo com os saques e depósitos.
        extrato = extrato + f"""\n 
\n Valor total de saques:    - R$ {saques_acumulados:.2f}
\n Valor total de depositos: + R$ {depositos_acumulados:.2f}
\n ______________________________________________________    

   Seu saldo é de:             R$ {saldo:6.2f}"""

        print(extrato)


    elif opcao == "q":
        print("\n\nEncerrando...\n O Banco " " agradece a sua preferência!\n\n")
        break
    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada")
