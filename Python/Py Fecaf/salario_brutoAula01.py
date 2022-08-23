nome = input("Digite o Nome do Funcionário: ") #pede pro usuário digitar o nome na tela
registro = int(input("Digite o Numero do Registro: ")) #Vai guardar um número inteiro
salario_bruto = float(input("Digite o salário bruto: ")) #vai guardar um número com casas decimais
gestor = bool(input("O funcionário especifico é um gestor? ")) #vai guardar um numero booleano

desconto = salario_bruto - (12.8/100) * salario_bruto #calcula o desconto do salário bruto
salario_desconto = salario_bruto - desconto #define o valor do desconto
comissao = salario_bruto + (16.7/100) * salario_bruto #descobre o valor da comissão
salario_comissao = comissao - salario_bruto # calcula a comissao que foi descontada do salário
salario_total = (salario_bruto-salario_desconto + salario_comissao) #calcula o valor final do salário


print("nome", nome, "registro" , registro)
print("Salário Bruto", salario_bruto)
print("Total de desconto", salario_desconto)
print("Total de comissão", salario_comissao)
print("Total do salário", salario_total)
