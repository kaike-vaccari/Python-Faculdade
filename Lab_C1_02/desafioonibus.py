passagem = 5.00
diesel = 5.95

onibus = [
    {'nome': 'Ônibus 1', 'cap': 65, 'cons': 11, 'manut': 80},
    {'nome': 'Ônibus 2', 'cap': 55, 'cons': 14, 'manut': 60},
    {'nome': 'Ônibus 3', 'cap': 80, 'cons': 17, 'manut': 45}
]

itinerarios = [
    {'nome': 'Itinerário 1', 'km': 40, 'pass': 790},
    {'nome': 'Itinerário 2', 'km': 43, 'pass': 1200},
    {'nome': 'Itinerário 3', 'km': 68, 'pass': 835}
]

for b in onibus:
    for i in itinerarios:
        v = -(-i['pass'] // b['cap'])  # viagens (arredondar pra cima)
        dist = v * i['km']
        litros = dist / b['cons']
        custo = litros * diesel + b['manut']
        receita = i['pass'] * passagem
        lucro = receita - custo
        print(f"{b['nome']} - {i['nome']}")
        print(f"1. Custo diário: R${custo:.2f}")
        print(f"2. Lucro diário: R${lucro:.2f}")
        print(f"3. Viagens por dia: {v}")
        print(f"4. Litros por dia: {litros:.2f}\n")
