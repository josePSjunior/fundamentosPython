# Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para três variáveis inteiras. 

data = input("Digite a data em formato DD/MM/AAAA: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")