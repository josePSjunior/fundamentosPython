## escreva um programa que receba o nome de um produto e seu preço, e retorne o preço total
## considerando os descontos seguintes:
## 1. se o produto for um smartphone, será aplicado um desconto de 10%.
## 2. se o produto for um tablet, será aplicado um desconto de 15%.
## 3. se o produto for um laptop, será aplicado um desconto de 20%.
## 4. para qualquer outro produto, não haverá desconto.

codprod = input("Qual é o produto?:")
valor = float(input("Qual é o valor do produto? R$: "))

match codprod:
    case "smartphone":
         print(f"Foi aplicado um desconto de {valor * 0.1} (10%) O valor a ser pago é: {valor - valor * 0.1}")
    case "tablet":
        print(f"Foi aplicado um desconto de {valor * 0.15} (15%) O valor a ser pago é: {valor - valor * 0.15}")
    case "laptop":
        print(f"Foi aplicado um desconto de {valor * 0.2} (20%) O valor a ser pago é: {valor - valor * 0.2}")
    case _:
        print("O produto selecionado não tem desconto associado, ovalor a ser pago é: ", valor)