
def encontra_vogais(palavra):
    palavra = input("Digite uma palavra que você deseja separar as vogais:")
    vogais = ['a', 'e', 'i', 'o', 'u']
    letras_encontradas = []
    for letra in palavra:
        if letra in vogais:
            if letra not in letras_encontradas:
                letras_encontradas.append(letra)
    for vogal in letras_encontradas:
        return print(vogal)
