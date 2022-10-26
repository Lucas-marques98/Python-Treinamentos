#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Por favor, digite um número:'))
dobro = num * 2 
triplo = num * 3
raizQuadrada = num ** (1/2) #pow(num, (1/2)) outra forma de fazer a raiz quadrada.

print(f'O dobro de {num} é igual a : {dobro}')
print(f'O triplo de {num} é igual a : {triplo}')
print(f'A raiz quadrada de {num} é igual a {raizQuadrada:.2f}')

#para formartar numeros flutuantes basta apenas usar :.2f ou mais casas flutuantes.