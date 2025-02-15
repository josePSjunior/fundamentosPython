## Escreva um programa que solicite ao altilizador dois números inteiros a operação
## matemática a ser realizada (+, -, *, /).

import match

num1: float(input("Digite o primeiro número: "))
num2: float(input("Digite o segundo número: "))

operacao = str(input("Escolha a operação (+,-,*,/): "))

match operacao:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print ("Não é possível dividir por zero!")
        else:
            print(num1 / num2)
    case _:
        print("Operação inválida. Por favor, escolha uma das opções acima")