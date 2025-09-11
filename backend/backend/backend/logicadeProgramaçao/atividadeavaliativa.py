import json

ARQUIVO_PERIFERICOS = 'perifericos.json'
ARQUIVOS_CATEGORIA = ' categoria'

categoria= []
perifericos = []

id_categoria = 1
id_perifericos = 1

def carregar_arquivo(perifericos):

    try :
        with open (categoria.json,'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_arquivo(nome, dados):
    with open(nome,'w') as arquivo:
        json.dump(dados,arquivo, indent=4)

    try:
        escolha = int(input("digite sua escolha: "))

def ixibir_menu():
    print("\n----perifericos----")
    print("1)cadastrar perifericoss")
    print("2)cadastrar categoria")
    print("3)listar categoria") 
    print("4)listar perifericos")
    print("[5]sair")

def cadastrar_perifericos():
    global id_perifericos
    global perifericos
    nome_perifericos = input("nome do perifericos: ")
    preco = float (input("preço: "))
    id_categoria = int(input("ID da categoria: "))
    perifericos = {

        "id": perifericos_id,
        "nome": nome_perifericos,
        "id_categoria": id_categoria
    }
    perifericos.append(perifericos)
    salvar_arquivo(ARQUIVO_PERIFERICOS)
    perifericos_id+= 1

def cadastrar_categoria(categoria_id):
    nome_categoria = input("nome categoria: ")
    categoria_id+= 1
    categoria = {"id": categoria_id, "nome": nome_categoria}
    categoria.append(categoria)
    salvar_arquivo(ARQUIVOS_CATEGORIA, categoria)
    print("categoria cadastrada com sucesso! ")
