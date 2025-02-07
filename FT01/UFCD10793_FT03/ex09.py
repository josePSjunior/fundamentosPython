## O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
## Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, de seguida, 
## calcule e mostre o resultado do seu IMC e classifique esse resultado de acordo com as seguintes condições:
## • IMC<17 - Muito abaixo do peso ideal
## • 17<=IMC<18,5 - Abaixo do peso
## • 18,5<=IMC<25 - Peso normal
## • 25<=IMC<30 - Acima do peso
## • 30<=IMC<35 - Obesidade I
## • 35<=IMC<40 - Obesidade II (severa)
## • IMC>=40 - Obesidade III (mórbida)
" Nota: IMC=massa/(altura*altura)"

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura * altura)
print(f"IMC: {imc:.2f}")
if imc < 17:
    print("Muito abaixo do peso ideal")
elif 17 <= imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Acima do peso")
elif 30 <= imc < 35:
    print("Obesidade I")
elif 35 <= imc < 40:
    print("Obesidade II (severa)")
    
else: print("Obesidade III (mórbida)")

