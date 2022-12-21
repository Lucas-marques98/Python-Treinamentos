semana = dict()

segunda = ['Professor Marcel', 'Java Desktop']
terca = ['Professor Alan', 'Desenvolvimento em Python']
quarta = ['Aula EAD', 'Liderança exponencial','Linga Inglesa', 'Processos seletivos']
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

velozes_furiosos = dict({
    "Filme": "Velozes e furiosos",
    "Protagonista": "Vin Diesel (Dom Toretto)",
    "Ano de lançamento": 2001
})

vingadores = dict({
    "Filme": "Os vingadores",
    "Protagonista": "Robert Downey (Homem de Ferro)",
    "Ano de lançamento": 2012
})

pantera_negra = dict({
    "Filme": "Pantera negra",
    "Protagonista": "Chadwick Boseman (Pantera Negra)",
    "Ano lançamento": 2018
})

coringa = dict({
    "Filme": "Coringa",
    "Protagonista": "Joaquin Phoenix (Coringa)",
    "Ano lançamento": 2019
})

carga_explosiva = dict({
    "Filme": "Carga Explosiva",
    "Protagonista": "Jason Statham (Frank Martin)",
    "Ano lançamento": 2011
})


filmes = dict({
    "Velozes e furiosos": velozes_furiosos,
    "Pantera negra": pantera_negra,
    "Vingadores": vingadores,
    "Coringa": coringa,
    "Carga explosiva": carga_explosiva
})

print(f'Meus tops 5 filmes:  \n {filmes}')
