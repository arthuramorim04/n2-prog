from musica import Musica

colecao = Musica()

autor = str(input("Informe o autor: "))
nome = str(input("Informe o nome da música: "))
genero = str(input("Informe o gênero da música: "))

colecao.insert(nome, autor, genero)