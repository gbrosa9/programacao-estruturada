#def media(ap1, ap2, ac):
'''
Faça uma funçãocmedia(), que recebe os parâmetros posicionais ap1, ap2 e ac  e retorne a média de avaliações, utilizando a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.

'''
  #  return (ap1 + ap2) * 0.4 + ac * 0.2

#def main():
   # print(media(8,8,10))

#main()


# ---------------------------------------------------------------------------------------------------------------- #

# Exercicio 2


def m_para_cm(comp_m):
    # metro para cm

   return comp_m * 100





# Exercicio 3 

def raio(tam_raio):
    pi = 3.14
    area =  pi * tam_raio **2
    return area * tam_raio


# Exercicio 4

def fahr_para_celcius(fahrenheit):
    '''Conversor de temperatura de Fahrenheit para Celcius -> Onde C / 5 = F ( - 32) / 9'''
    return 5 * (fahrenheit - 32) / 9

def main():
    print(raio(4.5))
    print(m_para_cm(4.5))
    print(fahr_para_celcius(183))

main()