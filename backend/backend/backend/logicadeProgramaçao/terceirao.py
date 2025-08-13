def gerar_nomes_alunos():

    print("liste os alunos^^")
    print("Ao terminar digite encerrar")
    with open("alunos.txt", 'w') as alunos:
        while True :
            aluno = input ("liste os nomes: ")
            if aluno.lower()=="encerrar":
                print("encerrando")
                break
            alunos.write(aluno+"\n")
gerar_nomes_alunos()

def listar_alunos():
    with open ("alunos.txt", 'r') as listar:
        print("-----listar alunos-----")
        for alunos in listar:
            nomes = alunos.strip()
            print("alunos: ", nomes)
listar_alunos()



    