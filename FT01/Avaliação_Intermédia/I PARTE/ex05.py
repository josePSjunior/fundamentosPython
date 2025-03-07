"Elabora uma script em python que peça ao utilizador um número e some todos os números de 1"
"até esse mesmo número. Deves utilizar o tratamento de erros."

try:
    num = int(input("Digite um número inteiro: "))
    if num < 1:
        print("Erro: Por favor insira um número inteiro positivo.")
    else:
        soma = sum(range(1, num + 1))
    print(f"A soma de todos os números de 1 até {num} é {soma}.")
except ValueError:
    print("Erro: Apenas números inteiros são aceitos.")