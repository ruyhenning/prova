def gerar_lista_compras():

    print("seja bem-vindo,vamos as compras")
    print("Ao encerrar digite fim")
    with open("comida.txt", 'w') as comida:
        while True :
            item= input ("digite o item: ")
            if item.lower()=="fim":
                print("encerrando lista")
                break
            comida.write(item+"\n")
gerar_lista_compras()

def lista_itens():
    with open ("comida.txt", 'r') as lista:
        print("-----lista de compras-----")
        for item in lista:
            produto = item.strip()
            print("item: ", produto)
lista_itens()

    
