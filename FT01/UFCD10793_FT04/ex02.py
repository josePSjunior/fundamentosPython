## Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de uma pessoa.

estado_civil = ["solteiro", "casado", "viúvo"]

est_civ = input("Digite o estado civil (S, C ou V): ")
if est_civ == "S":
    print("Estado civil: ", estado_civil[0])
elif est_civ == "C":
    print("Estado civil: ", estado_civil[1])
elif est_civ == "V":
    print("Estado civil: ", estado_civil[2])
else:
    print("Estado civil não encontrado")