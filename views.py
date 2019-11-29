from flask import render_template, Flask, request, redirect, url_for
from datetime import date,datetime
import Temporarypython
from Models import CommentModel
from Models import Peoplemodel, Berbermodel, Ownermodel
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner
from passlib.hash import pbkdf2_sha256 as hasher
from flask_login import LoginManager, login_user, logout_user, current_user


#Ertuğrul's Function


def home_page():
    berbershopList = Temporarypython.listOfBerbers()
    citylist = ["Istanbul", "Ankara", "Izmir", "Diyarbakır"]
    return render_template('home.html', berbers=berbershopList, citylist=citylist)


def statistics():
    return render_template('statistics.html')

def barbershop_view_edit():
    commentid = request.form["commentid"]
    commentidint = int(commentid)
    commenttitle = request.form["commenttitle"]
    commenttext  = request.form["commenttext"]
    dateTime = datetime.now()

    commentModel = CommentModel()
    commentModel.updateByIdTitleText(commentidint,commenttitle,commenttext,dateTime)

    return redirect(url_for("barbershop_view"))

def barbershop_view_delete():
    commentModel = CommentModel()
    commentModel.deleteById(int(request.form["commentid"]))
    return redirect(url_for("barbershop_view"))


def barbershop_view():
    if request.method == 'GET':
        #Get the list of the comment
        commentModel = CommentModel()
        commentlist = commentModel.getAllCommentswithPeople()

        for c in commentlist:
            c.dateTime = date(c.dateTime.year, c.dateTime.month, c.dateTime.day)

        return render_template("barbershopview.html", commentlist=commentlist)
    else:
        commentModel = CommentModel()

        berbershopid = request.form["bcommentselector"]
        commenttitle = request.form["bcommenttitle"]
        commenttext = request.form["bcommenttext"]
        commentrate = request.form["bcommentrate"]

        #save in database

        comment = Comment()
        comment.berber, comment.title, comment.content, comment.rate,comment.peopleId = int(berbershopid), commenttitle, commenttext,\
                                                                                        int(commentrate),1

        commentModel.save(comment)
        return redirect(url_for("barbershop_view"))



###########################################################



def blog_page():
    return render_template("blog.html", name="blog_page")


def profile_page():
    if request.method == 'POST':
        card_owner_name = request.form["name_surname"]
        card_number = request.form["number"]
        card_valid_date = request.form["date"]
        card_cvv = request.form["cvv"]
        print(card_owner_name + " " + card_number + " " + card_valid_date + " " + card_cvv)
    return render_template("profile.html")


def addcreditcard_page():
    return render_template("add_credit_card.html")

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
                return render_template("signin.html", message="True", role=people.get_role(username))
            else:
                return render_template("signin.html", message="False")
        else:
            return render_template("signin.html", message="False")

def signout():
    logout_user()
    return render_template("signin.html", message="s")

def admin_panel():
    if(current_user.role=="berber"):
        #Düzeltttt user yerine admin yazılacak !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        person = People()
        person.username="deneme"
        person.gender = "male"

        person2 = People()
        person2.username = "deneme2"
        person2.gender = "male"


        peoples = [person, person2]

        people = Peoplemodel()
        peoples = people.get_all_list()



        return render_template("admin_panel.html", people=peoples)
    else:
        return render_template("signin.html", message="admin_error")
