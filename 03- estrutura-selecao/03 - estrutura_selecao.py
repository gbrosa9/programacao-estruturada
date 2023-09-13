"""
Programação Estrutura
2023.2

Estrutura de seleção

if <Teste logico>:
    <codigo>
else:
    <codigo>

"""

def e_par(num):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")

    print("Fim da função")

# e_par(4)
# e_par(5)

def conceito(nota):
    if nota > 9:
        print("Conteito A")
    elif nota > 8:
        print("Conceito B")
    elif nota > 7:
        print("Conceito C")
    else:
        print("Conceito D")

# conceito(9.5)
# conceito(5)

# Pesquisar sobre o match

# def cli():
#     opcao = input("Digite 1 para inserir nome, 2 para nota, ou "
#                   "qualquer outro caractere para sair:")

#     match opcao:
#         case "1":
#             print("Opção 1")
#         case "2":
#             print("Opção 2")
#         case _:
#             print("Sair")

# Exercicios

# def e_par2(num):
#     return num % == 0

def maior (num1, num2):
    if num1 > num2:
        return num1

    return num2

# Ternário
def maior2(num1, num2):
    return num1 if num1 > num2 else num2

def ve_num(num):
    if num > 0:
        print(num, "esse número e positivo")
    else:
        print(num, "esse número e negativo")


# ve_num(-5)
# ve_num(5)


# 1 Elabore uma função e_par, que receba um número e retorne True ou FALSE ONCONFORME O NÚMERO SEJA PAR OU NÃO



def positivo (num):
    if num > 0:
        return "positivo"
    if num == 0:
        return "zero"
    
    return "negativo"







