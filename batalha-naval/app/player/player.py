class Player:

    def __init__(self, move, nickname: list):
        self.move = move
        self.nickname = nickname

    def players(self):
        return self.nickname
