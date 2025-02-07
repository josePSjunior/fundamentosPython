## Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar 
## a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
## Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma mensagem personalizada. 
## Para os restantes casos, mostra no ecrã o resultado da operação desejada.

operacao = input("Escolha a operação (+,-,*,/): ")

if operacao in ['+', '-', '*', '/']:
    num1 = float(input("Insira o primeiro valor: "))
    num2 = float(input("Insira o segundo valor: "))
    if operacao == '+':
        soma = num1 + num2
        print("%s+%s=%s"%(num1,num2,soma))
    elif operacao == '-':
        subtracao = num1 - num2
        print("%s-%s=%s"%(num1,num2,subtracao))
    elif operacao == '*':
        multiplicacao = num1 * num2
        print("%s*%s=%s"%(num1,num2,multiplicacao))
    else:
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            divisao = num1 / num2
            print("%s/%s=%s"%(num1,num2,divisao))
else:
    print("Operação inválida!")  # Caso o utilizador insira uma oper
