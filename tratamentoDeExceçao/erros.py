# try:
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     media = (nota1 + nota2) / 2
#     print(media)
# except:
#     print("Valor invalido")

# while True:
#     try:
#         nota1 = float(input("Digite a primeira nota: "))
#         nota2 = float(input("Digite a segunda nota: "))
#         media = (nota1 + nota2) / 2
#         print(media)
#         break
#     except:
#         print("Digite novamente a nota de forma numerica")

# while True:
#     try:
#         preco = float(input("Digite o valor do produto: "))
#         quantidade = int(input("Digite o quantidade de produto: "))
#         conta = preco * quantidade
#         print(conta)
#         break
#     except Exception as erro:
#         print("Valor invalido" , type(erro))

while True:
    try:
        numero = float(input("Digite o numero"))
        resultado = 100 / numero
        print(resultado)
        break
    except ValueError:
        print("Digite um numero")
    except ZeroDivisionError:
        print("Digite um numero sem ser zero")
    except Exception as erro:
        print(erro)