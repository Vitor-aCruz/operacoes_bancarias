menu = """
[c] Criar usuariario
[cc] Criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
conta = []





def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado.")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")
        return conta
    print(f"Usuário não encontrado.")
    

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de : R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
    else:
        print("Valor de depósito inválido.")
    return saldo , extrato

def sacar (*,saldo, valor , extrato , limite , limite_saques,numero_saques):
        excedeu_saldo = saldo < valor
        excedeu_limite = valor > limite
        excedeu_limite_saq = numero_saques >= limite_saques

        if excedeu_saldo:
            print (f"Transação falhou! Saldo indisponível.")
            print (f"Saldo disponivel atualmente : {saldo:.2f}.")
 
        elif excedeu_limite:
            print (f"Transação falhou! Limite por saque é de {limite:.2f}")
 
        elif excedeu_limite_saq:
            print ("Transação falhou! Quantidade de saques excedidas!")

        elif valor > 0:
            print (f'Saque realizado no valor de {valor:.2f}.')
            saldo -= valor
            extrato += f"Saque de : R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print ("Operação inválida!!")
        return saldo , extrato, numero_saques
def exibir_extrato(saldo, / , * , extrato):
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"Saldo: R$ {saldo:.2f}")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input(f"Digite a quantia a ser depositada:" ))
        saldo , extrato = depositar(saldo,valor,extrato)
        
           
    elif opcao == "s":
        valor = float(input(f"Digite o valor a ser sacado: "))
        saldo , extrato , numero_saques = sacar(
            saldo = saldo,
            valor=valor,
            extrato = extrato,
            limite=limite,
            limite_saques=LIMITE_SAQUES,
            numero_saques=numero_saques

        )
        
    elif opcao == "e":
        extrato = exibir_extrato(saldo , extrato=extrato)


    elif opcao == "c":
        criar_usuario(usuarios)

    elif opcao == "cc":
        numero_conta = len(conta)+1
        nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if nova_conta:
            conta.append(conta)
        

    elif opcao == "q":
        break

print ("Obrigado por utilizar o nosso serviço bancário!")
      




