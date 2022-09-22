cont_eymael= 0 #contador do eymael
cont_levy= 0 #contador do levy
cont_daciolo= 0 #contador do daciolo
cont_nul= 0 #contador de votos nulos
cont_br= 0 #contador de votos em brancos
tot_votos= 0 #contador de todos os votos

continua = "s"
 #enquanto continua que vale "s" for igual a "s" ele vai rodar o programa, se for diferente ele vai parar e mostrar a mensagem de erro
while continua =="s":
    print("Eleiçoes 2022")
    print("Votação: Escolha o seu candidato: ")
    print("1 - Eymael / 2 - Levy Fidelix / 3 - Cabo Daciolo")
    print("4 - Voto Nulo / 5 - Voto em Branco")
    print("O código inválido irá anular o seu voto")
    voto=int(input("Digite o seu voto:"))
    if voto == 1:
        cont_eymael=cont_eymael+1
    elif voto == 2:
        cont_levy=cont_levy+1
    elif voto == 3:
        cont_daciolo=cont_daciolo+1
    elif voto == 4:
        cont_nul=cont_nul+1
    elif voto == 5:
        cont_br=cont_br+1
    else:
        print("Voto anulado")
        cont_nul=cont_nul+1
    tot_votos=tot_votos+1
    print("FIM - A democracia agradece")
    print("Digite s para o próximo voto ou qualquer outra")
    print("caracter para encerrar a votação nesta urna")
    continua = input()
print("Totais da urna:")
print("Total de votos = ",tot_votos)
print("Eymael -> ",cont_eymael," % =",(cont_eymael/tot_votos)*100)
print("Fidelix -> ",cont_levy," % =",(cont_levy/tot_votos)*100)
print("Daciolo -> ",cont_daciolo," % =",(cont_daciolo/tot_votos)*100)
print("Brancos -> ",cont_br," % =",(cont_br/tot_votos)*100)
print("Nulos -> ",cont_nul," % =",(cont_nul/tot_votos)*100)