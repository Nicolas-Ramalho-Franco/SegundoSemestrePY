import test

# def consultar_modo(modos, modo):
#     if modo in modos:
#      return modos[modo ]
#     return "Modo não cadastrado"
#
# modos_camera = {
#     "noturno": "melhora fotos com pouca luz",
#     "retrato": "destaca pessoas",
#     "documento": "melhora leitura de textos"}
#
# print(consultar_modo(modos_camera, "noturno"))
#
# def configuracao(configuracoes, recurso):
#     if recurso in configuracoes:
#      return configuracoes[recurso]
#     return "recurso não cadastrado"
#
#
# print(configuracao(test.configuracoes, "hdr"))

# def consultar_modo(dados , chave):
#     if chave in dados:
#       return dados[chave]
#     return "recurso não cadastrado"
#
# print(consultar_modo(test.modos , "noturno"))


# Base de trabalho enunciado
# Crie uma função chamada gerar_mensagem
# A função deve receber um parâmetro chamado estudante
# com valor padrão True.
# Se estudante for True:
# retorne "Modo simples ativado"
# Se estudante for False:
# retorne "Modo avançado ativado"
# Teste:
# gerar_mensagem()
# gerar_mensagem(estudante=False)
#
# def gerar_mensagem(estudante = False):
#     if estudante ==True:
#         return "Modo simples Ativo"
#     return "Modo avançado ativo"
#
# print(gerar_mensagem())
# print(gerar_mensagem(estudante=True))

def avaliar_recurso(nome, clareza, utilidade, facilidade):
    media = (clareza + utilidade + facilidade) / 3
    return nome, media
# Chamada pouco clara:
resultado = avaliar_recurso("modo estudo", 8, 9, 7)
print(resultado)