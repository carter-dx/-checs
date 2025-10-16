from tinydb import TinyDB
from models.tournament_model import Tournament

db = TinyDB("db.json")
tournaments_table = db.table("tournaments")

def save_tournaments(tournaments):
    serialized = [t.serialize() for t in tournaments]
    tournaments_table.truncate()
    tournaments_table.insert_multiple(serialized)

def load_tournaments():
    serialized = tournaments_table.all()
    return [Tournament.deserialize(data) for data in serialized]
