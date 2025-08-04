ganhos_mes = 0
gastos_mes = 0
ganhos_totais = 0
gastos_totais = 0

for mes in range(1, 13):
    ganhos_mes = float(input(f'Digite o ganho no mês {mes}:'))
    gastos_mes = float(input(f'Digite o gasto no mês {mes}:'))
    ganhos_totais += ganhos_mes
    gastos_totais += gastos_mes
saldo = ganhos_totais - gastos_totais
if (saldo) < 0:
    sit_financeira = ('Voçê está no prejuizo')
elif (saldo) > 0:
    sit_financeira = ('Você está no lucro')
print('Resumo do ano\nGanhos totais: {}\nGastos totais: {} \nSaldo: {}\nSituação financeira: {}'.format(ganhos_totais, gastos_totais, saldo, sit_financeira))
