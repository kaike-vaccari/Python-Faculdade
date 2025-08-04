senha = "1234"
leitura = ""
tentativas = 0
max_tentativas = 3

while leitura != senha and tentativas < max_tentativas:
    leitura = input("Digite a senha: ")
    if leitura != senha:
        tentativas += 1
        print("Senha incorreta. Tente novamente")

if tentativas == max_tentativas:
    print("Numero máximo de tentativas. Acesso negado")

if leitura == senha:
    print("Acess Permited")