# Reproduz o seguinte programa.

txt =" uFcd proGRAMação eM pyTHON"

#imprimir texto

print(txt)

#Imprimir Texto sem espaçamento inicial

txt=txt.strip()
print(txt)
#Imprimir frase até à palavra na 13ª posição

print(txt[:13])

#Imprimir últimos 5 caracteres da frase
print(txt[-5:])


#Imprimir frase em maiúsculas

txt=txt.upper()
print(txt)

#Formatação de strings

nome="Sandra Oliveira"

print("O {}")