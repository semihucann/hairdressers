import psycopg2 as dbapi2
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner, LikedDisliked , Berbershop
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

    def getAllCommentswithPeopleByBerbershopId(self,id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT c.*, p.id, p.username from comments as c join people as  p on c.people_id = p.id 
                WHERE c.berbershop = %s order by c.date_time desc
            """,(id,))

        rows = cursor.fetchall()
        comments = []
        for row in rows:
            comment = Comment()
            comment.id, comment.peopleId, comment.berber, comment.title, comment.content, comment.rate, comment.dateTime, \
            comment.like, comment.dislike = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]

            people = People()
            people.id, people.username = row[9], row[10]
            comment.peopleobj = people
            comments.append(comment)
        return comments

    def commentCurrentUserRelationship(self,id,peopleid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
              select com.id, com.people_id, com.ifliked, com.ifdisliked from
               commentlikedislike as com where com.comment_id = %s and com.people_id = %s  
            """,(id,peopleid))

        row = cursor.fetchone()
        likedDisliked = LikedDisliked()
        if (row == None) :
            return None
        likedDisliked.id, likedDisliked.peopleId, likedDisliked.ifliked, likedDisliked.ifDisliked= row[0], \
        row[1], row[2], row[3]
        return likedDisliked

    def updateByIdTitleText(self, id, title, content, datetime):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                       UPDATE Comments SET title = %s , content= %s, date_time = %s  where id = %s""",
                           (title,content,datetime,id))


    def  increaseLikeNumber(self, commentid):
         with dbapi2.connect(url) as connection:
             cursor = connection.cursor()
             cursor.execute(""" UPDATE Comments as c SET comment_like = comment_like +1  where c.id = %s""",
                                   (commentid,))

    def increaseDislikeNumber(self, commentid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" UPDATE Comments as c SET comment_dislike = comment_dislike +1  where c.id = %s""",
                           (commentid,))

    def decreaseDislikeNumber(self, commentid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" UPDATE Comments as c SET comment_dislike = comment_dislike -1  where c.id = %s""",
                           (commentid,))

    def decreaseLikeNumber(self, commentid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" UPDATE Comments as c SET comment_like = comment_like -1  where c.id = %s""",
                           (commentid,))

    def increaseLikeDecreaseDislike(self, commentid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" UPDATE Comments as c SET comment_like = comment_like +1 , comment_dislike = comment_dislike -1
              where c.id = %s""",
                           (commentid,))

    def decreaseLikeIncreaseDislike(self, commentid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(""" UPDATE Comments as c SET comment_like = comment_like -1 , comment_dislike = comment_dislike + 1
              where c.id = %s""",
                           (commentid,))



    def likeDislikeUpdateCondition(self,commentid, peopleid, bool , likedislikeid):
        #it is not existed
        if(bool == 1 or bool == 2):
            like , dislike = 0, 0
            if(bool == 1):
                self.increaseLikeNumber(commentid)
                like = 1
            else :
                dislike = 1
                self.increaseDislikeNumber(commentid)

            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""  INSERT into CommentLikeDislike (comment_id, people_id, ifliked, ifdisliked) 
                                               values (%s, %s, %s, %s) """,
                               (commentid, peopleid, like, dislike))


        elif (bool == 3):
            self.decreaseLikeNumber(commentid)
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" DELETE from CommentLikeDislike as c where c.id = %s """,
                               (likedislikeid,))






        elif (bool == 4):

            like = 0
            dislike = 1
            self.decreaseLikeIncreaseDislike(commentid)
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" UPDATE CommentLikeDislike as c SET ifliked = %s, ifdisliked = %s where c.id = %s """,
                               (like, dislike, likedislikeid))
        elif (bool == 5):
            like = 1
            dislike = 0
            self.increaseLikeDecreaseDislike(commentid)
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute(""" UPDATE CommentLikeDislike as c SET ifliked = %s, ifdisliked = %s where c.id = %s """,
                               (like, dislike, likedislikeid))
        else :
            self.decreaseDislikeNumber(commentid)
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""DELETE from CommentLikeDislike as c where c.id = %s""",
                               (likedislikeid,))








    def likedislikeUpdate(self, commentid, peopleid, bool , likedislikeid):

        if( likedislikeid == None): #no like-dislike exist
            like = 0
            dislike = 0
            if(bool ==1):
                self.increaseLikeNumber(commentid)
                like = 1
            if (bool == -1):
                dislike = 1
                self.increaseDislikeNumber(commentid)
            with dbapi2.connect(url) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                                    INSERT into CommentLikeDislike (comment_id, people_id, ifliked, ifdisliked) 
                                    values (%s, %s, %s, %s) """,
                               (commentid, peopleid,like,dislike))

        else:
            if(bool == 1 or bool==-1): #delete it got notr
                if(bool == 1) :
                    self.decreaseDislikeNumber(commentid)
                else:
                    self.decreaseLikeNumber(commentid)
                with dbapi2.connect(url) as connection:
                    cursor = connection.cursor()
                    cursor.execute("""DELETE from CommentLikeDislike as c where c.id = %s""",
                                   (likedislikeid,))
            else:
                like,dislike = 0,0
                if(bool == 2):
                    like = 1
                    self.increaseLikeDecreaseDislike(commentid)
                else:
                    dislike = 1
                    self.decreaseLikeIncreaseDislike(commentid)
                with dbapi2.connect(url) as connection:
                    cursor = connection.cursor()
                    cursor.execute(""" UPDATE CommentLikeDislike as c SET ifliked = %s, ifdisliked = %s where c.id = %s """,
                                   (like,dislike,likedislikeid))









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
            cursor.execute("""INSERT INTO Contact_info (berbershop_id , type , telephone_number , facebook , twitter , 
                    instagram)
                    VALUES ( %s , %s , %s , %s , %s , %s)""",
                           (contactInfo.berberShopId, contactInfo.type,
                            contactInfo.telephoneNumber, contactInfo.facebook, contactInfo.twitter,
                            contactInfo.instagram))

    # update method that will do update
    def update(self, contactInfo):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Contact_Info SET id = %s, berbershop_id = %s , type  =%s , telephone_number = %s ,
                facebook = %s , twitter = %s , instagram =%s where id = %s """,
                           (contactInfo.id, contactInfo.berberShopId, contactInfo.type,
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
        contactInfo.id, contactInfo.berberShopId, contactInfo.type, contactInfo.telephoneNumber, \
        contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], row[
            5], row[6]
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
            contactInfo.id, contactInfo.berberShopId, contactInfo.type, contactInfo.telephoneNumber, \
            contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], \
                                                                               row[5], row[6]
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

    def getByBarbershopId (self, barbershopid):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                       SELECT * from Contact_info as c where c.berbershop_id = %s """, (barbershopid,))
            row = cursor.fetchone()

            # return one comment object
        contactInfo = ContactInfo()
        contactInfo.id,  contactInfo.berberShopId, contactInfo.type, contactInfo.telephoneNumber, \
        contactInfo.facebook, contactInfo.twitter, contactInfo.instagram = row[0], row[1], row[2], row[3], row[4], row[
            5], row[6]
        return contactInfo


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


    def delete_id(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM People where id = %s", (id,))

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

#FATIH'S MODELS

class CreditcardModel:
    def insert(self, creditCard):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Creditcards (people_id, name, card_number, cvv_number, last_month, last_year) 
                             VALUES (%s , %s , %s , %s , %s , %s )""", (creditCard.people_id, creditCard.name,
                                                                        creditCard.card_number,
                                                                        creditCard.cvv, creditCard.last_month,
                                                                        creditCard.last_year))


class Berbershopmodel:

    def insert(self, berbershop):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Berbershop (owner_people_id, shopname, location, city, opening_time, closing_time, trade_number) 
                             VALUES (%s , %s , %s , %s , %s , %s, %s)""", (berbershop.ownerpeople_id, berbershop.shopname,
                                                                        berbershop.location, berbershop.city,
                                                                        berbershop.openingtime, berbershop.closingtime,
                                                                        berbershop.tradenumber))


    #get All
    def getAll(self):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * from Berbershop")
            rows = cursor.fetchall()

        berbershops = []
        for row in rows:
            berbershop = Berbershop()
            berbershop.id, berbershop.ownerpeople_id, berbershop.shopname, berbershop.location, berbershop.city, \
            berbershop.openingtime, berbershop.closingtime, berbershop.tradenumber = row[0], row[1], row[2], row[3], row[4], \
                                                                               row[5], row[6], row[7]
            berbershops.append(berbershop)
        return berbershops

    # get by id
    def getById(self, id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * from Berbershop as b where b.id = %s """, (id,))
            row = cursor.fetchone()

        # return one berbershop object
        berbershop = Berbershop()
        berbershop.id, berbershop.ownerpeople_id, berbershop.shopname, berbershop.location, berbershop.city, \
        berbershop.openingtime, berbershop.closingtime, berbershop.tradenumber = row[0], row[1], row[2], row[3], row[4], \
                                                                                 row[5], row[6], row[7]
        return berbershop



contact = ContactInfo()
contactmodel = ContactInfoModel()
contact.berberShopId = 1
contact.telephoneNumber = 2164931980
contact.instagram = "ertugrulsmz"
contact.twitter = "ertugrulsmz"
contactmodel.insert(contact)



