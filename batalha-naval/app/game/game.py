from app.player.player import Player
from app.move.move import Move


class Game:

    def __init__(self, player, move, start_game):
        self.player = Player('move', ['louyza', 'isabel']).players()
        self.move = Move('', '', '', '', '')

    def start_game(self):
        pass


