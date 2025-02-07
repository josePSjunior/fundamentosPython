## Elabora um programa que pede ao utilizador para inserir dois números inteiros. O programa deve
## escrever todos os números inteiros entre os dois limites por ordem crescente. Utiliza o ciclo for

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i)   
else:
    print("Insira números inteireos válidos para continuar o programa.")