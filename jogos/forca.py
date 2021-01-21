from random import randrange


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Forca!")
    print("********************************")

    with open("palavras.txt", "r", encoding='UTF-8') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
            print("Você errou. Faltam {} tentativas".format(6-erros))

        if erros == 6:
            break
        if "_" not in letras_acertadas:
            break
        print(letras_acertadas)

    if "_" not in letras_acertadas:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
