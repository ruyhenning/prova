import json

usuario = []


def carregar_arquivo():

    try :
        with open ('sistemacadastro.json','r') as arquivo:
            usuario = json.load(arquivo)
            print("cadastro carregado!")
    except FileNotFoundError:
        print("cadastro não encontrado")


def gerar_nomes_usuario():
    
    print("/n-----cadastrar usuario-----")

    nome_usuario = input("Nome do usuario: ").strip().lower()

    while True:
        try:    
            telefone = int(input("digite seu telefone: "))
            break

        except ValueError:
            print("digite somente numero")

    while True:
        try:
            idade = int(input("digite sua idade: "))
            break

        except ValueError: 
            print("somente sua idade")

    while True:
        try:
            cidade = input("digite sua cidade: ")
            break

        except ValueError: 
            print("somente o nome da cidade")

    while True:
        try:
            sexo = input("digite seu sexo: ")
            break

        except ValueError:
            print("digite somente palavras")

    novo_usuario = {
        "nome_usuario": nome_usuario,
        "telefone": telefone, 
        "idade":idade, 
        "cidade":cidade,
        "sexo":sexo,
    }

    usuario.append(novo_usuario)

    with open('usuarios.json','w')as arquivo :
        json.dump(usuario,arquivo,indent=5)
        print(f"\n produto{nome_usuario}foi cadastrado")

carregar_arquivo()
gerar_nomes_usuario()
    
            




