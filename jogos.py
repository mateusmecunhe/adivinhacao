import adivinhacao
import forca

print('*************')
print('Qual jogo você quer jogar?')
print('*************')
escolha = int(input("1 - adivinhação; 2- forca"))

if escolha == 1:
    adivinhacao.jogar()
if escolha == 2:
    forca.jogar()
