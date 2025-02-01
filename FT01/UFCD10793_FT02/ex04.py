## Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma:
## “A média das notas [nota1] e [nota2] é [média].”

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2
print("A média das notas", nota1, "e", nota2, "é", media)
