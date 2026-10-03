import json

incidentes = []
nome = "incidentes.json"

def registrar():
    for i in range(3):
        servico = input("Serviço: ")
        status = input("Status: ")
    incidente = {
        "servico": servico,
        "status": status
    }
    incidentes.append(incidente)
    with open(nome, "a", encoding="utf-8") as arq:
        json.dump({"incidentes": incidentes}, arq)

def consultar():
    with open(nome , "r", encoding="utf-8") as arq:
        incidentes = json.load(arq)

def menu():
    print("""
    1-Registrar  incidente
    2-Consultar histórico
    3-Sair
    """)
    opc = input("Digite a sua opcao: ")


opc = input("Digite a sua opcao: ")
match opc:
    case "1":
        registrar()
    case "2":
        consultar()
    case "3":
        print("Sair .....")

