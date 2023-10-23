'''Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. 
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

def numeros(n):
    for i in range(1, n+1):
        print(*range(1, i+1)) 

n = int(input('Digite um número inteiro: '))

numeros(n)