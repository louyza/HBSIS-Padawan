from app.board.board import Board
from app.player.player import Player
import emoji


class Strategy:

    def __init__(self, move_player_one, move_player_two,  player):
        self.move_player_one = Board('', '').board
        self.move_player_two = Board('', '').board
        self.player = Player('a1', ['gaby', 'louyza']).players()

    def right_move_player_one(self, tactics: list):
        for i in self.move_player_one:
            for j in range(len(tactics)):
                if tactics[j] in self.move_player_one:
                    self.move_player_one = self.move_player_one.replace(tactics[j], emoji.emojize(":speedboat:"))
            return f"Turn's player : {self.player[0]} \n{self.move_player_one}"

            break

    def right_move_player_two(self, tactics: list):
        for i in self.move_player_two:
            for j in range(len(tactics)):
                if tactics[j] in self.move_player_two:
                    self.move_player_two = self.move_player_two.replace(tactics[j], emoji.emojize(":speedboat:"))
            return f"Turn's player : {self.player[1]} \n{self.move_player_two}"
            break
