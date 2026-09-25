def Menu():
    print("-"*30)
    print("Bem vindo ao menu")
    print("-"*30)

def salvar():
    servico = input("Digite seu servico: ")
    descricao = input("Digite sua descricao: ")
    with open("desafioarquivo.txt", "a") as arquivo:
        arquivo.write(servico + " - " + descricao + "\n")

def consultar():
    try:
        with open("desafioarquivo.txt", "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo ainda não existe. Salve um serviço primeiro.")

Menu()
while True:
    print("""
    1 - Salvar
    2 - Consultar
    3 - Sair
    """)
    opcao = int(input("Digite sua opcao: "))

    match opcao:
        case 1:
            salvar()
        case 2:
            consultar()
        case 3:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida, tente novamente.")