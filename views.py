from flask import render_template,Flask
import Temporarypython


def home_page():
    berbershopList = Temporarypython.listOfBerbers()
    return render_template('home.html', berbers=berbershopList)


def blog_page():
    return render_template("blog.html", name="blog_page")


def profile_page():
    return render_template("profile.html")
