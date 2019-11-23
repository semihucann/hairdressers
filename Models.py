import psycopg2 as dbapi2
from Entities import People,Comment, ContactInfo
url = "postgres://lltjryrurbhacv:4ed89e50a1718d204c9ac3cee26560e3874bf47bd7ce47e12f0c4f81611954f6@ec2-107-22-236-52.compute-1.amazonaws.com:5432/d2lpnjbrjgerqm"


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



class ContactInfoModel:

    # will be called from outside to decide insert or update
    def save(self, comment):
        if (comment.id == None):  # if object has no id value then insert
            self.__insert(comment)
        else:
            if (self.ifExist(comment.id) != True):  # object has value but if it exists in database
                self.__insert(comment)  # then insert since that object not in database
            else:
                self.__update(comment)  # it exists in database update

    # private insert method that will be used by save method
    def __insert(self, contactInfo):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Contact_info (berber_id , berbershop_id , type , telephone_number , facebook , twitter , 
                    instagram)
                    VALUES (%s , %s , %s , %s , %s , %s , %s)""", (contactInfo.berberId,contactInfo.berberShopId,contactInfo.type,
                                                                   contactInfo.telephoneNumber,contactInfo.facebook,contactInfo.twitter,
                                                                   contactInfo.instagram))

    # private update method that will be used by save method
    def __update(self, contactInfo):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Contact_Info SET id = %s, berber_id  = %s , berbershop_id = %s , type  =%s , telephone_number = %s ,
                facebook = %s , twitter = %s , instagram =%s where id = %s """,
                           (contactInfo.id,contactInfo.berberId,contactInfo.berberShopId,contactInfo.type,contactInfo.telephoneNumber,
                            contactInfo.facebook,contactInfo.twitter,contactInfo.instagram,contactInfo.id))

    # get by id
    def getById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Contact_info as c where c.id = %s """, (id,))
            row = cursor.fetchone()

        # return one comment object
        contactInfo = ContactInfo()
        contactInfo.id, contactInfo.berberId, contactInfo.berberShopId, contactInfo.type, contactInfo.telephoneNumber, \
        contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        return contactInfo

    def deleteById(self,id):
        with dbapi2.connect(url) as connection:
            cursor=connection.cursor()
            cursor.execute("""
                DELETE from Contact_info where id = %s
            """,(id,))

    # get All
    def getAll(self):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * from Contact_info as c")
            rows = cursor.fetchall()

        contacts = []
        for row in rows:
            contactInfo = ContactInfo()
            contactInfo.id, contactInfo.berberId, contactInfo.berberShopId, contactInfo.type, contactInfo.telephoneNumber, \
            contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], \
                                                                               row[5], row[6], row[7]
            contacts.append(contactInfo)
        return contacts


    def ifExist(self,id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Contact_info where id = %s
            """,(id,))
        row = cursor.fetchone()
        if(row == None):
            return False
        return True













