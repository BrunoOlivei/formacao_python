joao_do_frete = 0
maria_da_pamonha = 0
ze_da_farmacia = 0
voto_nulo_vereador = 0
dr_zureta = 0
sr_gomes = 0
voto_nulo_prefeito = 0

print("_______BEM VINDO AO SISTEMA DE PESQUISA ELEITORAL_______\n")
print("________________________________________________________\n")
print("_____________Escolha uma das opções abaixo:_____________\n")
print("1- Vote para Prefeito e Vereador\n"
      "2 - Apurar Votos\n"
      "3 - Sair\n")
print("________________________________________________________")
opcao = int(input("Digite o número da sua opção: "))

while opcao != 3:
    if opcao == 1:
        print("_______________________VEREADORES:______________________")
        print("111 - Vereador Joao do Frete")
        print("222 - Vereador Maria da Pamonha")
        print("333 - Vereador Ze da Farmacia")
        print("444 - Voto Nulo")
        print("________________________________________________________")
        voto_vereador = int(input("Digite o número do vereador escolhido: "))
        print("________________________________________________________")
        if voto_vereador == 111:
            joao_do_frete = joao_do_frete + 1
        elif voto_vereador == 222:
            maria_da_pamonha = maria_da_pamonha + 1
        elif voto_vereador == 333:
            ze_da_farmacia = ze_da_farmacia + 1
        elif voto_vereador == 444:
            voto_nulo_vereador = voto_nulo_vereador + 1
        print("_______________________PREFEITOS:______________________")
        print("11 - Prefeito Dr. Zureta")
        print("22 - Prefeito Senhor Gomes")
        print("44 - Voto Nulo")
        print("_______________________________________________________")
        voto_prefeito = int(input("Digite o número do vereador escolhido: "))
        print("_______________________________________________________")
        if voto_prefeito == 11:
            dr_zureta = dr_zureta + 1
        elif voto_prefeito == 22:
            sr_gomes = sr_gomes + 1
        elif voto_vereador == 44:
            voto_nulo_prefeito = voto_nulo_prefeito + 1

    elif opcao == 2:
        print("___________________APURAÇÃO DOS VOTOS___________________")
        print("_______________________PREFEITOS:______________________")
        total_prefeitos = dr_zureta + sr_gomes + voto_nulo_prefeito
        print(f'11 - Prefeito Dr. Zureta: {round((dr_zureta/total_prefeitos)*100, 2)}%')
        print(f'22 - Prefeito Senhor Gomes: {round((sr_gomes / total_prefeitos) * 100, 2)}%')
        print(f'44 - Votos Nulos: {round((voto_nulo_prefeito / total_prefeitos) * 100, 2)}%')
        print("_______________________________________________________")
        print(f"Total de votos: {total_prefeitos}.")
        print("_______________________________________________________")
        print("_______________________VEREADORES:______________________")
        total_vereadores = joao_do_frete + maria_da_pamonha + ze_da_farmacia + voto_nulo_vereador
        print(f'111 - Vereador João do Frete: {round((joao_do_frete / total_vereadores) * 100, 2)}%')
        print(f'222 - Vereador Maria da Pamonha: {round((maria_da_pamonha / total_vereadores) * 100, 2)}%')
        print(f'333 - Vereador Ze da Farmacia: {round((ze_da_farmacia / total_vereadores) * 100, 2)}%')
        print(f'44 - Votos Nulos: {round((voto_nulo_vereador / total_vereadores) * 100, 2)}%')
        print("_______________________________________________________")
        print(f"Total de votos: {total_vereadores}.")

    print("_______BEM VINDO AO SISTEMA DE PESQUISA ELEITORAL_______")
    print("________________________________________________________")
    print("_____________Escolha uma das opções abaixo:_____________")
    print("1- Vote para Prefeito e Vereador\n"
          "2 - Apurar Votos\n"
          "3 - Sair\n")
    print("________________________________________________________")
    opcao = int(input("Digite o número da sua opção: "))

