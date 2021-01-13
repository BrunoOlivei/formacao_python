import forca
import adivinhacao

print("********************************")
print("******Escolha o seu jogo!*******")
print("********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo? "))

if jogo == 1:
    print("Iniciando jogo da Forca")
    forca.jogar()
else:
    print("Iniciando jogo de Adivinhação")
    adivinhacao.jogar()

