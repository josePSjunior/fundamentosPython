## Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N) em que N é um número introduzido
## utilizador (NOTA: este programa poderia ser feito utilizando a fórmula da progressão aritmética,
## S = (1+N) * N/2, mas faz de conta que não sabíamos a fórmula).

N = int(input("Introduza um número inteiro positivo (N): "))
if N > 0:
    soma = 0
    for i in range(1, N + 1):
        soma += i
    print("A soma dos", N, "primeiros números naturais é:", soma)   
else:
    print("Por favor, insira um número inteiro positivo.")
