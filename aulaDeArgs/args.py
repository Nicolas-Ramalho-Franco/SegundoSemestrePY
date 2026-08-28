# def CriarListaRecurso(*recursos):
#     listaRecurso = []
#     for recurso in recursos:
#         listaRecurso.append(recurso)
#
#     print(listaRecurso)
#
# CriarListaRecurso("HDR","GRADE")
# CriarListaRecurso("TIMER","FOCO","ZOOM")



# def SomaNota (*args):
#     print(sum(args)/len(args))
#
# SomaNota(1,2,3,4,5,6,7,8,9,10)


# def MostrarConfiguracao(**conig):
#     print(conig)
#
# MostrarConfiguracao(
#     nome='nicolas',
#     idade=18,
#     sexo='M'
# )

# def MostrarConfig (**args):
#     for chave in args:
#         print(chave , ":", args[chave])
#
#
#
# MostrarConfig(
#     nome='nicolas',
#      idade=18,
#      sexo='M'
# )

# def configurar_captura(**opcoes):
#     modo = opcoes.get("modo", "automatico")
#     qualidade = opcoes.get("qualidade", "média")
#     flash = opcoes.get("flash", True)
#     return modo, qualidade, flash
#
# print(configurar_captura(modo="noturno"))
# print(configurar_captura(modo="retrato",
# qualidade="alta", flash=False))

def CriarListaRecurso(*recursos):
    listaRecurso = []
    for recurso in recursos:
        listaRecurso.append(recurso)

    print(listaRecurso)

def resulmo_config(**recursos):
    contar = 0
    for recurso in recursos:
        contar += 1
    print(f"Voce adicionou essa quantidade de recursos: {contar}")


prontos = lambda conta : conta +conta
print(prontos(5),prontos(9))

media = lambda conta : "reprovou" if conta<=6 else "passou"
print(media(conta=prontos (5)))

resulmo_config(
    nome='nicolas',
    idade=18,
    sexo='M')
CriarListaRecurso("TIMER","FOCO","ZOOM")


