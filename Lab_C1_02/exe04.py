temp_seg = int(input('Digite o tempo de duração da tarefa em segundos:'))
horas = temp_seg // 3600
resto = temp_seg % 3600
minutos = resto // 60
segundos = resto % 60
print('O tempo de duração desta tarefa foi de {} hr, {} min, e {} seg'.format(horas, minutos, segundos))