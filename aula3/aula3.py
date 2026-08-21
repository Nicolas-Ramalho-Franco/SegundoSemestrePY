recursos = {
    "noturno": "melhora fotos com pouca luz",
    "retrato": "destaca pessoas",
    "documento": "melhora leitura de textos"
}
nota=[]

def configuracao(dados, recurso):
     if recurso in dados:
      return dados[recurso]
     return "recurso não cadastrado"

def avaliar_recurso(dados,nome):
    if nome in dados:
        clareza = int(input("Digite uma nota de 0 a 10 para a clareza do recurso:"))
        nota.append(clareza)
        utilidade = int(input("Digite uma nota de 0 a 10 para a utilidade do recurso:"))
        nota.append(utilidade)
        facilidade = int(input("Digite uma nota de 0 a 10 para a facilidade do recurso:"))
        nota.append(facilidade)
        media = sum(nota)/ len(nota)
        devolucao = print(f"Esse foi o recurso escolido para fazer a avaliaçao: {nome}, e ele tem essa media: {media}")
        return devolucao
    return "recurso não cadastrado"

opc = input("""
    digite a sua opc
    1. avaliar recurso
    2. avaliar utilidade
    0.Sair..
""")
while opc != "0":
    match opc:
        case "1":
            avaliar_recurso(recursos, input("Digite o nome do recurso: "))
        case "2":
            configuracao(recursos, input("Digite o nome do recurso: "))
        case _:
            print("Opção inválida........")
    opc = input("Digite a sua opção: ")

print("Saindo do recurso..... muito obrigado volte sempre")
