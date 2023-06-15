professor = input("Olá professor(a), por favor diga seu nome: ")
qtdAlunos = int(input(f"Professor(a) {professor} por favor me diga quantos alunos tem na sala: "))

for i in range(qtdAlunos):
  nomeAlunos = int(input(f"Professor(a) {professor} informe o nome dos alunos"))