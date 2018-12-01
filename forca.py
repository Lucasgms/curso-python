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
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_corretas
        index = index + 1

        print(letras_corretas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

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

    numero_aleatorio = random.randrange(0, len(arquivo))
    palavra_secreta = palavras[numero_aleatorio].upper()

    return palavra_secreta


def inicializa_letras_corretas(palavra):
    return ["for" for letra in palavra]


def solicita_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute


def monta_palavra_correta(palavra, chute, letras_corretas):
    index = 0

    for letra in palavra:
        if chute == letra:
            letras_corretas[index] = letra
        index += 1

    return letras_corretas


if __name__ == "__main__":
    jogar()
