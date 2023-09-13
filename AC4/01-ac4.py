# n % x !=0,  quando x for diferente de 1, e x diferente de n
 # Saber qual é primo e nao é.

# É primo quando o único divisor for 1, e ele mesmo

'''def e_primo(num):
    for div in range(2, num):
        if num % div == 0: #  Ele retorna o resto da divisão do operando da esquerda pelo operando da direita.
            # Ele é usado para obter o resto de um problema de divisão.
            print('Não é primo')
            break
    
    else:
        print('É primo')

e_primo(7)
e_primo(14)'''


# Exercicio 1 - AC4

def e_primo(num):
    
    primo = True
    for div in range(2, num):
    
        
        if num % div == 0: #  Ele retorna o resto da divisão do operando da esquerda pelo operando da direita.
            # Ele é usado para obter o resto de um problema de divisão.
            primo = False
            print(f'Não sendo primo, o {num} é divisível por {div} .')
             
    print(f'É primo? {primo}')

e_primo(7)
e_primo(14)

