"Ler o ficheiro CVS"

import csv

with open("equipes.csv", "r") as ficheiro_csv:
    leitor = csv.reader(ficheiro_csv)
    for linha in leitor:
        print(linha)