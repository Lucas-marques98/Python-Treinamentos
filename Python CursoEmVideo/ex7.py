#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Olá, por favor digite seu nome: ')
n1 = float(input(f'{nome} digite a primeira nota: '))
n2 = float(input(f'{nome} digite a segunda nota: '))

print(f'{nome} a média entre {n1} e {n2} é igual a {(n1 + n2) / 2}')