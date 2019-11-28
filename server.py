from flask import Flask
import views
from flask_login import LoginManager
import Models

import os

url = os.getenv("DATABASE_URL")
lm = LoginManager()


@lm.user_loader
def load_user(user_id):
    people = Models.Peoplemodel()
    return people.get_all(user_id)

def create_app():
    app2 = Flask(__name__)
    app2.secret_key = 'super secret key'
    app2.add_url_rule("/", view_func=views.home_page)
    app2.add_url_rule("/statistics",view_func=views.statistics)
    app2.add_url_rule("/barbershopview",view_func=views.barbershop_view, methods=["GET", "POST"])
    app2.add_url_rule("/barbershopview/edit",view_func=views.barbershop_view_edit, methods=["POST"])
    app2.add_url_rule("/barbershopview/delete", view_func=views.barbershop_view_delete, methods=["POST"])
    app2.add_url_rule("/blog", view_func=views.blog_page)
    app2.add_url_rule("/profile", view_func=views.profile_page, methods=["GET", "POST"])
    app2.add_url_rule("/addcreditcard", view_func=views.addcreditcard_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup", view_func=views.signupbase_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_berber", view_func=views.signup_berber_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_owner", view_func=views.signup_owner_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_user", view_func=views.signup_user_page, methods=["GET", "POST"])
    app2.add_url_rule("/signin", view_func=views.signin, methods=["GET", "POST"])
    app2.add_url_rule("/signout", view_func=views.signout)
    app2.add_url_rule("/admin_panel", view_func=views.admin_panel)

    lm.init_app(app2)
    lm.login_view = "login_page"

    app2.config["DEBUG"] = True
    return app2


app = create_app()


if __name__ == "__main__":
    #port = app.config.get("PORT", 5000)
    #app.run(host="0.0.0.0", port=port)
    app.run()