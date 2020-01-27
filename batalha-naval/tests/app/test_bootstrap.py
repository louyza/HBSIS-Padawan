import unittest
from unittest.mock import patch, Mock
from app.bootstrap import StartUp
from app.board.board import Board
from app.game.game import Game
from app.generate_positions import generate_positions
from app.move.move import Move
from app.player.player import Player
from app.strategy.strategy import Strategy


class TestBootstrap(unittest.TestCase):
    def test_call_execute(self):
        bootstrap = StartUp()
        bootstrap.execute()
        self.assertIsInstance(bootstrap, StartUp)

    @patch.object(Board, 'create_board')
    def test_bootstrap_called_create_board(self, mock_create_board):
        board = Board(Mock, Mock)
        board.create_board()

        mock_create_board.assert_called_once()

    @patch.object(Strategy, 'right_move_player_one')
    def test_bootstrap_callend_right_move_player_one(self, mock_right_move_player_one):
        strategy = Strategy(Mock, Mock, Mock)
        strategy.right_move_player_one(Mock)

        mock_right_move_player_one.assert_called_once()