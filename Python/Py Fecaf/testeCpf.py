#Validar os últimos digitos do CPF 

# # CPF fictício “529982247-25”.

#validando o último digito somando os 9 primeiros digitos de 10 até 2
print(5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2)
#Somando os resultados, pegando esse valor e multiplicando por 10 e pegando o resto desse valor por 11
# print(50+18+72+63+48+10+8+12+14)
print (295 * 10 % 11) 

print(5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2)

print(347 * 10 % 11)


print("Cpf Válido!!!")