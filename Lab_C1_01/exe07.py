nome = input('Digite o seu nome:')
sexo = input('Digite o seu sexo(masculino ou feminino):')
peso = float(input('Digite o seu peso em kg:'))
altura = float(input('Digite a sua altura em metros:'))
imc = peso / altura ** 2
if imc < 18.5:
    estcritico = 'Abaixo do peso' #estado crítico
elif imc >= 18.5 and imc < 25:
    estcritico = 'Peso ideal(parabéns)'
elif imc >= 25 and imc < 30:
    estcritico = 'Levemente acima do peso'
elif imc >= 30 and imc < 35:
    estcritico = 'Obesidade grau 1'
elif imc >= 35 and imc < 40:
    estcritico = 'Obesidade grau 2(severa)'
else:
    estcritico = 'Obesidade grau 3(mórbida)'
if sexo == 'masculino':
   pideal =  72.7*altura-58 #peso ideal
elif sexo == 'feminino':
   pideal = 62.1*altura-44.7
else:
    print('Digite um sexo valido')
print('{} seu peso ideal é {:.2f}, o seu IMC é {:.2f}, e o seu estado crítico é {}.'.format(nome, pideal, imc, estcritico))
