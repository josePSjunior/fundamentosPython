"Escreve um programa que receba três números reais e indique qual o maior dos três números. "

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
elif num2 == num1 and num2 == num3:
    print("Os três números são iguais")
else:
    print(f"O maior número é {num3}")