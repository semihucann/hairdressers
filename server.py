from flask import Flask
import views


def create_app():
    app2 = Flask(__name__)
    app2.add_url_rule("/", view_func=views.home_page)
    app2.add_url_rule("/statistics",view_func=views.statistics)
    app2.add_url_rule("/berbershopview",view_func=views.berbershop_view)
    app2.add_url_rule("/blog", view_func=views.blog_page)
    app2.add_url_rule("/profile", view_func=views.profile_page, methods=["GET", "POST"])
    app2.add_url_rule("/addcreditcard", view_func=views.addcreditcard_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup", view_func=views.signupbase_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_berber", view_func=views.signup_berber_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_owner", view_func=views.signup_owner_page, methods=["GET", "POST"])
    app2.add_url_rule("/signup_user", view_func=views.signup_user_page, methods=["GET", "POST"])
    app2.add_url_rule("/signin", view_func=views.signin)

    app2.config["DEBUG"] = True
    return app2


app = create_app()


if __name__ == "__main__":
    #port = app.config.get("PORT", 5000)
    #app.run(host="0.0.0.0", port=port)
    app.run()