"Peça dois números ao utilizador e trate a divisão por zero."

try:
    num1 = int(input("Digite o numerador:"))
    num2 = int(input("Digite o denominador:"))
    print("Resultado da divisão:", num1 / num2)
except ZeroDivisionError:
    print("Erro: O número não pode ser divido por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos.")