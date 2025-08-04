nota1 = float(input('Digite uma nota'))
nota2 = float(input('Digite outra nota'))
nota3 = (nota1+nota2)/2
if nota3 < 6:
 print('Reprovado')
elif nota3 >= 6 and nota3 < 7:
    print('Estudar mais')
elif nota3 >= 7 and nota3 < 9:
    print('Fazer mais exercícios')
else:
 print('Parabéns! Ótima nota')
