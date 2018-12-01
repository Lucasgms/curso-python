import random


def jogar():

    imprime_mensagem_inicial()
    palavra_secreta = buscar_palavra_secreta()
    letras_corretas = inicializa_letras_corretas(palavra_secreta)

    print(letras_corretas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = solicita_chute()

        if chute in palavra_secreta:
            letras_corretas = monta_palavra_correta(chute, palavra_secreta, letras_corretas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_corretas

        print(letras_corretas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo!")


def imprime_mensagem_inicial():
    print("********************************")
    print("** Bem vindo ao jogo da Forca **")
    print("********************************")


def buscar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()

    return palavra_secreta


def inicializa_letras_corretas(palavra):
    return ["_" for letra in palavra]


def solicita_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute


def monta_palavra_correta(chute, palavra, letras_corretas):
    index = 0

    for letra in palavra:
        if chute == letra:
            letras_corretas[index] = letra
        index += 1

    return letras_corretas


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
