from datetime import datetime

class Round:
    def __init__(self, name, matches=None):
        self.name = name
        self.matches = matches or []  # list of tuples [(player1, score1), (player2, score2)]
        self.start_time = datetime.now()
        self.end_time = None

    def end_round(self):
        self.end_time = datetime.now()

    def add_match(self, player1, player2, score1=0, score2=0):
        self.matches.append([(player1, score1), (player2, score2)])

    def to_dict(self):
        return {
            'name': self.name,
            'matches': [
                [{'player': p.to_dict(), 'score': s} for p, s in match]
                for match in self.matches
            ],
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None
        }

    @classmethod
    def from_dict(cls, data):
        from .player import Player
        round_obj = cls(data['name'])
        round_obj.start_time = datetime.fromisoformat(data['start_time'])
        round_obj.end_time = datetime.fromisoformat(data['end_time']) if data['end_time'] else None
        for match in data['matches']:
            p1_data = match[0]['player']
            p2_data = match[1]['player']
            score1 = match[0]['score']
            score2 = match[1]['score']
            from .player import Player
            p1 = Player.from_dict(p1_data)
            p2 = Player.from_dict(p2_data)
            round_obj.add_match(p1, p2, score1, score2)
        return round_obj
