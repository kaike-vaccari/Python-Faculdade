class Carro:
    def __init__(self, marca, cor, preco):
        self.marca = marca
        self.cor = cor
        self.preco = preco

    def Ligar(self):
        print('Ligando o carro...')

    def Buzinar(self):
        print('biiiiiiiit!!! biiiiiiiit!!!')

    def Desligar(self):
        print('Desligando o carro...')

    def Exibir_informacoes(self):
        print(self.marca, self.cor, self.preco)

carro1 = Carro('Mercedes', 'preto', 20000)
carro2 = Carro('Xevrolet', 'Branco', 50000)
carro3 = Carro('BMW', 'prata', 100000)

carro3.Exibir_informacoes()
carro1.Ligar()
carro1.Buzinar()
carro1.Desligar()