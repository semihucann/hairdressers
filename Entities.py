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
class Comments:
    def __init__(self, id, peopleid, berberid, comment_title, comment_content, rate, datetime,comment_like,comment_dislike):
        self.id = id
        self.peopleid = peopleid
        self.berber = berberid
        self.comment_title = comment_title
        self.comment_content=comment_content
        self.rate = rate
        self.date_time=datetime
        self.comment_like=comment_like
        self.comment_dislike=comment_dislike




