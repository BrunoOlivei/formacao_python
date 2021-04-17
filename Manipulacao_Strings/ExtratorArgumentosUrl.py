class ExtratorArugmentosUrl:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL Inválida!!!")

    @staticmethod
    def url_valida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def retorna_moedas(self):
        busca_moeda_origem = "moedaorigem=".lower()
        busca_moeda_destino = "moedadestino=".lower()

        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
            final_substring_moeda_origem = self.url.find("&")
            moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

        inicio_substring_moeda_destino = self.encontra_indice_inicio_substring(busca_moeda_destino)
        final_substring_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[inicio_substring_moeda_destino:final_substring_moeda_destino]

        return moeda_origem, moeda_destino

    def encontra_indice_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extrai_valor(self):
        busca_valor = "valor=".lower()
        inicio_substring_valor = self.encontra_indice_inicio_substring(busca_valor)
        valor = self.url[inicio_substring_valor:]
        return valor
