def criarArquivo():
    contagem = 0
    with open("incidentes.txt", "a") as arquivo:
        while contagem < 3:
            servico1 = input("Serviço: ")
            descricao1 = input("Descrição: ")

            arquivo.write(servico1 + " - " + descricao1 + "\n")
            contagem += 1
    arquivo = open("incidentes.txt", "r")
    conteudo = arquivo.read()
    print("\n=== HISTÓRICO DE INCIDENTES ===")
    print(conteudo)
    arquivo.close()

criarArquivo()