nome = "Ronaldo"

print(nome[0]) // para acessar o indice da String
print(nome[4])
print(nome[8])

print(nome.upper()) #Deixa as letras todas Maiúsculas
print(nome.lower()) #Deixa as letras todas Minusculas 
print(nome.capitalize()) #Deixa a String com a primeira Letra Maiúscula
print(nome.strip())

tiozao = " João "

print(tiozao.strip()) #Remove os espaços dentro de uma String

print(len(nome)) #Para descobrir o comprimento da String

x = 50

if x % 5 != 0:
  print("X não é Multiplo de 5")
  
else:
  print("é multiplo por 5")

a = int(input("Digite um Numero:"))
if (a > 0 ) and (a < 10):
  print("Entre Zero e Dez")


salario = float(input("Digite o Salário:"))

if salario < 2000:
  salario = salario * 1.20
  print("Salário = R$", salario)
else:
  salario = salario * 1.10
  print("Salário = R$", salario)