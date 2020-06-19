from flask import Blueprint, render_template
from web_app.model import db, Game
import requests
import bs4
import pdb
import numpy as np


bgg_route = Blueprint("bgg_route", __name__)

@bgg_route.route("/add/<game_id>")
def get_game(game_id=None):
    print(game_id)

    url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + game_id
    result = requests.get(url)
    print("---------")
    print(url)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    game_id = game_id  #Game.query.get(game.id) or 
    game_name = soup.find('name').text
    game_maxplayers = int(soup.find('maxplayers').text)

    db_game = Game(id=game_id, name=game_name, max_players=game_maxplayers)


    db.session.add(db_game)
    db.session.commit()
    
    return 'OK'

@bgg_route.route("/reset")
def reset():
    db.session.query(Game).delete()
    db.session.commit()
    return "OK"


# @bgg_route.route("/random")
# def random_game():
#     list_game = list(Game.query.all())
#     r_game = np.random.choice(list_game)
  
#     return render_template("index.html",
#         r_game_name=r_game.name,
#         r_game_id=r_game.id,
#         r_max_players=r_game.max_players,
#     )

  # return f'Game Name: {r_game.name} Game ID:{str(r_game.id)} Max Players:{str(r_game.max_players)}'
