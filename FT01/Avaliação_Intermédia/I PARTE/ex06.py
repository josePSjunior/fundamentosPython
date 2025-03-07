"Elabora uma script em python que peça ao utilizador dois números e devolva a divisão do"
"primeiro número introduzido pelo seguinte. Trate erros como divisão por zero e valores inválidos."

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    print("O resultado da divisão é: ", numero1 / numero2)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Insira valores numéricos válidos.")
