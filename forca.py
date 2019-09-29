import random




def jogar():
    print("**************")
    print("bem vindo ao jogo de forca!")
    print("**************")


    arquivo = open('palavras.txt', 'r')
    lista_de_palavras = []
    for linha in arquivo:
        lista_de_palavras.append(linha.strip())


    arquivo.close()


    palavra_secreta = lista_de_palavras[random.randrange(0, len(lista_de_palavras))].upper()

    #tamanho_da_palavra_secreta = len(palavra_secreta)


    letras_acertadas = ["_" for l in palavra_secreta]

    print((letras_acertadas))

    tentativas = 5

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("qual a letra?")
        chute = chute.strip().upper()
        if(len(chute) != 1):
            print("escolha apenas uma letra")
            continue

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    print(f'acertou a letra {letra} na posição {index+1}')
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas-=1
            print(f'faltam {tentativas} erros')
        print(letras_acertadas)
        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
    print('fim de jogo')
    if(acertou):
        print('ganhou')
    else:
        print('errou')


if(__name__=="__main__"):
    jogar()