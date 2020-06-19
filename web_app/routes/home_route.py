from flask import Blueprint, render_template
from web_app.model import Game
import numpy as np

home_route = Blueprint("home_route", __name__)

# @home_route.route("/")
# def our_home():
#     return render_template("index.html")
@home_route.route("/")
def random_game():
    list_game = list(Game.query.all())
    r_game = np.random.choice(list_game)
  
    return render_template("index.html",
        r_game_name=r_game.name,
        r_game_id=r_game.id,
        r_max_players=r_game.max_players,
    )

@home_route.route("/hello")
def hello():
    return "Hello World"