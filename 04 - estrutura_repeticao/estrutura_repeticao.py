"""
Programação Estruturada  - (12/09/2023)
Estrutura de Repetição

"""



def contagem_regressiva(num):
    while num >0:
        print(num)
        num -= 1

# contagem_regressiva(5)

def pede_nome():
    nome = input('Informe o seu nome: ')

    while nome == "": # Enquanto não for digitado nada, ele retornará para perguntar o nome.
        nome = input('Texto passado é inválido! Informe um nome: ')


    print(f'Olá {nome}')

#pede_nome()

def numero():
    while True:
        numero = int(input('Informe um número: '))

        if numero == 3:
            print('Escreveu 3!')
            continue # Interrompe a iteração corrente     !IMPORTANTE!

        if numero == 5:
            break  # Interrompe por completo a estrutura de repetição   !IMPORTANTE!

        print('Próximo número')
         
        
#numero()

def tentativas():
    num_tentativas = 0

    while num_tentativas < 3:
        nome = input('Informe um nome: ')

        if nome != "":  # != significa diferente   "" significa vazio
            print('Olá', nome)
            break


        num_tentativas += 1  # += está dizendo de uma maneira mais simples que o total recebe o próprio valor de total + o conteúdo

    else: # Só vai ser executado caso não tenha passado pelo break.
        print('Nenhum nome foi inserido')
        nome = 'erro'

    print(nome)
#tentativas()


# =============================

def contagem_regressiva2(num):
    for cont in range (num, 0, -1): # 5 4 3 2 1   (o -1 serve pra ir de num que recebe 5 até 1, porque vai diminuindo 1)
        print(cont)

# contagem_regressiva2(5)


def imprime_texto():
    for _ in range(5):
        print('Texto')
    
imprime_texto()