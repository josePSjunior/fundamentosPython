## Escreve um programa para escrever no ecrã a palavra olá 100 vezes.

i = 1
soma = 0

valor = int(input("Digite um valor: "))

while i <= valor:
    soma = soma + i
    i += 1
    
print(f'Sim of all numbers till {valor} is', soma)