print("Sistema de gestão de prioridade")

print("1.Capitar Problema")
print("2.Consultar Problema")
print("3.media de chmados")
print("4. Mostar todos os chamados de problema")
print("5.Sair")

DBdesafio={}

opc = input("Digite a sua opção : ")
match opc :
    case "1":
        identificadorChamado = input("Digite o nome de chamado: ")
        DBdesafio[identificadorChamado] = {
            "sistema_servico": input("Digite o nome do sistema afetado ou o nome do serviço afetado: "),
            "nivel_problema": int(input("Digite o nível do problema de 1 a 3: ")),
            "horas_abertas": float(input("Digite a quantidade de horas em aberto: ")),
            "usuarios_afetados": int(input("Digite o número de usuários afetados: ")),
            "ambiente_problema": input("Digite o nome do ambiente do problema: ")
        }
        print("\nBase de dados de chamados atualizada:")

    case "2":
        print("Procurar chamado:")
        busca= input("Digite o nome do chamado: ")

        if busca in DBdesafio:
            print(f"\n Chamado '{busca}' encontrado!")

            # Acessa o dicionário interno do chamado encontrado
            dados = DBdesafio[busca]

            # Exibe os dados organizados
            print(f"• Sistema/Serviço: {dados['sistema_servico']}")
            print(f"• Nível do Problema: {dados['nivel_problema']}")
            print(f"• Horas em Aberto: {dados['horas_abertas']}h")
            print(f"• Usuários Afetados: {dados['usuarios_afetados']}")
            print(f"• Ambiente: {dados['ambiente_problema']}")
        else:
            print(f"\nO chamado '{busca}' não existe na base de dados.")

    case "3":
        print("Voce escolheu incerir nota")

    case "4":
        print("\nBase de dados de chamados atualizada:")
        print(DBdesafio)

    case "5":
        print("Saindo.....")
    case _:
        print("Opção invalida........")
