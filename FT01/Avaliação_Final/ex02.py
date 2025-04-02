# Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra. 

def contar_vogais(palavras):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in palavras:
        if letra in vogais:
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")
print(f"Número de vogais em '{palavra}': {contar_vogais(palavra)}")        