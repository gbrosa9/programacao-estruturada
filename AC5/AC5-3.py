def divide_numeros():

    try:
        num1 = int(input("Digite um número inteiro: "))

        num2 = int(input("Digite o segundo número inteiro: "))

        resultado = (num1 / num2)

    except ValueError:
        print('Erro! O valor inserido na2o é um número inteiro.')

    except ZeroDivisionError:

        print('Erro! Não é possível dividir o número por ZERO.')

    finally:
        try:
            print(f'O resultado da divisão é: {resultado}')
        
        except NameError:
            print('Finalizando programa..')


divide_numeros()