## Escreve um programa que solicite ao utilizador um número e escreva em simultâneo a sequência
## crescente e decrescente entre 1 e esse número.
## Apresentação no ecrã:
##1 5
##2 4
##3 3
##4 2
##5 1

N = int(input("digite um número:"))

if N > 0:
    for i in range(1, N + 1):
        print(i, N - i + 1)

else:
    print("número inválido")