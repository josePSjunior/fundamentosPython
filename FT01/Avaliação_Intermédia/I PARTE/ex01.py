"Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada"

try:
    num = int(input("Por favor, insira um número inteiro:"))
    print("O número que você digitou foi:", num)
except ValueError:
    print("Erro: O número deve ser inteiro")