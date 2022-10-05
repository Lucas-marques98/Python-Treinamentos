def calcularJuros (c,t,p):
  juros = c * t * p
  return juros

capital = float(input("digite o capital em R$: "))
taxa = float(input("digite a taxa em %: ")) / 100
periodo = int(input("digite o periodo em meses: "))
print("")
juros = calcularJuros((capital, taxa , periodo))
montante = capital + juros
print("Montante a ser pago em R$%.2f"%montante)