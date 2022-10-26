#Escreva um programa que leia um valor em metros e o exiba convertido em centìmetros e milimetros.

medida = float(input('Por favor, digite uma distância em metros: '))

print(f'A medida de {medida}M corresponde a {medida * 100 :.0f}CM e a {medida * 1000 :.0f}MM')