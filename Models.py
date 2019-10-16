import psycopg2
from Entities import People
try:
    connection = psycopg2.connect(user="x",
                                  password="x",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()

    class PeopleModel:

        def getAll(self): #get all People from Database
            query='Select * from People'
            cursor.execute(query)
            peopleTuple=cursor.fetchall() #get tuple from cursor

            peoplelist = [] #list of retrieved people Class
            for var in peopleTuple:
                id = (list(var))[0]
                username = (list(var))[1]
                name = (list(var))[2]
                surname = (list(var))[3]
                mail = (list(var))[4]
                password = (list(var))[5]
                gender = (list(var))[6]
                age = (list(var))[7]
                peoplelist.append(People(id,username,name,surname,mail,password,gender,age))
            return peoplelist


finally:
    if (connection):
        cursor.close()
        connection.close()







