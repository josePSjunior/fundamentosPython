## Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média. 

soma = 0
for i in range(1,5):
    numero = int(input(f"Digite o {i}º número: "))
    soma = soma + numero
    
    
print("soma = ", soma)