''''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''



def quantidade_de_digitos(inteiro):   # Daria para fazer com if e else também.
    return len(str(inteiro))

inteiro = int(input('Digite um número inteiro: '))
quantidade_digitos = quantidade_de_digitos(inteiro)

print(f'O número {inteiro} possui {quantidade_digitos} dígitos.')