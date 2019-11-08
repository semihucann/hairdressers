from flask import render_template,Flask,request,redirect,url_for
import Temporarypython


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
        return render_template("signup_base.html")
    else:
        form_register_type = request.form["register_type"]
        form_mail = request.form["mail"]
        form_name_surname = request.form["name_surname"]
        form_username = request.form["username"]
        form_password = request.form["password"]
        form_gender = request.form["gender"]
        print(form_mail,form_name_surname, form_username, form_password, form_register_type,form_gender)

        if form_register_type=="type_user":
            return render_template("signup_user.html")
        elif form_register_type=="type_owner":
            return render_template("signup_owner.html")
        elif form_register_type=="type_berber":
            return render_template("signup_berber.html")
        else:
            return redirect(url_for("signupbase_page"))


def signup_user(username):
    print(username)
    return render_template("signup_user.html")