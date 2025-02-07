## Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média dos números introduzidos.

numeros = []

for i in range(20):
    numero = float(input(f"Introduza o número real {i+1}: "))
    numeros.append(numero)
    
soma = sum(numeros)
media = soma / len(numeros)
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")