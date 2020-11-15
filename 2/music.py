from connection import MongoConnect

class Music():

    def save(self, nome, autor, genero):
        conexao = MongoConnect()
        model = {
            "nome": nome,
            "genero": genero,
            "autor": autor
        }
        conexao.insert(model)