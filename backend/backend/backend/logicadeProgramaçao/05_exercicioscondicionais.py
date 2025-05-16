num1 = int(input("digite o valor:"))
num2 = int(input("digite o valor:"))
operacao = (input("digite a operacao : "))
 
match operacao:
    case "*":
        soma = num1 * num2
        print("soma", soma)

idade = int(input("sua idade?"))

match idade:
     
    case x if x <12 :
        print("crianca")
    case x if x >=12 and x <18:
        print("adolescente")
    case x if x >=18 and x <60:
        print("adulto")
    case x if x >=60 and x <100:
        print("idoso")
    case x if x >=100 :
        print("morto")  

notas = int(input("sua nota?"))

match notas:

    case 10:
      print("gabaritou")
    case 7|8|9:
      print("ta na media")
    case 1|2|3|4|5|6:
      print("reprovado huahauha")
    case _:
        print("nota invalida")
