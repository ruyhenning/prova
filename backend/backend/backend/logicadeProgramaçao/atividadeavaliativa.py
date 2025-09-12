import json

ARQUIVO_PERIFERICOS = 'perifericos.json'
ARQUIVOS_CATEGORIAS = ' categoria'

categorias= []
perifericos = []

id_categorias = 1
id_perifericos = 1

def carregar_arquivo(perifericos):

    try :
            with open ('categorias.json','r') as arquivo:
                return json.load(arquivo)
    except FileNotFoundError:
            return []
        
def salvar_arquivo(nome, dados):
    with open(nome,'w') as arquivo:
            json.dump(dados,arquivo, indent=4)

    try:
            escolha = int(input("digite sua escolha: "))

    except FileNotFoundError:
     print("somentes numeros")

def exibir_menu():
    print("\n----perifericos----")
    print("1)cadastrar perifericoss")
    print("2)cadastrar categoria")
    print("3)listar categoria") 
    print("4)listar perifericos")
    print("[5]sair")


def cadastrar_categoria():
    global id_categorias
    global categorias

    nome_categoria = input("nome categoria: ")
    categoria = {"id": id_categorias, "nome": nome_categoria}
    categorias.append(categoria)

    salvar_arquivo(ARQUIVOS_CATEGORIAS,categorias)
    id_categorias += 1

    print("categoria cadastrada com sucesso !!")

def cadastrar_perifericos():
    global id_perifericos
    global perifericos
    nome_perifericos = input("nome dos perifericos: ")
    preco = float (input("preço: "))
    id_categorias = int(input("ID das categorias: "))
    perifericos = {

        "id": id_perifericos,
        "nome": nome_perifericos,
        "id_categorias": id_categorias
    }
    perifericos.append(perifericos)
    salvar_arquivo(ARQUIVO_PERIFERICOS)
    id_perifericos+= 1

    print ("periferico cadastrado com sucesso !!")

def listar_categorias():
    global categorias
    if categorias:
        print("CATEGORIAS:")
        for categorias in categorias:
            print(f"ID: {categorias['id']} - Nome: {categorias['nome']}")
    else:
        print("Nenhuma categoria cadastrada.")

def listar_perifericos():
    global perifericos
    global categorias
    if perifericos:
        print("Perifericos:")
        for perifericos in perifericos:
            print(f"ID: {perifericos['id']} - Nome: {perifericos['nome']} - Preço: {perifericos['preco']} - Categoria: {perifericos['id_categoria']}") 
    else:
        print("sem perifericos cadastrado.")

categorias = carregar_arquivo(ARQUIVOS_CATEGORIAS)
perifericos = carregar_arquivo(ARQUIVO_PERIFERICOS)

while True:
    exibir_menu()
    opcao = input("Escolha: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_perifericos()
    if opcao == '3':
        listar_categorias()
    elif opcao == '4':
        listar_perifericos()
    elif opcao == '5':
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida.")

listar_perifericos()