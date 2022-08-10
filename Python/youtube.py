from pytube import YouTube, streams

url = input(('Coloque sua Aqui Sua Url')) #informa para digitar a Url
video = YouTube(url) #importa a Url do Youtube
strem = video.streams.get_highest_resolution() #Baixa o video na melhor qualidade
streams.download(output_path='C:/Users/LUCAS-MARQUES/Desktop') #Destino que o video vai ser baixado

print('Seu video foi baixado com Sucesso')

