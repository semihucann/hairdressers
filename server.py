from flask import Flask
import views

def create_app():
    app = Flask(__name__)
    app.add_url_rule("/",view_func=views.home_page)
    app.add_url_rule("/blog",view_func=views.blog_page)
    app.add_url_rule("/profile",view_func=views.profile_page)

    app.config["DEBUG"] = True
    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT" ,5000)
    app.run(host="0.0.0.0", port=port)