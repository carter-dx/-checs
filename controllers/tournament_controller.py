from tinydb import TinyDB
from models.player import Player
from models.tournament_model import Tournament
from models.round import Round

db = TinyDB("db.json")
players_table = db.table("players")
tournaments_table = db.table("tournaments")

def save_players(players):
    players_table.truncate()
    serialized_players = [p.to_dict() for p in players]
    players_table.insert_multiple(serialized_players)

def load_players():
    serialized_players = players_table.all()
    return [Player.from_dict(p) for p in serialized_players]

def save_tournaments(tournaments):
    tournaments_table.truncate()
    serialized = [t.to_dict() for t in tournaments]
    tournaments_table.insert_multiple(serialized)

def load_tournaments():
    serialized = tournaments_table.all()
    return [Tournament.from_dict(t) for t in serialized]
