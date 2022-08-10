x = 1  # int / valor inteiro
x = "Lucas Marques"  # string
x = 30.5  # float
y = False  # bool / Bolean
n1 = 5
n2 = 4
# numero complexo. Parte real é o n1, parte imaginária é o n2.
y = complex(n1, n2)

print("A parte real e", y.real)  # mostra a parte Real
print("A parte imaginaria e", y.imag)  # mostra a parte imaginária.


# list / Array / posso colocar tipo de dados diferente dentro de uma lista.
l = ['carro', 'moto', 'barco']

l[0] = 'Onibus'  # alterando o valor do indice 0.
s = range(0, 10, 1)  # cria uma lista de 0 a 10 de 1 em 1.
print(s)

# imprimindo um valor especifico da lista, coloco o indice do valor entre cochetes [].
print(l[0])

# tupla / ela é parecido com um Array mas eu não posso substituir um elemento.
m = ('dinheiro', 'viagem', 'sucesso')

print(m)

d = {  # tipo dictonary / objeto
    "nome": "Lucas Marques",
    "cidade": "Não importa",
    "exemplo": "dictonary"
}
print("Valor: ", d["nome"])

s = {2, 2, 3, 3, 4, 4, 5, 5}  # tipo set / ele não imprimi valores repetidos
# frozenset / ele bloqueia o set, não podemos alterar de nenhuma forma
s = frozenset({2, 2, 3, 3, 4, 4, 5, 5})

print("Os Valores são", str(s))

print("o Valor de ", x)  # mostra o valor de x
print("O tipo de x ", type(x))  # imprime o tipo da váriavel
