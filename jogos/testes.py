def jogarForca():
    print("----------------------------")
    print ("Bem vinde ao jogo de Forca")
    print("----------------------------")

    palavra_secreta = "Obisidiana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        print("Continue jogando por favor")
        chute = input("Digite uma letra")
        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                print("Encotrei a letra {} na posição {}".format(letra,index))
            index = index + 1



if(__name__== "__main__"):
        jogarForca()

