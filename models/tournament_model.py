from .round import Round
from datetime import datetime

class Tournament:
    def __init__(self, name, location, date, nb_rounds=4, time_control="Blitz", description=""):
        self.name = name
        self.location = location
        self.date = date
        self.nb_rounds = nb_rounds
        self.time_control = time_control
        self.description = description
        self.players = []  # list of Player instances
        self.rounds = []   # list of Round instances

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_obj):
        self.rounds.append(round_obj)

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'nb_rounds': self.nb_rounds,
            'time_control': self.time_control,
            'description': self.description,
            'players': [p.to_dict() for p in self.players],
            'rounds': [r.to_dict() for r in self.rounds]
        }

    @classmethod
    def from_dict(cls, data):
        from .player import Player
        from .round import Round
        t = cls(data['name'], data['location'], data['date'], data['nb_rounds'], data['time_control'], data['description'])
        t.players = [Player.from_dict(p) for p in data['players']]
        t.rounds = [Round.from_dict(r) for r in data['rounds']]
        return t
