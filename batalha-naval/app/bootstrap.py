from app.board.board import Board
from app.move.move import Move
from app.player.player import Player
from app.strategy.strategy import Strategy
from app.generate_positions.generate_positions import GeneratePositions


class StartUp:

    def execute(self):
        board = Board('navio', 'a1')
        strategy = Strategy('12', 'a1', ['isabel', 'louyza'])
        strategy.right_move_player_one(['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'])
        strategy.right_move_player_two(['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'])
        generate_positions = GeneratePositions('board')
        move = Move('board', strategy, strategy, generate_positions, generate_positions)
        move.get_move_player_one()
        move.get_move_player_two()
        Player('', ['gaby', 'isabel']).players()
