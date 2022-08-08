num1=num2=res=0 #Váriaveis Globais / elas podem ser acessados em qualquer parte do programa

canal= "Cfb Cursos" #é possivel usar uma várivel dentro de uma função quando ela estiver em escopo global.

def lucas(): #criando Função
    global nome #váriavel Global dentro do escopo da função.
    nome = 'Lucas'
    sobrenome = 'Marques' #Váriavel local / dentro do escopo da função.

    #Não é possivel fazer um print em uma váriavel local, fora do escopo da função, a não ser que eu defina ela como uma várivel global
lucas() #chamando função.
print(nome)


  