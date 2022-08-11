# Elemento Random, Para gerar números aleatórios

import random

num_r= random.randrange(0,59) #Gera um número Aleatório do 0 ao 59

print("Valor: ", num_r, type(num_r)) # mostra na tela o valor aleatório e o tipo dele.

num_6 = [
  random.randrange(0,59),
  random.randrange(0,59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  ] #Gera vários numeros ao mesmo tempo, dentro de uma List / Array

print("Valor 1: "+ str(num_6[0])) 
print("Valor 2: ", str(num_6[1]))
print("Valor 3: ", str(num_6[2]))
print("Valor 4: ", str(num_6[3]))
print("Valor 5: ", str(num_6[4]))
#Mostra na Tela os valores aleatórios da List