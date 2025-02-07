" Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo."

num = float(input("introduza um número:"))
if num == 0:
    print("O número é nulo.")
elif num > 0:
    print("O número é positivo.")
else: print("O número é negativo.")