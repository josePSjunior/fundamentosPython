#a) Armazene as diferentes datas numa string;
dates = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
#b) Imprima as datas correspondentes ao ano de 2022;
date_list = dates.split(",")
print(date_list)
for x in date_list:
    if x[-4:] == '2022':
        print(x)
output = [x for x in date_list if x[-4:] == '2022']
print(output)
#c) Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
days = []
for x in date_list:
    days.append(int(x[:2]))
print(days)
days_sorted = sorted(days)
print(days_sorted)