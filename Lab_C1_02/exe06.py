real = float(input('Digite um valor em real:R$'))
x12 = real / 12 #parcela em 12 vezes
x24 = real / 24 #parcela em 24 vezes
x36 = real / 36 #parcela em 36 vezes
px12 = x12 * 1.4/100 #porcentagem aplicada a parcela x12
px24 = x24 * 1.4/100
px36 = x36 * 1.4/100
for i1 in range(1, 13):
    x12 += px12
for i2 in range(1, 25):
    x24 += px24
for i3 in range(1, 37):
    x36 += px36
print('Parcelando o valor R${:.2f} em 12x fica R${:.2f}, em 24x fica R${:.2f} e em 36x fica R${:.2f}.\nOBS:Valor de cada parcela'.format(real, x12, x24, x36))

