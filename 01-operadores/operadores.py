
# Aula 2 - Programação Estruturada 22/08/2023

#  nome = input('Informe o seu nome: ')
#  print(type(nome))

#  idade = int(input('Informe a sua idade: '))
#  print(type(idade))

# Atribuição

x = 2 
x = 3 
x = x + 2
x += 2 # ---> mesma coisa que x = x + 2 
x /= 4 # ---> mesma coisa que x = x / 4

# Aritméticos

x = 10
y = 2.0
z = -2

print ( x + y)
print ( x - y)
print ( x * y)
print ( x / y)    # Retorno é sempre float (número decimal, ex: 5.0)
print ( x % y)    # Operador Módulo, é o resto retorna o resto da divisão do primeiro número pelo segundo
print ( x ** y)   # Operador Potência
print ( x // y)   # Divisão Inteira é o Quociente da Divisao   10 dividido por 2 = 5, entao 5 é a divisão inteira.

print ((x + 20) <= y * 2 != 10)

# Operações aritméticas com strings

print ("Olá," + "MUNDO!")  # Concatenação de Strings
print( 10* "-") # Um inteiro e uma String


# Comparação ou Relacionais
# Retornar True ou False

print(x > y) # True (Maior)
print(x < y) # False (Menor)
print(x >= y) # True (Maior ou Igual)
print(x <= y) # False  (Menor ou igual)
print(x == y) # False (Igual)
print(x != y) # True (Diferente)

# Booleanos ou Lógicos

print( True and False)
print( True or False)
print( not True)

print(bool(10))

x = 10
y = 'oi'

print(x and y)
