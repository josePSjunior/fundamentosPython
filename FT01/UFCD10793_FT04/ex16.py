## Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número
## fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

num = int(input("Insira um número entre 0 e 10: "))

if 0 <= num <= 10:
    print("Você inseriu:", num)
else:
    print("Número fora do intervalo. O programa será encerrado.")