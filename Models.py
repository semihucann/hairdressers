import psycopg2 as dbapi2
from Entities import People,Comment
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


class CommentModel:

    #will be called from outside to decide insert or update
    def save(self, comment):
        if(comment.id == None): # if object has no id value then insert
            self.__insert(comment)
        else:
            if(self.ifExist(comment.id)!=True): # object has value but if it exists in database
                self.__insert(comment) #then insert since that object not in database
            else:
                self.__update(comment) # it exists in database update




    #private insert method that will be used by save method
    def __insert(self, comment):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute("""INSERT INTO Comments (people_id , berber , comment_title , comment_content , rate , date_time , 
                comment_like , comment_dislike)
                VALUES (%s , %s , %s , %s , %s , %s , %s , %s)""", (comment.peopleId, comment.berber, comment.title,
                                         comment.content, comment.rate, comment.dateTime, comment.like,
                                         comment.dislike))
    #get by id
    def getById(self,id):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute ("""
                SELECT * from Comments as c where c.id = %s """,(id,))
            row = cursor.fetchone()

        # return one comment object
        comment = Comment()
        comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime, \
        comment.like, comment.dislike = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        return comment

    #get All
    def getAll(self):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute("SELECT * from Comments as c")
            rows=cursor.fetchall()

        comments = []
        for row in rows:
            comment = Comment()
            comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime, \
            comment.like, comment.dislike = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
            comments.append(comment)
        return comments

    def deleteById(self,id):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute("""
                DELETE from Comments where id = %s
            """,(id,))

    #private update method that will be used by save method
    def __update(self,comment):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Comments SET id = %s, people_id = %s , berber = %s , comment_title =%s , comment_content = %s ,
                rate = %s , date_time = %s , comment_like =%s , comment_dislike = %s where id = %s""",
                (comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime,
                 comment.like, comment.dislike, comment.id))

    def ifExist(self,id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Comments where id = %s
            """,(id,))
        row = cursor.fetchone()
        if(row == None):
            return False
        return True

















