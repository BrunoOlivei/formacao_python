print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if acertou:
        print("Você acertou")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi MAIOR que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi MENOR que o número secreto.")

    rodada = rodada + 1


print("Fim do jogo")
