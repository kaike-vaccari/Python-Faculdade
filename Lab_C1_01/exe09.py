porcentagem01 = 145
porcentagem02 = 135
porcentagem03 = 125
salario_min = float(1518)
salario = float(input('Digite o seu salário líquido'))
if salario < salario_min*2:
    salario_r = salario * (porcentagem01 / 100)  # salario reajustado
elif salario < salario_min*5:
    salario_r = salario * (porcentagem02 / 100)
else:
    salario_r = salario * (porcentagem03 / 100)
print(salario_r)
