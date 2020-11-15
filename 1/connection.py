import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="localhost",
                                      port="5432",
                                      database="N2")
        return connection