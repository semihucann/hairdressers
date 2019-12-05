from flask import render_template, Flask, request, redirect, url_for, current_app
import datetime

from Models import CommentModel, ContactInfoModel, StatisticsModel
from Models import Peoplemodel, Berbermodel, Ownermodel, CreditcardModel, Berbershopmodel, RezervationModel
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner, CreditCard, Berbershop
from passlib.hash import pbkdf2_sha256 as hasher
from flask_login import LoginManager, login_user, logout_user, current_user


#Ertuğrul's Function


def home_page():
    berbershopModel = Berbershopmodel()
    berbershopList = berbershopModel.getAll()

    nonuniquecitylist = []
    uniquecitylist = []

    for berbershop in berbershopList :
        nonuniquecitylist.append(berbershop.city)
    for x in nonuniquecitylist:
        # check if exists in unique_list or not
        if x not in uniquecitylist:
            uniquecitylist.append(x)

    return render_template('home.html', berbershops=berbershopList, citylist=uniquecitylist)


def statistics():
    statisticModel = StatisticsModel()
    mostPopularBerbers = statisticModel.mostPopularBerbershops()
    return render_template('statistics.html',mostPopularBerbers = mostPopularBerbers)

def rezervation(id):
    if request.method == 'GET':
        options = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

        bm = Berbershopmodel()
        berbershop = bm.getById(id)
        rezervationModel = RezervationModel()
        now = datetime.datetime.now()
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)
        tmrw = str(tomorrow) + " 00:00"
        tomorrowafter = today + datetime.timedelta(days=2)
        tmrwafter = str(tomorrowafter)+ " 00:00"

        todayrezervations = rezervationModel.getAllByBarberShop(int(id),now,tmrw)
        tomorrowrezervations = rezervationModel.getAllByBarberShop(int(id),tmrw,tmrwafter)
        for t in tomorrowrezervations:
            minute = t.dateTimeRezervation.minute
            minutestr = ""
            if minute == 0 :
                minutestr = str(minute) + "0"
            else:
                minutestr = str(minute)
            t.dateTimeRezervation = str(t.dateTimeRezervation.hour) + ":" + minutestr
        for j in todayrezervations:
            minute = j.dateTimeRezervation.minute
            minutestr = ""
            if minute == 0:
                minutestr = str(minute) + "0"
            else:
                minutestr = str(minute)
            j.dateTimeRezervation = str(j.dateTimeRezervation.hour) + ":" + minutestr


        return render_template('rezervation.html', today = today,tomorrow = tomorrow,
                               id=id,todayrezervations=todayrezervations, tomorrowrezervations = tomorrowrezervations,
                               hour = now.hour, options = options, berbershop = berbershop)

    else:
        formvalue = request.form["formvalue"]
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        hourint = 0
        note =""

        if(int(formvalue) == 1):
            hour = request.form["todayhour"]
            tdy = str(today) + " " + str(hour)
            note = request.form["todaynote"]
        else:
            hour = request.form["tomorrowhour"]
            tdy = str(tomorrow) + " " + str(hour)
            note = request.form["tomorrownote"]


        rm = RezervationModel()
        rezervation = Rezervation()
        rezervation.peopleId = current_user.id
        rezervation.dateTimeRezervation = tdy
        rezervation.note = note
        rezervation.status = "notokey"
        rezervation.berberShopId = int(id)
        rm.insert(rezervation)
        return redirect(url_for("rezervation", id=id))

def rezervation_delete (id):
    rezid = request.form["rezid"]
    rezidint = int(rezid)
    rm = RezervationModel()
    rm.deleteById(rezidint)
    return redirect(url_for("rezervation", id=id))

def rezervation_edit (id):
    rezid = request.form["rezid"]
    datehour = request.form["daterez"]
    day = request.form["day"]
    date = day + " " + datehour
    rezidint = int(rezid)
    rm = RezervationModel()
    rm.updateByIdDate(rezidint,date)
    return redirect(url_for("rezervation", id=id))



