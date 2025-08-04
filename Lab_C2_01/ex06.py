# 6. Crie uma função chamada media() que recebe três notas e imprime a média
nota1 = 0
nota2 = 0
nota3 = 0
def media():
    nota1 = int(input('Digite uma nota:'))
    nota2 = int(input('Agora digite uma nota:'))
    nota3 = int(input('Digite a ultima:'))
    media1 = (nota1 + nota2 + nota3) / 3
    print('A média dos 3 números é {:.2f}'.format(media1))
media()