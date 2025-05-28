nome = input("digite seu nome:")
valor1 = int(input("digite o primeiro valor:"))
valor2 = int(input("digite o segundo valor:"))

print("Olá", nome)

if(valor1 > valor2):
    print("valor1 e maior que o valor2")

elif(valor2 > valor1 ):
     print("o valor2 é maior que o valor1")

else:
    print("os valores iguais")
            
nota1 = int(input("nota 1: "))
nota2 = int(input("nota 2: "))
nota3 = int(input("nota 3: "))
nota4 = int(input("nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) /4

if(media == 100):
    print("excelente", media)
elif(media == 80):
    print("muito bom", media)
elif(media == 70):
    print("bom", media)
elif(media < 70):
    print("precisa melhorar", media)

else:
    print("nao caiu em nenhuma condicional", media)

