class Player:
    def __init__(self, first_name, last_name, birth_date, sex, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.ranking = ranking
        self.score = 0

    def add_score(self, points):
        self.score += points

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'sex': self.sex,
            'ranking': self.ranking,
            'score': self.score
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(
            data['first_name'],
            data['last_name'],
            data['birth_date'],
            data['sex'],
            data['ranking']
        )
        player.score = data.get('score', 0)
        return player

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Score: {self.score}, Ranking: {self.ranking}"
