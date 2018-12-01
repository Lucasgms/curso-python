import random

def jogar():
    print("********************************")
    print("** Bem vindo ao jogo da Forca **")
    print("********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(arquivo))
    palavra_secreta = palavras[numero_aleatorio].upper()

    letras_corretas = ["for" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_corretas)

    while not enforcou and not acertou:

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0

            for letra in palavra_secreta:
                if chute == letra:
                    letras_corretas[index] = letra
                index += 1
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


if __name__ == "__main__":
    jogar()
