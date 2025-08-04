idade_dias = int(input('Digite quantos dias de vida você tem:'))
ano = idade_dias // 365
resto = idade_dias % 365
mes = resto // 30
dias = resto % 30
print('Você ja vivel {} anos, {} meses e {} dias'.format(ano, mes, dias))