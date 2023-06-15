num1 = float(input("Entre com o número 1: "))
num2 = float(input("Entre com o número 2: "))
x = int(input("Entre com o valor de x: "))
if  x == 1:
    y = num1+num2
    print (y)
elif x == 2:
    y = num1-num2
    print (y)
elif x == 3:
    y = num1*num2
    print (y)
elif x == 4:
    y = num1%num2
    print (y)
else:
    print ("ERRO")