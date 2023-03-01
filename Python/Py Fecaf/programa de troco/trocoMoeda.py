nome = input('Olá seja bem vindo, por favor digite seu nome:')

# Lê o valor da mercadoria e o valor pago pelo cliente
valor_mercadoria = float(input(f"{nome} por favor digita o valor da mercadoria: R$ "))
valor_pago = float(input(f"{nome} agora digite valor pago: R$ "))

# Calcula o troco
troco = valor_pago - valor_mercadoria

# Verifica se há troco a ser devolvido
if troco < 0:
    print(f"{nome} Faltam R$ {abs(troco):.2f}!")
elif troco == 0:
    print(f"{nome} Não existe troco!")
else:
    print(f"{nome} o valor do Troco: R$ {troco:.2f}")
    notas_moedas = {100: "nota(s) de R$ 100,00", 
                    50: "nota(s) de R$ 50,00",
                    20: "nota(s) de R$ 20,00",
                    10: "nota(s) de R$ 10,00",
                    5: "nota(s) de R$ 5,00",
                    2: "nota(s) de R$ 2,00",
                    1: "moeda(s) de R$ 1,00",
                    0.50: "moeda(s) de R$ 0,50",
                    0.25: "moeda(s) de R$ 0,25",
                    0.10: "moeda(s) de R$ 0,10",
                    0.05: "moeda(s) de R$ 0,05",
                    0.01: "moeda(s) de R$ 0,01"}
    notas_moedas_devolver = {}
    for valor in sorted(notas_moedas.keys(), reverse=True):
        qtd_notas_moedas = int(troco // valor)
        if qtd_notas_moedas > 0:
            notas_moedas_devolver[valor] = qtd_notas_moedas
            troco -= qtd_notas_moedas * valor
    for valor, descricao in notas_moedas_devolver.items():
        print(f"{descricao}: {valor * descricao}")
