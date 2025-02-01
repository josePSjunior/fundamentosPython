## Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja 
## maior que 20, devolva o resultado da sua divisão por 2.

import math

nint = int(input("Digite um número inteiro: \t"))

if nint > 20:
    
    nint = nint / 2
    
    print("o resultado da divisão do seu número por 2 é:", round(nint, 1))

else: print("O número indicado é inferior a 20")