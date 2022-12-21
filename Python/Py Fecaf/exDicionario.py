semana = dict()

segunda = ['Professor Marcel', 'Java Desktop']
terca = ['Professor Alan', 'Desenvolvimento em Python']
quarta = ['Aula EAD', 'Liderança exponencial',
          'Linga Inglesa', 'Processos seletivos']
quinta = ['Professor Marcel', 'Programação orientada a objetos - Java Desktop']
sexta = ['Professor Alan', 'Estratégia e implementação de dados']
sabado = []
domingo = []

semana = dict({
    "Segunda": segunda,
    "Terça": terca,
    "Quarta": quarta,
    "Quinta": quinta,
    "Sexta": sexta,
    "Sabado": sabado,
    "Domingo": domingo
})

print(f'Todas as aulas que eu tenho na semana \n {semana}')

print("\n")

filmes = dict()

quebrando_regras = dict({
    "Filme": "Quebrando Regras",
    "Protagonista": "Sean Faris (Jake Tyler)",
    "Ano de lancçamento": 2008
})

grande_mestre = dict({
    "Filme": "o Grande mestre",
    "Protagonista": "Donnie Yen (Yip Man)",
    "Ano de lançamento": 2008
})

jhon_wick = dict({
    "Filme": "Jhon Wick",
    "Protagonista": "Keanu Reeves (Jhon Wick)",
    "Ano de lançamento": 2014
})

doctor_estranho = dict({
    "Filme": "DOUTOR ESTRANHO NO MULTIVERSO DA LOUCURA",
    "Protagonista": "Benedict Cumberbatch (Dr Estranho)",
    "Ano de lançamento": 2022
})

assasino_preçofixo = dict({
    "Filme": "Assasino a preço fixo",
    "Protagonista": "Jason Statham (Arthur Bishop)",
    "Ano lançamento": 2011
})


filmes = dict({
    "Quebrando Regras \n": quebrando_regras,
    "\n O grande Mestre ": grande_mestre,
    "\n Jhon Wick": jhon_wick,
    "\n Doutor Estranho": doctor_estranho,
    "\n Assasino a Preço Fixo": assasino_preçofixo
})

print(f'Tops 5 filmes que eu considero muito bons: \n {filmes}')
