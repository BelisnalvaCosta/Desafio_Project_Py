"""
Desafio - Sistema Bancário - DIO
Versão 2:
- Modularização
    - Utilização de funções
- Novas funcionalidades
"""

# Dicionário do MENU
menu = """
[d] Depositar
[s] Sacar
[n] Novo Usuário
[c] Nova Conta
[lc] Lista Contas
[e] Extrato
[q] Sair
====> Digite sua opção: """

# Declaração das variáveis e constantes
saldo = 2500
limite = 800
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contador_saque = 0
saques_acumulados = 0
contador_deposito = 0
depositos_acumulados = 0
lista_usuarios = []
nro_conta = 0
contas = []
AGENCIA = "0001"


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (saldo < valor):  # Verifica se existe saldo
        print("Saldo insuficiente!")
    elif (saldo > valor):  # Caso haja saldo, continue
        numero_saques += 1  # Contador de saque. O limite é de 3 saques
        if (valor > limite):  # Se o saque for acima do limite diário de R$800,00
            print(f"Saque acima de R$ {limite:.2f} não permitido")
        elif (valor < limite):  # Se for menor que o limite diário, continue
            if (numero_saques > limite_saques):  # Verifica se atingiu a quantidade máxima de saques diários.
                print("\nExcedeu o limite de saques diário! Não é possível realizar mais de 3 saques ao dia!")
            else:

                global saques_acumulados
                saques_acumulados += valor
                print(f"\nSaque de R${valor:.2f} realizado com sucesso!")
                extrato = extrato + f"\nSaque nº{numero_saques}: - R$ {valor:.2f}"  # Faz a adição da string ao texto que irá aparecer no extrato

                saldo = saldo - valor

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    saldo = saldo + valor
    global contador_deposito
    contador_deposito += 1
    extrato = extrato + f"\nDepósito nº{contador_deposito}: + R$ {valor:.2f}"  # Faz a adição da string ao texto que irá aparecer no extrato
    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato


def print_extrato(saldo, /, *, extrato):
    print("\n*************** Extrato ***************")  # Exibe o extrato completo com os saques e depósitos.
    extrato = extrato + f"""\n 
\n Valor total de saques:    - R$ {saques_acumulados:.2f}
\n Valor total de depositos: + R$ {depositos_acumulados:.2f}
\n __________________________________________________________        

   Seu saldo é de:             R$ {saldo:6.2f}"""

    print(extrato)
    return extrato


def criar_usuario(
        usuarios):  # Nome="",data_nascimento="DD/MM/AAAA",cpf=1234567890,endereco="logradouro, nro - bairro - cidade/sigla estado"
    # Data de nascimento no formato: DD/MM/AAAA
    # Endereço no formato: logradouro, numero - bairro - cidade/sigla estado
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("CPF já cadastrado! Usuário existente!")
        return

    nome = input("Infome o nome complete do usuário: ")
    data_nascimento = input("Infome a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - barro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")


def criar_conta(agencia, nro_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": nro_conta, "usuario": usuario}

    print("Usuário Não encontrado! Fluxo de Criação de conta encerrado!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: \t {conta['agencia']}
            C/C:\t{conta['nro_conta']}
            Titular: \t{conta['usuario']['nome']}

        """
        print("=" * 100)
        print(linha)


while True:  # Laço infinito

    opcao = input(menu)  # Faz a leitura do comando de entrada

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que você deseja depositar?:"))
        if (deposito > 0):  # Verifica se o valor a ser depositado é positivo
            saldo, extrato = depositar(saldo, deposito, extrato)
            depositos_acumulados = depositos_acumulados + deposito
        else:  # Se o valor a ser depositado for negativo
            print("Valor de saque inválido. Tente novamente!")


    elif opcao == "s":
        print("Saque")
        saque = float((input("Quanto você deseja sacar?:")))
        saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saques=numero_saques,
                               limite_saques=LIMITE_SAQUES)


    elif opcao == "n":
        criar_usuario(usuarios=lista_usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, nro_conta, lista_usuarios)
        if conta:
            contas.append(conta)
            # numerro_conta +=1

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "e":
        print_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("\n\nEncerrando...\n O Banco " " agradece a sua preferência!\n\n")
        break
    else:
        print("Operação Inválida! Por favor selecione novamente a operação desejada")
