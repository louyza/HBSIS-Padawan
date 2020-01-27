from app.board.board import Board
from app.player.player import Player
from app.strategy.strategy import Strategy
from app.generate_positions.generate_positions import GeneratePositions
import emoji
import re
from pprint import pprint


class Move:

    def __init__(self, board, strategy_player_one, strategy_player_two, generate_positions_one, generate_positions_two):
        self.player = Player(Move, ['gaby', 'isabel']).players()
        self.board = Board('', '').board
        self.strategy_player_one = Strategy('g4', 'a4', 'b5').move_player_one
        self.strategy_player_two = Strategy('j1', 'i2', 'e3').move_player_two
        self.generate_positions = GeneratePositions(self.board).generate_position()
        self.generate_positions_one = GeneratePositions(self.board).generate_position()
        self.generate_positions_two = GeneratePositions(self.board).generate_position()

    def get_move_player_one(self):
        for i in self.strategy_player_one:
            for j in range(len(i)):
                if self.generate_positions_one in self.strategy_player_one[j]:
                    self.strategy_player_one = f'{self.strategy_player_one}'.replace('[', '').replace(']', '').replace("'", '')
                    self.strategy_player_one = f'{self.strategy_player_one}'.replace(self.generate_positions_one, emoji.emojize(":speedboat:")).replace('[', '').replace(']', '')
                    print(f"Turn's player {self.player[0]}")
                    pprint(self.strategy_player_one)
                    break
                else:
                    self.strategy_player_one = f'{self.strategy_player_one}'.replace('[', '').replace(']', '').replace("'", '')
                    self.strategy_player_one = f'{self.strategy_player_one}'.replace(self.generate_positions_one, emoji.emojize(":bomb:"))
                    print(f"Turn's player {self.player[0]}")
                    pprint(self.strategy_player_one)
                    break
            break

    def get_move_player_two(self):
        for i in self.strategy_player_two:
            for j in range(len(i)):
                if self.generate_positions_two in self.strategy_player_two[j]:
                    self.strategy_player_two = f'{self.strategy_player_two}'.replace('[', '').replace(']', '').replace("'", '')
                    self.strategy_player_two = f'{self.strategy_player_two}'.replace(self.generate_positions_two, emoji.emojize(":speedboat:"))
                    print(f"Turn's player {self.player[1]}")
                    pprint(self.strategy_player_two)
                    break
                else:
                    self.strategy_player_two = f'{self.strategy_player_two}'.replace('[', '').replace(']', '').replace("'", '')
                    self.strategy_player_two = f'{self.strategy_player_two}'.replace(self.generate_positions_two, emoji.emojize(":bomb:"))
                    print(f"Turn player {self.player[1]}")
                    pprint(self.strategy_player_two)
                    break
            break
























