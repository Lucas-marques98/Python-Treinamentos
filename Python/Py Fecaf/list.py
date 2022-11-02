alunos = {}

for i in range(0,5):
  aluno = input('Por favor digite o nome do aluno:')
  nota = float(input('Por favor digite as notas:'))
  alunos [aluno]= nota 
  
  print(f'{alunos}')
  soma=0
for nota in alunos.values():
    soma = soma + nota
media = soma/len(alunos)

print(f'A média da turma é {media:.2f}')