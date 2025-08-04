fabrica = float(input('Digite o custo de fabrica do carro:'))
distribuidor = fabrica * 0.28
imposto = fabrica * 0.45
valor_carro = fabrica + distribuidor + imposto
print('O valor final do carro é de R${}'.format(valor_carro))