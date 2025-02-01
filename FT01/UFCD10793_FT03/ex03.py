## Escreve um programa que solicite um número inteiro ao utilizador e verifique se o 
## mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;

## "O número [número] é [par/ímpar]"

num = int(input("Insira um número: \t"))

if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")