def barbershop_view_edit(id):
    commentrate = request.form["bcommentrate"]
    commentrateint = int(commentrate)
    commentid = request.form["commentid"]
    commentidint = int(commentid)
    commenttitle = request.form["commenttitle"]
    commenttext  = request.form["commenttext"]
    dateTime = datetime.datetime.now()

    commentModel = CommentModel()
    commentModel.updateByIdTitleTextRate(commentidint,commenttitle,commenttext,dateTime,commentrateint)

    return redirect(url_for("barbershop_view", id=id))

def barbershop_view_delete(id):
    idint = int(id)
    commentModel = CommentModel()
    commentModel.deleteById(int(request.form["commentid"]))
    return redirect(url_for("barbershop_view", id=id))

def barbershopview_comment_like_dislike(id) :
    if(current_user.is_active != True):
        return redirect(url_for("signin"))
    likeddislikedid = request.form["likedislikeid"]
    likeddislikedidint = None

    if(len(likeddislikedid) > 0 and likeddislikedidint != " "):
        likeddislikedidint = int(likeddislikedid)


    commentid = request.form["commentid"]
    commentidint = int(commentid)
    peopleid = request.form["peopleid"]
    peopleidint = int(peopleid)
    bool = int(request.form["bool"])
    boolint = int(bool)

    commentModel = CommentModel()
    commentModel.likedislikeUpdate(commentidint,peopleidint,boolint, likeddislikedidint)
    return redirect(url_for("barbershop_view", id=id))


def barbershop_view(id):
    if request.method == 'GET':
        idint = int(id)
        #Get the list of the comment
        commentModel = CommentModel()
        commentlist = commentModel.getAllCommentswithPeopleByBerbershopId(idint)


        berbershopModel = Berbershopmodel()
        berbershop = berbershopModel.getById(id)

        contactInfoModel = ContactInfoModel()
        contactInfo = contactInfoModel.getByBarbershopId(idint)
        berbershop.contactInfo = contactInfo

        #list berbers for rating
        berberModel = Berbermodel()
        berbers = berberModel.getBerbersByBerbershop(idint)

        x = 0 #indicating there is current user
        if(current_user.is_active):
            x=1


        for c in commentlist:
            c.dateTime = datetime.date(c.dateTime.year, c.dateTime.month, c.dateTime.day)
            if x==1 :
                c.likedDislikedobj = commentModel.commentCurrentUserRelationship(c.id, current_user.id)

        return render_template("barbershopview.html", commentlist= commentlist, berbershop = berbershop, berbers = berbers)

    else: #POST
        idint = int(id)
        commentModel = CommentModel()

        #get Form Data
        berbershopid =  idint = int(id)
        commenttitle = request.form["bcommenttitle"]
        commenttext = request.form["bcommenttext"]
        commentrate = request.form["bcommentrate"]
        berberid = request.form["berber"]
        berberidint = int(berberid)

        if berberidint == -1: #berbershop itself
            berberidint = None

        #save in database

        comment = Comment()
        comment.berbershop, comment.title, comment.content, comment.rate,comment.peopleId, comment.berber = int(berbershopid), commenttitle, commenttext,\
                                                                                        int(commentrate),current_user.id, berberidint

        commentModel.insert(comment)
        return redirect(url_for("barbershop_view",id=id))

def contact_delete(id):
    cm= ContactInfoModel()
    contactId = request.form["contactid"]
    cm.deleteById(int(contactId))
    return redirect(url_for("barbershop_view", id=id))


