## Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na forma numérica.

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

num_mes = int(input("Introduza o número do mês (1-12): "))
if 1 <= num_mes <= 12:
    print(" O mês é: ", meses[num_mes - 1])
else:
    print("Mês inválido. Por favor, insira um número entre 1 e 12.")
