"Cria ou faz download de um ficheiro CSV. De seguida cria um programa" 
"que leia o ficheiro CSV e mostre cada linha do mesmo. "

import csv

with open("equipes.csv", "w", newline="") as ficheiros_csv:
    escritor = csv.writer(ficheiros_csv)
    
    escritor.writerow(["Nome", "Lugar" "Idade"])
    
    escritor.writerow(["Pedro", "Aveiro", "40"])
    escritor.writerow(["Carlos", "Faro", "20"])
    escritor.writerow(["Julia", "Braga", "27"])
    
    