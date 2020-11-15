import psycopg2
from connection import Connection

class ControllerDb():

    def insert(self, nome, autor, genero):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """insert into musica (nome, autor, genero) 
                        values ('{0}', '{1}', '{2}');"""\
                        .format(nome, autor, genero)
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


    def find(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            select = "select * from musica"
            cursor.execute(select)
            musicas = cursor.fetchall()

            for row in musicas:
                print("Id = ", row[0])
                print("Nome = ", row[1])
                print("Autor  = ", row[2])
                print("Gênero  = ", row[3], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()