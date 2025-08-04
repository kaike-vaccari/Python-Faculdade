idade = int(input('Digite a idade do nadador:'))
if idade < 8 and idade > 4:
    print('Infantil A')
elif idade < 11 and idade > 7:
    print('Infantil B')
elif idade < 14 and idade > 10:
    print('Juvenil A')
elif idade < 18 and idade > 13:
    print('Juvenil B')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade insuficiente')