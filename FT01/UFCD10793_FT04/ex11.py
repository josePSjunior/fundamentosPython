##  Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.

N = int(input("Digite um número inteiro positivo (N):"))

if N > 0:
    soma = 0
    produto = 1
    
    for i in range(1, N + 1): 
        soma += i
        produto *= i
    
    print("A soma dos", N, "primeiros números naturais é:", soma)
    print("O produto dos", N, "primeiros números naturais é:", produto) 
else:
    print("Favor, inserir um número inteiro positivo.")