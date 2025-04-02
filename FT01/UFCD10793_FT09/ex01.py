# Considera o seguinte dicionário, a que cada prato é associado o respetivo 
# valor em euros: 

menu={ 
    "entremeada": 7, 
    "Sardinha": 6, 
    "Filetes": 5.5, 
    "Prego": 7, 
    "Hamburguer": 5.5 
} 
#a. Devolva o preço do “prego”. 
p_prego = menu.get("Prego")
print("O preço do Prego é: ", p_prego)

#b. Faça o print de todas as chaves do dicionário 
print (menu.keys())

#c. Acrescente na lista “omolete” com o preço de 5. 
menu.update({"Omelete": 5})

#d. Faça o print de todo o dicionário, para visualizar as alterações.
for x, y in menu.items():
    print(x, y)