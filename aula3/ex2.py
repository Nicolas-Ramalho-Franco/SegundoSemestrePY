# Crie uma função chamada gerar_mensagem

# A função deve receber um parâmetro chamado estudante
# com valor padrão True.

# Se estudante for True:
# retorne "Modo simples ativado"

# Se estudante for False:
# retorne "Modo avançado ativado"

def gerar_mensagem(estudante =True):
    if estudante:
        return "Modo simples ativado"
    else:
        return "Modo avançado ativado"

print(gerar_mensagem(estudante = False))
print(gerar_mensagem())