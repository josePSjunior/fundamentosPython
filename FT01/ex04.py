'''
Escrever um programa que calcule o volume de uma esfera. O valor do raio deverá ser introduzido pelo ultilizador (deverá ser criado o ficheiro ex04.py).
'''
from math import pi as PI

raio = float(input('Introduza o valor do raio da esfera: '))
volume = (4/3) * PI * (raio ** 3)
print(f'O volume da esfera é {volume:.2f}')  