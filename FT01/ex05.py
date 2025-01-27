'''
Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor da hipotenusa (deverá ser criado o ficheiro ex05.py).
'''
from math import sqrt

cateto1 = float(input('Digite o valor do cateto 1: '))
cateto2 = float(input('Digite o valor do cateto 2: '))
hipotenusa = sqrt(cateto1**2 + cateto2**2)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')
