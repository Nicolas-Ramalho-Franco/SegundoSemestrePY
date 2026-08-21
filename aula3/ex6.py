# Exercício 6 — Avaliação de uma configuração da câmera
#
# Objetivo: Usar vários parâmetros em uma regra de avaliação e devolver mais de um resultado.
#
# Situação
#
# Um grupo testou uma configuração da câmera e precisa registrar três notas: qualidade da imagem, facilidade de uso e utilidade.
#
# Sua tarefa
#
# • Crie a função avaliar_configuracao(nome, qualidade, facilidade, utilidade).
#
# • A função deve receber obrigatoriamente os quatro valores por parâmetros.
#
# • Calcule a média das três notas dentro da função.
#
# • Se a média for maior ou igual a 8, a situação deve ser "aprovada"; caso contrário, deve ser "revisar".
#
# • Retorne três informações: nome, media e situacao.
#
# • Faça uma chamada usando argumentos nomeados.
#
# • Teste pelo menos duas configurações diferentes e mostre os resultados fora da função.

nota =[]
def avaliar_configuracao(nome):

    clareza = int(input(f"Digite uma nota de 0 a 10 para a clareza do modo {nome}:"))
    nota.append(clareza)
    utilidade = int(input(f"Digite uma nota de 0 a 10 para a utilidade do modo {nome}:"))
    nota.append(utilidade)
    facilidade = int(input(f"Digite uma nota de 0 a 10 para a facilidade do modo {nome}:"))
    nota.append(facilidade)
    media = sum(nota) / len(nota)
    print(f"Voce deu nota para o recurso: {nome} e a media e: {media}")
    return media

avaliar_configuracao(input("Digite o nome do recuroso que queira avaliar:"))
