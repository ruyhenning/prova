def gerar_lista_usuarios():
    escolha = ""
    usuarios = []
    while escolha != 5:
        print("Seja Bem-vindo,cadastre seus usuarios")
        print("1)cadastrar usuarios")
        print("2)verificaçao")
        print("3)alterar usuario")
        print("4)deletar usuario")
        print("5)ao encerrar digite fim")
    try:
        escolha = int(input("digite sua escolha: "))
            
        match escolha:
            case 1:
                print("-----cadastrar usuario-----")
                print("-----digite sair ao terminar-----")
                while True:
                    nome_usuario = input("nome de usuario: ").strip().lower()
                    if nome_usuario == "fim":
                        break
            case 2:
                print("-----verificaçao de usuario-----")
                print("verificaçao validada. digite FIM ao finalizar")
                while True:
                        verificaçao_usuario = input("nome de usuario: ").strip().lower()
                        if verificaçao_usuario == "fim":
                            break
                        if verificaçao_usuario == cadastro_usuario:
                            print("Esta cadastrado")
                        else:
                            print("Nao esta cadastrado")
            case 3:
                print("-----alteraçao de usuario------")
                print("digite o nome que deseja alterar")
            case 4:
                print("-----excluir usuario")

    except ValueError:
        print("opçao invalida! digite outro numero.")

gerar_lista_usuarios()


