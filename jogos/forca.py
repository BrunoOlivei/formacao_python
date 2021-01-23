from random import randrange


def jogar():
    mensagem_inicio_jogo()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_campos_letras_palavra(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute_do_jogador()

        if chute in palavra_secreta:
            coloca_letra_acertada_local_certo(chute, letras_acertadas, palavra_secreta)
        else:
            erros +=1
            desenha_forca(erros)

        if erros == 7:
            break
        if "_" not in letras_acertadas:
            break
        print(letras_acertadas)

    if "_" not in letras_acertadas:
        imprime_mensagem_vitoria(palavra_secreta)
    else:
        imprimi_mensagem_derrota(palavra_secreta)


def mensagem_inicio_jogo():  # Mensagem que mostra o início do jogo
    print("********************************")
    print("Bem vindo ao jogo de Forca!")
    print("********************************")


def carrega_palavra_secreta():  # Carrega palavra secreta e prepara ela a partir de um arquivo
    with open("palavras.txt", "r", encoding='UTF-8') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_campos_letras_palavra(palavra):  # Cria os campos com _ a partir do número de letras
    return ["_" for letra in palavra]


def pede_chute_do_jogador():  # Input pedindo letra de tentativa
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute


def coloca_letra_acertada_local_certo(chute, letras_acertadas, palavra_secreta):  # coloca letra acertada no lugar
    # correto
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1


def imprime_mensagem_vitoria(palavra_secreta):  # Mensagem de vitória caso jogador ganhe
    print("Parabéns, você ganhou!")
    print("Você acertou a palavra {}".format(palavra_secreta))
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


def imprimi_mensagem_derrota(palavra_secreta):  # Mensagem de derrota caso o jogador use todas as tentavias e não
    # acerte a palavra
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

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
