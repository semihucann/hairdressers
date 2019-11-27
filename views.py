from flask import render_template,Flask,request,redirect,url_for
import Temporarypython
from Models import Peoplemodel,CommentModel
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner
from passlib.hash import pbkdf2_sha256 as hasher


#Ertuğrul's Function

def home_page():
    berbershopList = Temporarypython.listOfBerbers()
    citylist = ["Istanbul", "Ankara", "Izmir", "Diyarbakır"]
    return render_template('home.html', berbers=berbershopList, citylist=citylist)

def statistics():
    return render_template('statistics.html')

def barbershop_view():
    if request.method == 'GET':
        #Get the list of the comment
        commentModel = CommentModel()
        commentlist = commentModel.getAll()
        return render_template("barbershopview.html",commentlist=commentlist)
    else:
        berbershopid = request.form["bcommentselector"]
        commenttitle = request.form["bcommenttitle"]
        commenttext = request.form["bcommenttext"]
        commentrate = request.form["bcommentrate"]

        #save in database
        commentModel = CommentModel()
        comment = Comment()
        comment.berber, comment.title, comment.content, comment.rate,comment.peopleId = int(berbershopid), commenttitle, commenttext,\
                                                                                        int(commentrate),1

        commentModel.save(comment)
        # Get the list of the comment
        commentModel = CommentModel()
        commentlist = commentModel.getAll()
        return render_template("barbershopview.html", commentlist=commentlist)

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


def signupbase_page():
    if request.method == 'GET':
        #signup_base dönüyordu
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
        if (people.save(person)):
            berber = Berber()
            berber.experience_year = request.form["experience"]
            berber.gender_choice = request.form["gender_choice"]
            berber.start_time = request.form["start_time"]
            berber.finish_time = request.form["finish_time"]
            print(berber.experience_year, berber.gender_choice, berber.start_time, berber.finish_time)
            return render_template("signup_berber.html", message="True")
        else:
            #Kayıt yapılamadı
            return render_template("signup_berber.html", message="False")

        return redirect(url_for("signup_berber_page"))

def signup_owner_page():
    if request.method == 'GET':
        return render_template("signup_owner.html")
    else:
        form_mail = request.form["mail"]
        form_name_surname = request.form["name_surname"]
        form_username = request.form["username"]
        form_password = request.form["password"]
        form_gender = request.form["gender"]
        form_tc = request.form["tc_number"]
        form_serial_number = request.form["serial_number"]
        form_vol_number = request.form["vol_number"]
        form_family_order_no = request.form["family_order_no"]
        form_order_no = request.form["order_no"]

        print(form_mail, form_name_surname, form_username, form_password, form_gender, form_tc, form_serial_number, form_vol_number, form_family_order_no, form_order_no)
        return redirect(url_for("home_page"))
        # uyarı metni yazmamız gerekiyor

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
        if(people.save(person)):
            #BERBER KAYDI EKLENECEK
            return render_template("signup_user.html", message="True")
        else:
            return render_template("signup_user.html", message="False")

        return redirect(url_for("signup_user_page"))


def signin():
    return render_template("signin.html")