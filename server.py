from flask import Flask
import views


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/blog", view_func=views.blog_page)
    app.add_url_rule("/profile", view_func=views.profile_page, methods=["GET", "POST"])
    app.add_url_rule("/addcreditcard", view_func=views.addcreditcard_page, methods=["GET", "POST"])
    app.add_url_rule("/signup", view_func=views.signupbase_page, methods=["GET", "POST"])

    app.config["DEBUG"] = True
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
