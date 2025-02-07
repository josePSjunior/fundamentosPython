## Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número introduzido pelo utilizador.

tab = int(input("Introduza um número: "))
for i in range(1, 11):
    print(f"{tab} x {i} = {tab * i}")