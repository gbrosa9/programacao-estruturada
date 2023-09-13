# Exercicio 03 - AC4.


print(20*"=")
print('\nExercicio 3\n')

def num_positivos():
    
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0

    
    while True:
        numero = float(input('\nDigite um número: '))
        
        if numero > 0:
            print(f'\nO número {numero} é maior que 0.\n')
            print(20*"=")
            
        else:
            print(f'\nO numero {numero} e negativo.\nEncerrando Programa...')
            break
        
        if 0 <= numero and numero <= 25:
            contador1 += 1
        elif 26 <= numero and numero <= 50:
            contador2 += 1
        elif 51 <= numero and numero <= 75:
            contador3 += 1
        elif 76 <= numero and numero <= 100:
            contador4 += 1

    print(f'\nNúmeros no intervalo de 0 a 25: {contador1}')
    print(f'\nNúmeros no intervalo de 26 a 50: {contador2}')
    print(f'\nNúmeros no intervalo de 51 a 75: {contador3}')
    print(f'\nNúmeros no intervalo de 76 a 100: {contador4}\n')

num_positivos()