def contact_settings(id):

    if request.method == 'GET' :
        cm = ContactInfoModel()
        contactentity = cm.getByBarbershopId(int(id))
        return  render_template("contact.html", id = id, contact = contactentity)

    #POST
    cm = ContactInfoModel()
    typec = request.form["typec"]
    instagramc = request.form["instagramc"]
    twitterc = request.form["twitterc"]
    facebookc = request.form["facebookc"]
    contactId = request.form["contactid"]
    phoneNumber = request.form["phonenumber"]

    contact = ContactInfo()
    contact.type = typec
    contact.instagram = instagramc
    contact.twitter = twitterc
    contact.facebook = facebookc
    contact.telephoneNumber = phoneNumber
    contact.berberShopId = int (id)

    if (contactId == None) or (contactId == "") :
        cm.insert(contact)
    else :
        contact.id = int(contactId)
        cm.update(contact)

    return redirect(url_for("barbershop_view", id=id))



###########################################################



def blog_page():

    return render_template("blog.html", name="blog_page")


def newpost_page():

    return render_template("newpost.html", name="newpost_page")


def profile_page():
    if request.method == 'POST':
        if "delete_card" in request.form:
            CreditcardModel().delete_credit_card(request.form["delete_card"])
        else:
            credit_card = CreditCard()
            credit_card.name = request.form["name_surname"]
            credit_card.card_number = request.form["number"]
            last_date = request.form["date"]
            if "/" not in last_date:
                return render_template("profile.html")
            array_last_date = last_date.split("/")
            credit_card.last_year = array_last_date[1]
            credit_card.last_month = array_last_date[0]
            credit_card.cvv = request.form["cvv"]
            credit_card.people_id = request.form["card_owner_id"]

            if "card_id" in request.form:
                credit_card.id = request.form["card_id"]
                CreditcardModel().update(credit_card)
            else:
                CreditcardModel().insert(credit_card)

    if current_user.is_active:
        list_of_cards = CreditcardModel().get_all_credit_cards_of_a_person(current_user.id)
        return render_template("profile.html", cards=list_of_cards)

    return render_template("profile.html", cards=[])


def addcreditcard_page():
    return render_template("add_credit_card.html", title="Add Credit Card", credit_card=None)


def updatecreditcard_page():
    credit_card = CreditCard()
    if request.method == 'POST':

        credit_card.name = request.form["name_surname"]
        credit_card.card_number = request.form["number"]
        last_date = request.form["date"]
        if "/" not in last_date:
            return render_template("profile.html")
        array_last_date = last_date.split("/")
        credit_card.last_year = array_last_date[1]
        credit_card.last_month = array_last_date[0]
        credit_card.cvv = request.form["cvv"]
        credit_card.id = request.form["card_id"]

    return render_template("add_credit_card.html", title="Update Credit Card", credit_card=credit_card)

#Semih's Functions
##Notes:
# Berber signup kısmında start  and finish time sadece saat cinsinden alındı (08:30 yerine 08)


def signupbase_page():
    if request.method == 'GET':
        return render_template("register_type.html")
    else:
        if request.form['submit_button'] == 'user':
            return redirect(url_for('signup_user_page'))
        elif request.form['submit_button'] == 'berber':
            return redirect(url_for('signup_berber_page'))
        elif request.form['submit_button'] == 'owner':
            return redirect(url_for('signup_owner_page'))
        return render_template("profile.html")


def signup_berber_page():
    if request.method == 'GET':
        return render_template("signup_berber.html")
    else:
        person = People()
        person.username = request.form["username"]
        person.name_surname = request.form["name_surname"]
        person.mail = request.form["mail"]
        person.password_hash = hasher.hash(request.form["password"])
        person.gender = request.form["gender"]
        person.age = request.form["age"]
        person.role = "berber"
        people = Peoplemodel()

        if (people.control_exist(person)):
            return render_template("signup_berber.html", message="False")
        else:
            people.save(person)
            berbers = Berbermodel()
            berber = Berber()
            berber.people_id = berbers.get_id(person.username)[0]
            berber.gender_choice = request.form["gender_choice"]
            berber.experience_year = request.form["experience"]
            berber.start_time = request.form["start_time"][:2]
            berber.finish_time = request.form["finish_time"][:2]
            berbers.insert(berber)
            return render_template("signup_berber.html", message="True")

        return redirect(url_for("signup_berber_page"))


