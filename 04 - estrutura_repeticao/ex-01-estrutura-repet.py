''''
Elaborar uma função conta_pares(min, max) para exibir todos os valores entre min e max,
com um incremento de 2, separando-os com um hífen. Ex.: 2 – 4 – 6 – 8 – 10 – 12 – 14.
'''

# Exercício 1

'''def conta_pares(min, max):
    pass
    for c in range(min, max, -2):
        print(c, "-")

conta_pares(14, 0) '''

# Ex 1 do professor:


def conta_pares(min, max):
        if min % 2 != 0:
                min += 1

        if max % 2 != 0:
              max -= 1

        for num in range(min, max +1, 2):
                if num < max:
                    print(num, end=" - ")
                else:
                    print(num)

# conta_pares(1, 15)

                

# Exercício 2

def usuario_senha():
        usuario = (input('Digite um nome de usuário:'))
        senha = (input('Digite uma senha: '))

        while senha == usuario:
            usuario = input(('Valores iguais, exiba uma nova senha: '))
        
        if senha != usuario:
              print('Parabéns, você foi cadastrado com sucesso!')
        


usuario_senha()



