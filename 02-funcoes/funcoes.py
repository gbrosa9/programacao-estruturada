"""Programação estruturada
29/08/2023

Funções

"""

'''def cabecalho():  # A palavra reservada def, na primeira linha, explicita a definição da função naquele ponto.
    print("=" * 30)
    print("Título do Relatório")
    print("=" * 30)

cabecalho()  # Aqui digamos pro python rodar tudo que tem dentro da função, que é da linha 9,10,11
'''


def cabecalho(titulo, sep="-", tamanho=30):   # Nesta ordem de titulo, sep e tamanho
    print(sep * tamanho)
    print(titulo)
    print(sep * tamanho)

#cabecalho("Relatório de despesas", sep="-", tamanho=25) 
#cabecalho("Folha de ponto", tamanho=20, sep="-")  

# ---------------------------------------------------------------------------------------------#

def soma (x,y):
    return x + y   # retornar algo de uma função para que ao se chamar essa mesma se tenha acesso ao valor retornado.

# print(16 - soma(10,12) * soma (1,2))

# Escopo local vs escopo global de vairáveis 

a = 2 # Escopo global
PI = 3.14 # Caixa alta == Constante, então não é pra ALTERAR quando estiver CAIXA ALTA.

def func():  # Quando colocamos underscare _ é porque a função é privada 
    global a # Não é uma boa prática!
    a = 3  # Escopo global
    print(a)

def func2():
    print(a)

print(a)
func()
print(a)
func2()



