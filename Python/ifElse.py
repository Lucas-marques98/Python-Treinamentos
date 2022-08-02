peso = float(input("Informe seu Peso"))
altura = float(input("Informe sua Altura"))
imc = peso / (altura * altura)

print("o seu imc é de",imc)

if imc <= 18.5:
  print("Você está abaixo do peso")
elif imc <= 24.90:
  print("seu peso está normal")
else:
  print("você está acima do peso")