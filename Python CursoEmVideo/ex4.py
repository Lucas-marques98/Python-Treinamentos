#Dissecando uma váriavel

#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas informações possiveis sobre ele.

algo = input('Por favor digite algo:')

print('O tipo primitivo desse valor é ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está em capitalizada?', algo.istitle())

#Toda vez que estivermos trabalhando com strings, elas tem seus métodos.
#Métodos são todos que tem parenteses no fim.
