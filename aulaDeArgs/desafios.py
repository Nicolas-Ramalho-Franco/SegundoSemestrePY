# • Crie a função configurar_camera(**opcoes).
# • Dentro dela, obtenha modo com padrão "automatico" e qualidade com padrão "média" usando .get().
# • Retorne modo e qualidade.
# • Crie uma lambda chamada mensagem que receba um modo e devolva esse modo em uma mensagem
# simples.
# • Teste configurar_camera(modo="noturno") e configurar_camera(modo="retrato", qualidade="alta").
# • Use a lambda para mostrar uma mensagem para pelo menos um dos modos retornados.
# • Não use map(), filter() ou reduce() neste exercício.

def configurar_camera(**opcoes):
    modo = opcoes.get("modo","Automatico")
    qualidade = opcoes.get("qualidade","media")
    return modo,qualidade

mensagem = lambda receba: [print(f"{i + 1}°: {receba[i]}") for i in range(len(receba))]

print(configurar_camera(modo="modo",qualidade="qualidade"))
print(configurar_camera(qualidade="qualidade"))
camera =["hdr","noturno","claro"]
mensagem(camera)

