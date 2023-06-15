pessoas = []

print('1 - Cadastrar Pessoas')
print('2 - Mostrar Listas')
print('3 - Sair')

opcao = input('Informe o que deseja a cima: ')

if opcao == '1':
    nome = input('Nome Completo: ')
    rg = input('Numero de Identidade: ')
    cpf = input('Numero CPF: ')
    idade = input('Idade: ')
    nascimento = input('Nascimento: ')

    pessoas.append({'nome': nome, 'rg': rg, 'CPF': cpf,
                   'Idade': idade, 'Nascimento': nascimento})

    print('Pessoa cadastrada com sucesso!')

elif opcao == '2':
    print('<<<<<<<< Lista de Cadastro das pessoas >>>>>>>>')
    for pessoa in pessoas:
