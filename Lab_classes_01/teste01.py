class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem):
        print(self.nome + ' diz: ' + mensagem)

pessoa1 = Pessoa('João', 30)
pessoa1.falar('Olá, tudo bem?')