def signup_owner_page():
    if request.method == 'GET':
        return render_template("signup_owner.html")
    else:
        person = People()
        person.username = request.form["username"]
        person.name_surname = request.form["name_surname"]
        person.mail = request.form["mail"]
        person.password_hash = hasher.hash(request.form["password"])
        person.gender = request.form["gender"]
        person.age = request.form["age"]
        person.role = "owner"
        people = Peoplemodel()
        if(people.control_exist(person)):
            return render_template("signup_owner.html", message="False")
        else:
            people.save(person)
            owners = Ownermodel()
            owner = Owner()
            owner.people_id = owners.get_id(person.username)[0]
            owner.tc_number = request.form["tc_number"]
            owner.serial_number = request.form["serial_number"]
            owner.vol_number = request.form["vol_number"]
            owner.family_order_no = request.form["family_order_no"]
            owner.order_no = request.form["order_no"]
            owners.insert(owner)
            return render_template("signup_owner.html", message="True")

        return redirect(url_for("signup_owner_page"))


def signup_user_page():
    if request.method == 'GET':
        return render_template("signup_user.html", message="")
    else:
        person = People()
        person.username = request.form["username"]
        person.name_surname = request.form["name_surname"]
        person.mail = request.form["mail"]
        person.password_hash = hasher.hash(request.form["password"])
        person.gender = request.form["gender"]
        person.age = request.form["age"]
        person.role = "user"

        people = Peoplemodel()
        if (people.save(person)):
            return render_template("signup_user.html", message="True")
        else:
            return render_template("signup_user.html", message="False")

        return redirect(url_for("signup_user_page"))


def signin():
    if request.method == 'GET':
        return render_template("signin.html", message="")
    else:
        username = request.form["username"]
        password = request.form["password"]
        people = Peoplemodel()

        #Eğer kullanıcı databasede ekli değilse patlar
        if(people.control_exist_username(username)):
            person = People()
            person = people.get_all(username)

            if(hasher.verify(password, person.password_hash)):
                login_user(person)
                current_app.config["LOGGED_USERS"][person.username] = person

                return render_template("signin.html", message="True", role=people.get_role(username))
            else:
                return render_template("signin.html", message="False")
        else:
            return render_template("signin.html", message="False")

def signout():
    logout_user()
    return redirect(url_for("home_page"))

def admin_panel():
    peoples = []
    people = Peoplemodel()
    berbers = Berbermodel()
    owners = Ownermodel()
    peoples = people.get_all_list()
    if request.method == 'GET':
        if (current_user.role == "admin"):
            # Düzeltttt user yerine admin yazılacak !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return render_template("admin_panel.html", people=peoples)
        else:
            return render_template("signin.html", message="admin_error")
    else:
        if request.form["edit"]=="delete":
            form_movie_keys = request.form.getlist("people_keys")
            for i in form_movie_keys:
                for j in peoples:
                    if j.id == int(i) and j.role == "user":
                        people.delete_id(j.id)
                    elif j.id == int(i) and j.role == "berber":
                        berbers.delete_with_people_id(j.id)
                        people.delete_id(j.id)
                    elif j.id == int(i) and j.role == "owner":
                        owners.delete_with_people_id(j.id)
                        people.delete_id(j.id)

        else:
            print(request.form["edit"])
            #print(peoples[int(request.form["edit"])])
            for i in peoples:
                if int(request.form["edit"]) == i.id:
                    print(i.username)
                    #return redirect(url_for("admin_update", person="i"))
                    return  render_template("update.html", person=i)
        return redirect(url_for("admin_panel"))


def admin_update():
    return render_template("update.html")