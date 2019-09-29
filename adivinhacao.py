import random

def jogar():
    print('******************')
    print('bem vindo ao jogo de adivinhação!')
    print('******************')

    numero_secreto = random.randrange(1, 101)


    print(numero_secreto)

    contador = 1
    quantidade_de_tentativas = int(input('de quantas rodadas vc precisa?'))

    """while (contador <= quantidade_de_tentativas):
        chute_str = input('tente adivinhar: ')
        chute_int = int(chute_str)
        if (chute_int == numero_secreto):
            print('acertou')
            break
        else:
            if (chute_int > numero_secreto):
                print('alto demais')
            elif (chute_int < numero_secreto):
                print('baixo demais')
            quantidades_restantes = quantidade_de_tentativas - contador
            print('faltam {} de um total de {} tentativas'.format(quantidades_restantes, quantidade_de_tentativas))
        contador = contador + 1
    
    print('fim do jogo')"""

    for contador in range(quantidade_de_tentativas):
        chute = int(input('tente adivinhar o número entre 1 e 100: '))

        if(chute < 1 or chute > 100):
            print("número inválido")
            continue

        if(chute == numero_secreto):
            print('acertou')
            break
        else:
            if(chute < numero_secreto):
                print('baixo demais')
            elif(chute>numero_secreto):
                print('alto demais')
            contador += 1
            quantidades_restantes = quantidade_de_tentativas - contador
            print(f'faltam {quantidades_restantes} de um total de {quantidade_de_tentativas} tentativas')


    print("fim do jogo")

if(__name__=="__main__"):
    jogar()