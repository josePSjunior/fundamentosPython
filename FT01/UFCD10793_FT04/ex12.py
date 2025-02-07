##  Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N sabendo que: n!=1*2*3*…*n.

N = int(input("Digite um número inteiro positivo: "))

if N >= 0:
    fatorial = 1
    for i in range(1, N + 1):
        fatorial *= i
    print(f"O fatorial de {N} é {fatorial}")

else:
    print("Número inválido. Por favor, digite um número inteiro positivo.")