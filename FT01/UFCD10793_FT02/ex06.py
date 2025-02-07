## Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a
## converta para grau Celsius (C), devolvendo o resultado da conversão.

"Use a fórmula: C = 5 * ((F-32) / 9)."

grauF = float(input("Insira a temperatura em Fahrenheit: "))
grauC = 5 * ((grauF - 32) / 9)
print(f"A temperatura em Celsius é: {grauC:.2f}")  # Mostra