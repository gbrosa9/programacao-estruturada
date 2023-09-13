
'''def positivo (num):
    if num > 0:
        return "positivo"
    if num == 0:
        return "zero"
    
    return "negativo" '''


# VOGAL LETRA EXERCICIO

'''def ve_vogal(vogal):
    
    if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u' or vogal == 'e':
        print('Vogal')
    else:
        print('Consoante')

ve_vogal('b')'''


# CALCULO DE MEDIA EXERCICIO

def notas(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if nota1 >= 11 or nota2 >= 11 or nota3 >= 11:
        print('A nota é inválida') 
            
    elif media == 10:
        print('Aprovado com distinção')
    
    elif media >= 7:
        print('Aprovado!')

    elif media <=6:
        print('Reprovado')    
    
notas(10, 3, 10)

