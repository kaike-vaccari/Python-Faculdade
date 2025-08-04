codigo = int(input('Digite o código do pedido:'))
quantidade = int(input('Digite a quantidade:'))
c100 = ['Cachorro-quente', 1.20]
c101 = ['Bauru simples', 1.30]
c102 = ['Bauru com ovo', 1.50]
c103 = ['Hambúrguer', 1.20]
c104 = ['Cheeseburguer', 1.30]
c105 = ['Refrigerante', 1.00]
if codigo == 100:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c100[0], quantidade * c100[1]))
elif codigo == 101:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c101[0], quantidade * c101[1]))
elif codigo == 102:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c102[0], quantidade * c102[1]))
elif codigo == 103:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c103[0], quantidade * c103[1]))
elif codigo == 104:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c104[0], quantidade * c104[1]))
elif codigo == 105:
    print('Pedindo {} {}, você irá pagar R${:.2f}'.format(quantidade, c105[0], quantidade * c105[1]))
else:
    print('Código inválido')