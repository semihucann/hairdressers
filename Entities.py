from datetime import datetime

# Entity of Comment table in Database
class Comment:
    def __init__(self):
        self.id = None
        self.peopleId = None
        self.berber = None
        self.berbershop = None
        self.title = ""
        self.content = ""
        self.rate = 0
        self.dateTime = datetime.now()
        self.like = 0
        self.dislike = 0
        self.peopleobj = None
        self.likedDislikedobj = None

class LikedDisliked:
    def __init__(self):
        self.id = None
        self.comment_id = None
        self.peopleId = None
        self.ifliked = None
        self.ifDisliked = None


# Entity of Contact_info table in database
class ContactInfo:
    def __init__(self):
        self.id = None
        self.berberShopId = None
        self.type = None
        self.telephoneNumber = None
        self.facebook = None
        self.twitter = None
        self.instagram = None


# Entity of Rezervation table in database
class Rezervation:
    def __init__(self):
        self.id = None
        self.peopleId = None
        self.berberShopId = None
        self.dateTimeRegistration = datetime.now()
        self.dateTimeRezervation = None
        self.status = None
        self.note = None
        self.priceType = None


##Semih Classlar########################################################
class People:
    def __init__(self):
        self.id = None
        self.username = None
        self.name_surname = None
        self.mail = None
        self.password_hash = None
        self.gender = None
        self.age = None
        self.role = None
        self.active = True

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active

class Berber:
    def __init__(self):
        self.id = None
        self.people_id = None
        self.berber_shop_id = None
        self.gender_choice = None
        self.experience_year = None
        self.start_time = None
        self.finish_time = None
        self.rates = None


class Owner:
    def __init__(self):
        self.id = None
        self.people_id = None
        self.tc_number = None
        self.serial_number = None
        self.vol_number = None
        self.family_order_no = None
        self.order_no = None

########################################################################

# FATIH'S CLASSES


class ServicePrice:
    def __init__(self):
        self.id = None
        self.shop_id = None
        self.service_name = None
        self.definition = None
        self.gender = None
        self.price = None
        self.duration = None


class CreditCard:
    def __init__(self):
        self.id = None
        self.people_id = None
        self.name = None
        self.card_number = None
        self.cvv = None
        self.last_month = None
        self.last_year = None


class Berbershop:
    def __init__(self):
        self.id = None
        self.shopname = None
        self.ownerpeople_id = None
        self.location = None
        self.city = None
        self.openingtime = None
        self.closingtime = None
        self.tradenumber = None
        self.campaigns = None  # i need this for my page, you can ignore it for now
        self.contactInfo = None

########################################################################

# HALIS'S CLASSES

