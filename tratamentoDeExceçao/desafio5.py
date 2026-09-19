from _pyrepl import keymap

aluno={
    "nome":"Lia",
    "notas" :{"Python":8.5 , "calculo":7.0}
}

def verAluno(aluno,materia):
    nota = aluno["notas"][materia]
    print(f"A nota a {materia} é: {nota}")
try:
    print("--- Teste 1: Registo válido ---")
    verAluno(aluno, "Python")

    print("\n--- Teste 2: Disciplina inexistente ---")
    verAluno(aluno, "Fisica")
except KeyError as e:
    print(f"Erro de chave: A estrutura não contém a secção 'notas' ou a disciplina {e} é inexistente.")

except TypeError:
    print("Voce digitou um nome que não existe em nosso sistema")
