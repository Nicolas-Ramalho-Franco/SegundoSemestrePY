modos_camera = {
"noturno": {
"uso": "ambientes com pouca luz",
"dificuldade": 1
},
"retrato": {
"uso": "fotos de pessoas",
"dificuldade": 2
},
"documento": {
"uso": "fotos de textos e quadros",
"dificuldade": 3
},
"esporte": {
"uso": "movimento rápido",
"dificuldade": 4
}
}
avaliacoes = [8, 9, 7, 10]

def consultar_modo (modo):
    if modo in modos_camera:
        return modos_camera[modo]
    return "modo invalido"

def gerar_resulmo_avaliacao():
       soma=sum(avaliacoes)
       resultado = soma / len(avaliacoes)
       if resultado > 9:
        return f"seu resultado foi exelente{resultado}"
       return f"seu resultado foi aprovado{resultado}"

def mensagem_final(message = False):
    if message:
        return "Saindo do sistema"
    return "mensagem vazia ou sem saida"


def recomendar_modo(dificuldade_procurada):
    for nome_modo, detalhes in modos_camera.items():
     if detalhes["dificuldade"] == dificuldade_procurada:
      return f'O modo recomendado é "{nome_modo}" (Uso: {detalhes["uso"]})'
    return "Modo invalido"


print(recomendar_modo(2))
print(recomendar_modo(4))
print(recomendar_modo(5)) # testando o modo invalido
print(mensagem_final(message=True))
print(mensagem_final()) # testando o modo sem sair
print(consultar_modo("noturno"))
print(gerar_resulmo_avaliacao())