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
            cursor.execute("""INSERT INTO Comments (people_id , berber , title , content , rate , date_time , 
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
            cursor.execute("SELECT * from Comments as c order by c.date_time desc")
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
                UPDATE Comments SET id = %s, people_id = %s , berber = %s , title = %s , content = %s ,
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

    def getAllCommentswithPeople(self):

        commentlist = self.getAll()
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT p.id,p.username,p.name_surname from People as p  JOIN Comments as c ON p.id = c.people_id 
            """)

        rows = cursor.fetchall()
        i = 0
        for row in rows:
            people = People()
            people.id, people.username, people.name_surname = row[0], row[1], row[2]
            commentlist[i].peopleobj = people
            i += 1

        return commentlist

    def updateByIdTitleText(self, id, title, content, datetime):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                       UPDATE Comments SET title = %s , content= %s, date_time = %s  where id = %s""",
                           (title,content,datetime,id))






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
            cursor.execute("""INSERT INTO Rezervation (people_id, berbershop_id, datetime_registration, datetime_rezervation, status, note, 
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
                UPDATE Rezervation SET id = %s, people_id  = %s, berbershop_id = %s, datetime_registration = %s, datetime_rezervation = %s ,
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




# SEMİH MODELS ######################################################################
class Peoplemodel:
    def insert(self, people):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO People (username, name_surname, mail, password_hash, gender, age,role)
                           VALUES (%s , %s , %s , %s , %s , %s,  %s )""", (
            people.username, people.name_surname, people.mail, people.password_hash, people.gender, people.age,
            people.role))

    def control_exist(self, people):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM People where username = %s or mail = %s ", (people.username, people.mail))
        row = cursor.fetchone()
        if (row == None):
            return False
        return True

    def save(self, people):
        if (self.control_exist(people) == False):
            self.insert(people)
            return True
        else:
            return False


    def get_hash(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                               SELECT password_hash from people where username = %s
                            """, (username,))
            hash = cursor.fetchone()[0]
            return hash

    def get_role(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""    SELECT role from people where username = %s
                                   """, (username,))
            role = cursor.fetchone()[0]
            return role

    def get_all(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT * from people where username = %s
                                   """, (username,))
            person = People()
            rows = cursor.fetchall()
            person.id = rows[0][0]
            person.username = rows[0][1]
            person.name_surname = rows[0][2]
            person.mail = rows[0][3]
            person.password_hash = rows[0][4]
            person.gender = rows[0][5]
            person.age = rows[0][6]
            person.role = rows[0][7]
            person.active = True
            return person

    def get_all_list(self):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT * from people""")
            people_list = []
            rows = cursor.fetchall()
            for i in rows:
                person = People()
                person.id = i[0]
                person.username = i[1]
                person.name_surname = i[2]
                person.mail = i[3]
                person.password_hash = i[4]
                person.gender = i[5]
                person.age = i[6]
                person.role = i[7]
                person.active = True
                people_list.append(person)
            return people_list

    def control_exist_username(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM People where username = %s ", (username, ))
        row = cursor.fetchone()
        if (row == None):
            return False
        return True


class Berbermodel:
    def get_id(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                            SELECT id FROM PEOPLE WHERE username = %s 
                            """, (username, ))
        row = cursor.fetchone()
        return row

    def insert(self, berber):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Berber (people_id, gender_choice, experience_year, start_time, finish_time, rates) 
                             VALUES (%s , %s , %s , %s , %s , %s )""", (berber.people_id, berber.gender_choice, berber.experience_year,
                                                                             berber.start_time, berber.finish_time, berber.rates))


class Ownermodel:
    def get_id(self, username):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                            SELECT id FROM PEOPLE WHERE username = %s 
                            """, (username,))
        row = cursor.fetchone()
        return row


    def insert(self, owner):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Owner (people_id, tc_number, serial_number, vol_number, family_order_no, order_no)
                            VALUES (%s , %s , %s , %s , %s , %s )""", (owner.people_id, owner.tc_number, owner.serial_number, owner.vol_number, owner.family_order_no, owner.order_no))


######################################################################################