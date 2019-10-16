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
    def __init__(self, id, peopleid, berberid, comment, point, datetime):
        self.id = id
        self.peopleid=peopleid
        self.berberid=berberid
        self.comment=comment
        self.point=point
        self.datetime=datetime

