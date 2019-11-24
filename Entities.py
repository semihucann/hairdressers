from datetime import datetime

class Berbershop:
    def __init__(self):

        self.id=None
        self.shopname=None
        self.ownerpeople_id=None
        self.location=None
        self.openingtime=None
        self.closingtime=None
        self.tradenumber=None






#Entity of People table in database
class People:
    def __init__(self,id,username,name,surname,mail,password,gender,age):
        self.username=username
        self.name=name
        self.surname=surname
        self.mail=mail
        self.password=password
        self.gender=gender
        self.age=age

    @property
    def fullname(self):
        return self.name+" "+self.surname

    @fullname.setter
    def fullname(self,fullname):
        first, last=fullname.split(' ')
        self.name=first
        self.surname=last





#Entity of Comment table in Database
class Comment:
    def __init__(self):
        self.id = None
        self.peopleId = None
        self.berber = None
        self.title = ""
        self.content = ""
        self.rate = 0
        self.dateTime = datetime.now()
        self.like = 0
        self.dislike = 0

#Entity of Contact_info table in database
class ContactInfo:
    def __init__(self):
        self.id = None
        self.berberId = None
        self.berberShopId = None
        self.type = None
        self.telephoneNumber = None
        self.facebook = None
        self.twitter = None
        self.instagram = None


#Entity of Rezervation table in database
class Rezervation :
    def __init__(self):
        self.id = None
        self.peopleId = None
        self.berberId = None
        self.dateTimeRegistration = datetime.now()
        self.dateTimeRezervation = None
        self.status = None
        self.note = None
        self.priceType = None













