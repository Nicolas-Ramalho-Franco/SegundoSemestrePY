produto = {"nome":"Teclado" , "Preco" : 120.0}

while True:
    try:
        pesquisa = input("Digite o nome do produto:").lower()
        print(produto[pesquisa])
        break
    except KeyError :
        print("Voce digitou o valor errado")
