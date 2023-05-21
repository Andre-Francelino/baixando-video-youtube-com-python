
import pytube

# O link abaixo usado como exemplo é de um vídeo do canal Brincando com Ideias
# sobre a possibilidade de programar microcontrolador Arduino com a Linguagem python

# Definindo a URL do vídeo desejado
url = 'https://www.youtube.com/shorts/AhRiUZzxyBI'

# Criando um objeto YouTube com o URL do vídeo
yt = pytube.YouTube(url)

# Selecionando o 1º streaming de video disponível
video = yt.streams.first()

# Baixando o vídeo
video.download('Downloads')
