print("Sistema de gestão de prioridade")

print("1.Capitar Problema")
print("2.Consultar Problema")
print("3.media de chamados")
print("4. Mostar todos os chamados de problema")
print("5.Sair")

DBdesafio={}

opc = input("Digite a sua opção : ")
match opc :
    case "1":
        identificadorChamado = input("Digite o nome de chamado: ")
        DBdesafio[identificadorChamado] = {
            "sistema_servico": input("Digite se e sistema ou serviço: "),
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

            if dados['nivel_problema'] >=3 and dados['sistema_servico'] == "producao":
                print("Critico")
            elif dados['nivel_problema'] >=3 and dados['usuarios_afetados']==100:
                print("Alta")
            elif dados['nivel_problema'] >=2 or dados['horas_abertas'] > 4.0:
                print("media")
            else:
                print("Baixa")

        else:
            print(f"\nO chamado '{busca}' não existe na base de dados.")

    case "3":
        print("Voce escolheu incerir nota")
        if len(DBdesafio) == 0:
            print("Não existem chamados cadastrados.")
        else:
            quantidade_nivel_1 = 0
            quantidade_nivel_2 = 0
            quantidade_nivel_3 = 0
            soma_niveis = 0

            for chamado, dados in DBdesafio.items():
                nivel = dados["nivel_problema"]

                if nivel == 1:
                    quantidade_nivel_1 += 1
                elif nivel == 2:
                    quantidade_nivel_2 += 1
                elif nivel == 3:
                    quantidade_nivel_3 += 1

                soma_niveis += nivel

            total_chamados = len(DBdesafio)
            media = soma_niveis / total_chamados

            print("\n===== RESUMO DOS NÍVEIS =====")
            print(f"Total de chamados: {total_chamados}")
            print(f"Chamados nível 1: {quantidade_nivel_1}")
            print(f"Chamados nível 2: {quantidade_nivel_2}")
            print(f"Chamados nível 3: {quantidade_nivel_3}")
            print(f"Média do nível de severidade: {media:.2f}")

    case "4":
        if len(DBdesafio) == 0:
            print("Não existem chamados cadastrados.")
        else:
            for chamado, dados in DBdesafio.items():
                print("\n-----------------------------")
                print(f"Chamado: {chamado}")
                print(f"Sistema/Serviço: {dados['sistema_servico']}")
                print(f"Nível do Problema: {dados['nivel_problema']}")
                print(f"Horas em Aberto: {dados['horas_abertas']}h")
                print(f"Usuários Afetados: {dados['usuarios_afetados']}")
                print(f"Ambiente: {dados['ambiente_problema']}")

    case "5":
        print("Saindo.....")
    case _:
        print("Opção invalida........")
