''''
Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento.
 O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas
 e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo.
 O relatório com as opções de pagamento deve conter os seguintes dados: 
 valor dos juros, valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. 
 A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. 
 No momento, não é necessário formatar os valores.

 Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
 1                       0
 3                       10
 6                       15
 9                       20
 12                      25
 Valor dos Juros Valor Total     Quantidade de Parcelas  Valor da Parcela
 0               R$ 1.000,00     1                       R$  1.000,00
 R$ 100,00       R$ 1.100,00     3                       R$    366,00
 R$ 150,00       R$ 1.150,00     6                       R$    191,67


'''
# Exercicio 02 - AC4.


print(20*"=")
print('\nExercicio 2\n')

def determina_juros(parcelas, divida):
   
    if parcelas == 1:
        return (divida)
        
    elif parcelas == 3:
        return ((3 * divida) / 100)
        
    elif parcelas == 6:
        return ((6 * divida) / 100)
    
    elif parcelas == 9:
       return ((9 * divida) / 100)
    
    elif parcelas == 12:
        return ((12 * divida) / 100)
        
def determina_parcelas(divida):
    opcoes_de_parcela = float(input('\nEm quantas vezes voce deseja parcerlar: '))
    juros = determina_juros(opcoes_de_parcela, divida)
    valor_total = divida + juros
    valor_parcela = valor_total / opcoes_de_parcela
    
    print(f' \nO valor dos juros foram: {juros:.1f}\n')
    print(f' \nO valor total: {valor_total:.1f}\n')
    print(f' \nQuantidade de parcelas: {opcoes_de_parcela:.1f}\n')
    print(f' \nVoce pagara {opcoes_de_parcela:.1f} parcelas de {valor_parcela:.1f}\n')
    
    
divida = float(input('Digite sua divida: '))
determina_parcelas(divida)
    
