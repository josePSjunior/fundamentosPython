'''
Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).
'''

horas = int(input('Introduza as Horas: '))
minutos = int(input('Introduza os Minutos: '))
segundos = int(input('Introduza os Segundos: '))
total_segundos = (horas * 3600) + (minutos * 60) + segundos
print(f'{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {total_segundos} segundos.')