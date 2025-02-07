## Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média. 

# Função para calcular a média de quatro números
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# Lista para armazenar os números
numeros = []

# Loop para ler quatro números inteiros e positivos
for i in range(4):
    while True:
        try:
            numero = int(input(f"Digite o número inteiro e positivo {i + 1}: "))
            if numero > 0:
                numeros.append(numero)
                break
            else:
                print("Por favor, insira um número positivo.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Calcula a média
media = calcular_media(numeros)

# Devolve a média
print("A média dos números é:", media)
