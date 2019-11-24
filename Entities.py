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
        self.campaigns = None # i need this for my page, you can ignore it for now



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













