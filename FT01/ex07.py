'''Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
uma mensagem de acordo com o resultado obtido.
'''

distancia = float(input('Introduz a distância percorrida em km: '))
litros = float(input('Introduz a quantidade de litros consumido: '))
consumo = distancia / litros

msg = f'O consumo é de {consumo:.2f} km/l'
if consumo > 10:
    msg += '''
Consumo muito elevado.
(SUVs grandes, veículos desportivos ou condução agressisa em cidade).'''

elif consumo > 8:
    msg += '''
Consumo elevado.
(SUVS médios ou grandes, veículos com motores mais potentes).'''

elif consumo >=6:
    msg += '''
Consumo alto.
(A maioria dos veículos ligeiros convencionais a gasolina ou diesel).'''

elif consumo >= 4:
    msg += '''
Consumo baixo.
(Veículos compactos, híbridos convencionais ou a diesel eficiente em rodovia).'''

else:
    msg += '''
Consumo muito baixo.
(Muito raro, geralmente veículos híbridos plug-in ou extremamente eficientes a diesel)'''

print(msg)