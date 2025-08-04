real = float(input('Digite um valor em reais:'))
dolar = real / 5.85
euro = real / 6.60
libras = real / 7.65
print('Com ${} reais, você consegue comprar\nDolares americanos: ${:.2f}\nEuro: ${:.2f}\nLibras Esterlinas: ${:.2f}'.format(real, dolar, euro, libras))
