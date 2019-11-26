import psycopg2 as dbapi2
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner
import os

url = os.getenv("DATABASE_URL")


class CommentModel:

    # to decide insert or update
    def save(self, comment):
        if (comment.id == None):  # if object has no id value then insert
            self.insert(comment)
        else:
            if (self.ifExist(comment.id) != True):  # object has value but if it exists in database
                self.insert(comment)  # then insert since that object not in database
            else:
                self.update(comment)  # it exists in database update

    # insert method that will be do insertion
    def insert(self, comment):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Comments (people_id , berber , comment_title , comment_content , rate , date_time , 
                comment_like , comment_dislike)
                VALUES (%s , %s , %s , %s , %s , %s , %s , %s)""", (comment.peopleId, comment.berber, comment.title,
                                                                    comment.content, comment.rate, comment.dateTime,
                                                                    comment.like,
                                                                    comment.dislike))

    # get by id
    def getById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Comments as c where c.id = %s """, (id,))
            row = cursor.fetchone()

        # return one comment object
        comment = Comment()
        comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime, \
        comment.like, comment.dislike = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        return comment

    # get All
    def getAll(self):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * from Comments as c")
            rows = cursor.fetchall()

        comments = []
        for row in rows:
            comment = Comment()
            comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime, \
            comment.like, comment.dislike = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
            comments.append(comment)
        return comments

    def deleteById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE from Comments where id = %s
            """, (id,))

    # update method that will do update
    def update(self, comment):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Comments SET id = %s, people_id = %s , berber = %s , comment_title =%s , comment_content = %s ,
                rate = %s , date_time = %s , comment_like =%s , comment_dislike = %s where id = %s""",
                           (comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate,
                            comment.dateTime,
                            comment.like, comment.dislike, comment.id))

    def ifExist(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Comments where id = %s
            """, (id,))
        row = cursor.fetchone()
        if (row == None):
            return False
        return True


class ContactInfoModel:

    #  to decide insert or update
    def save(self, comment):
        if (comment.id == None):  # if object has no id value then insert
            self.insert(comment)
        else:
            if (self.ifExist(comment.id) != True):  # object has value but if it exists in database
                self.insert(comment)  # then insert since that object not in database
            else:
                self.update(comment)  # it exists in database update

    # insert method that will do insertion
    def insert(self, contactInfo):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Contact_info (berber_id , berbershop_id , type , telephone_number , facebook , twitter , 
                    instagram)
                    VALUES (%s , %s , %s , %s , %s , %s , %s)""",
                           (contactInfo.berberId, contactInfo.berberShopId, contactInfo.type,
                            contactInfo.telephoneNumber, contactInfo.facebook, contactInfo.twitter,
                            contactInfo.instagram))

    # update method that will do update
    def update(self, contactInfo):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Contact_Info SET id = %s, berber_id  = %s , berbershop_id = %s , type  =%s , telephone_number = %s ,
                facebook = %s , twitter = %s , instagram =%s where id = %s """,
                           (contactInfo.id, contactInfo.berberId, contactInfo.berberShopId, contactInfo.type,
                            contactInfo.telephoneNumber,
                            contactInfo.facebook, contactInfo.twitter, contactInfo.instagram, contactInfo.id))

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
        contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], row[
            5], row[6], row[7]
        return contactInfo

    def deleteById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE from Contact_info where id = %s
            """, (id,))

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

    def ifExist(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Contact_info where id = %s
            """, (id,))
        row = cursor.fetchone()
        if (row == None):
            return False
        return True


class RezervationModel:

    # to decide insert or update
    def save(self, rezervation):
        if (rezervation.id == None):  # if object has no id value then insert
            self.insert(rezervation)
        else:
            if (self.ifExist(rezervation.id) != True):  # object has value but if it exists in database
                self.insert(rezervation)  # then insert since that object not in database
            else:
                self.update(rezervation)  # it exists in database update

    # insert method that will do insertion
    def insert(self, rezervation):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Rezervation (people_id, berber_id, datetime_registration, datetime_rezervation, status, note, 
                    price_type)
                    VALUES (%s , %s , %s , %s , %s , %s , %s)""",
                           (rezervation.peopleId, rezervation.berberId, rezervation.dateTimeRegistration,
                            rezervation.dateTimeRezervation, rezervation.status, rezervation.note,
                            rezervation.priceType))

    # update method that will do update
    def update(self, rezervation):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Rezervation SET id = %s, people_id  = %s, berber_id = %s, datetime_registration = %s, datetime_rezervation = %s ,
                status = %s , note = %s , price_type =%s where id = %s """,
                           (
                               rezervation.id, rezervation.peopleId, rezervation.berberId,
                               rezervation.dateTimeRegistration,
                               rezervation.dateTimeRezervation, rezervation.status, rezervation.note,
                               rezervation.priceType, rezervation.id))

    # get by id
    def getById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Rezervation as r where r.id = %s """, (id,))
            row = cursor.fetchone()

        # return one comment object
        rezervation = Rezervation()
        rezervation.id, rezervation.peopleId, rezervation.berberId, rezervation.dateTimeRegistration, rezervation.dateTimeRezervation, \
        rezervation.status, rezervation.note, rezervation.priceType = row[0], row[1], row[2], row[3], row[4], \
                                                                      row[5], row[6], row[7]
        return rezervation

    def deleteById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE from Rezervation where id = %s
            """, (id,))

    # get All
    def getAll(self):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * from Rezervation as r")
            rows = cursor.fetchall()

        rezervations = []
        for row in rows:
            rezervation = Rezervation()
            rezervation.id, rezervation.peopleId, rezervation.berberId, rezervation.dateTimeRegistration, rezervation.dateTimeRezervation, \
            rezervation.status, rezervation.note, rezervation.priceType = row[0], row[1], row[2], row[3], row[4], \
                                                                          row[5], row[6], row[7]
            rezervations.append(rezervation)
        return rezervations

    def ifExist(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Rezervation where id = %s
            """, (id,))
        row = cursor.fetchone()
        if (row == None):
            return False
        return True


rezervationModel = RezervationModel()
rezervation = Rezervation()
rezervation.priceType = "not determined"
rezervationModel.save(rezervation)


class Peoplemodel:
    def insert(self, people):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor
            #cursor.execute("""INSERT INTO People (username, name_surname, mail, password_hash, gender, age,role)
            #               VALUES (%s , %s , %s , %s , %s , %s,  %s )""", (people.username, people.name_surname, people.mail, people.password_hash, people.gender, people.age, people.role))
            print (people.username, people.name_surname, people.mail, people.password_hash, people.gender, people.age, people.role)