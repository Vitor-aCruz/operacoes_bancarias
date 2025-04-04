menu = """

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

while True:
    opcao = input(menu)

    if opcao == "d":
        dep = float(input(f"Digite a quantia a ser depositada:" ))

        if dep > 0 :
            print (f"Depósito realizado com sucesso no valor de {dep:.2f}!")
            saldo += dep
            extrato += f"Depósito de : R$ {dep:.2f}\n"
    elif opcao == "s":
        saq = float(input(f"Digite o valor a ser sacado: "))

        excedeu_saldo = saldo < saq
        excedeu_limite = saq > limite
        excedeu_limite_saq = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print (f"Transação falhou! Saldo indisponível.")
            print (f"Saldo disponivel atualmente : {saldo:.2f}.")
 
        elif excedeu_limite:
            print (f"Transação falhou! Limite por saque é de {limite:.2f}")
 
        elif excedeu_limite_saq:
            print ("Transação falhou! Quantidade de saques excedidas!")

        elif saq > 0:
            print (f'Saque realizado no valor de {saq:.2f}.')
            saldo -= saq
            extrato += f"Saque de : R$ {saq:.2f}\n"
            numero_saques +=1
        else:
            print ("Operação inválida!!")
            
    elif opcao == "e":
        print ("Nenhuma movimentação foi realizada."if not extrato else extrato)
        print (f"Saldo atual: R$ {saldo:.2f}.")

    elif opcao == "q":
        break
    
    else : 
        print("Operação inválida!!")

print ("Obrigado por utilizar nossos serviços, até a próxima!")




