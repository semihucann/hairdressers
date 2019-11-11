import psycopg2 as dbapi2
from Entities import People,Comments
url = "postgres://lltjryrurbhacv:4ed89e50a1718d204c9ac3cee26560e3874bf47bd7ce47e12f0c4f81611954f6@ec2-107-22-236-52.compute-1.amazonaws.com:5432/d2lpnjbrjgerqm"


class PeopleModel:

    def getAll(self): #get all People from Database
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
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


class CommentsModel:
    def Insert(Comments):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute("""INSERT INTO Comments (id,people_id , berber , comment_title , comment_content , rate , date_time , 
                comment_like , comment_dislike)
                VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s)""", (Comments.id, Comments.peopleid, Comments.berber, Comments.comment_title,
                                         Comments.comment_content, Comments.rate, Comments.date_time, Comments.comment_like,
                                         Comments.comment_dislike))



#adding value by using model and entity
Comments1=Comments(1,1,1,'my comment','content',1,'2016-06-22 19:10:25-07',1,2)
commentModel=CommentsModel
commentModel.Insert(Comments1)







