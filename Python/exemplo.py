nome = input('Olá seja bem vindo(a), digite seu nome: \n')
peso = float(input(f'por favor {nome} digite seu peso: '))

if peso <= 30.5 and 40.90:
    print(f"{nome} Você está abaixo do peso")
    print("Você precisa começar a se alimentar mais")
elif peso <= 50.90 and 70.90:
    print(f"{nome} seu peso está normal")
    print('Parabéns, você está se alimentando bem e cuidando da saúde')
else:
    print(f"{nome} você está acima do peso")
    print('você precisa urgentemente emagrecer.')
