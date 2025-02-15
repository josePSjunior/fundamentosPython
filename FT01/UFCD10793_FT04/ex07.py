## Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N) em que N é um número introduzido
## utilizador (NOTA: este programa poderia ser feito utilizando a fórmula da progressão aritmética,
## S = (1+N) * N/2, mas faz de conta que não sabíamos a fórmula).

N = input("Introduza um número natural: ")

while not N.isdigit():
    print("O número introduzido não é valido")
    N = input("Introduza um número natural: ")
    
N = int(N)

soma = 0
for i in range(1, N+1):
    soma = soma + i

print("soma =", soma)