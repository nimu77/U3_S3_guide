from flask import Flask
from web_app.routes.home_route import home_route
from web_app.routes.bgg_route import bgg_route
from web_app.model import db, migrate


DATABASE_URL = "sqlite:///nimu_game.db"


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_route)
    app.register_blueprint(bgg_route)

    return app


### this is only if you don't have wsgi.py file.
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)