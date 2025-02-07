## Num ficheiro diferente dos utilizados nas alíneas anteriores, escreve um programa que
## faça a conversão para kms, de um dado valor em metros.

metros = float(input("insira quantidade de metros percorridos:"))

km = (metros / 1000) * 1

print(f'{metros} metros equivalem a {km} km')