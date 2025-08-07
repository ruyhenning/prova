nome = input("nome de cadastro:")
print("bem vindo! " + nome)
saldo = 0
opcao= ""

while opcao !="sair":
    print("\n1. Depositar\n2. sacar\n3. saldo-atual\nsair")
    opcao = input("escolha sua opcao:")

    match opcao:
        case "1":
            saldo += float(input("valor: "))
            print("deposito feito")
        case "2":
            valor = float(input("valor: "))
            if valor <= saldo:
                saldo -=valor
                print("saque feito")
            else:
                print("saldo indisponivel")
        case "3":
            print("saldo atual: R$", saldo)
        case "sair":
            print("volte sempre," + nome + "!")
        
           
        
               
