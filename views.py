from flask import render_template,Flask,request,redirect,url_for
import Temporarypython
from Models import Peoplemodel
from Entities import Comment, ContactInfo, Rezervation, People, Berber, Owner

def home_page():
    berbershopList = Temporarypython.listOfBerbers()
    citylist = ["Istanbul", "Ankara", "Izmir", "Diyarbakır"]
    return render_template('home.html', berbers=berbershopList, citylist=citylist)


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
        form_mail = request.form["mail"]
        form_name_surname = request.form["name_surname"]
        form_username = request.form["username"]
        form_password = request.form["password"]
        form_gender = request.form["gender"]
        form_experince_year = request.form["experience"]
        form_gender_choice = request.form["gender_choice"]
        form_start_time = request.form["start_time"]
        form_finish_time = request.form["finish_time"]
        print(form_mail, form_name_surname, form_username, form_password, form_gender, form_experince_year, form_gender_choice, form_start_time, form_finish_time)
        return redirect(url_for("home_page"))
        #uyarı metni yazmamız gerekiyor


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
        return render_template("signup_user.html")
    else:
        person = People()
        person.username = request.form["username"]
        person.name_surname = request.form["name_surname"]
        person.mail = request.form["mail"]
        person.password_hash = request.form["password"]
        person.gender = request.form["gender"]
        person.age = request.form["age"]
        person.role = "user"
        #print(person.username, person.name_surname, person.mail, person.password_hash, person.gender, person.age, person.role)
        people = Peoplemodel()
        people.insert(person)




        return redirect(url_for("home_page"))
        # uyarı metni yazmamız gerekiyor


def signin():
    return render_template("signin.html")