anos = int(input('Quantos anos você tem?:'))
mes = int(input('Digite os meses além dos anos:'))
dias = int(input('Digite os dias além dos meses:'))
idade_dias = anos*365 + mes*30 + dias
print('Você ja viveu {} dias'.format(idade_dias))
