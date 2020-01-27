from app.board.board import Board
import random


class GeneratePositions:
    def __init__(self, board):
        self.board = Board('', '').board

    def generate_position(self):
        string = 'abcdefghij'
        random_number = random.randint(0, 9)
        random_string = random.choice(string)
        join_random = random_string + str(random_number)
        return join_random

