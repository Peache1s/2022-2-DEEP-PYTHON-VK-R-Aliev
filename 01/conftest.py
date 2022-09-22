"""
A module for pytest fixtures
"""
import pytest
from game import TicTacGame


@pytest.fixture()
def my_game():
    """
    fixture for create tictac game object
    :return: object of tictac game
    """
    tic_tac_game = TicTacGame()
    return tic_tac_game
