# EXERCICIO RESOLVIDO SEM NENHUM MÉTODO.

lista = []

for n in range(0, 10):
    n1 = int(input('Digite um valor:'))
    if n == 0 or n1 > lista[-1]:
        lista.append(n1)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#EXERCICIO RESOLVIDO USANDO O MÉTODO SORTED

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro: '))
# n3 = int(input('Digite outro: '))
# n4 = int(input('Digite outro: '))
# n5 = int(input('Digite outro: '))
# n6 = int(input('Digite outro:'))
# n7 = int(input('Digite outro: '))
# n8 = int(input('Digite outro: '))
# n9 = int(input('Digite outro: '))
# n10 = int(input('Digite o último número: '))

# lista_crescente = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]

# print("ordem de números crescente = ", sorted(lista_crescente))