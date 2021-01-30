class Data:

    def __init__(self):
        data = input('Digite a data de nascimento: ')
        data_formatada = data.split("/")
        dia = int(data_formatada[0])
        mes = int(data_formatada[1])
        ano = int(data_formatada[2])

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime_data(self):
        if self.dia < 10:
            print(f'0{self.dia}/{self.mes}/{self.ano}')
        else:
            print(f'{self.dia}/{self.mes}/{self.ano}')
