"""
A module for testing tictac game by pytest
"""

import random
import pytest
import mock

WELCOME_MESSAGE = "Welcome to the TicTacGame.\nThe format of input data: 'number_of_line " \
                  "number_of_column'"


def fill_the_board(input_data, board):
    """
    :param input_data: input players picks of fields
    :param board: 2d list 3 x 3 to be used for board of my game
    :return: board
    """
    i = 1
    for data in input_data:
        symbol = 'X' if i % 2 == 1 else 'O'
        ind = data.split()
        board[int(ind[0]) - 1][int(ind[1]) - 1] = symbol
        i += 1
    return board


class TestMyGame:
    """
    Test class
    """
    input_type_error = 'Incorrect input format: integers are needed! \nTry again!'
    input_range_error = 'Incorrect input format: the numbers must be integers from 1 to 3. ' \
                        '\nTry again!'
    input_occupation_error = 'This field is already occupied by another player. \nTry again!'
    input_number_of_int_error = 'Incorrect input format: you need to enter exactly 2 numbers: ' \
                                'row number and column number.\nTry again!'

    @pytest.mark.parametrize('input_data, expected', [(['1 1', '2 1', '2 2', '3 1', '3 3'], 'X'),
                                                      (['1 2', '1 1', '2 3', '2 2', '3 1',
                                                        '3 3'], 'O'),
                                                      (['3 1', '1 1', '2 2', '2 1', '1 3'], 'X'),
                                                      (['1 1', '3 1', '2 1', '2 2', '1 2',
                                                        '1 3'], 'O'),
                                                      (['1 1', '2 2', '1 2', '2 1', '1 3'], 'X'),
                                                      (['2 1', '1 2', '2 2', '1 1', '2 3'], 'X'),
                                                      (['3 1', '1 2', '3 2', '1 1', '3 3'], 'X'),
                                                      (['2 2', '1 2', '2 1', '1 3', '3 1',
                                                        '1 1'], 'O'),
                                                      (['1 2', '2 1', '1 3', '2 2', '3 1',
                                                        '2 3'], 'O'),
                                                      (['1 3', '3 1', '1 1', '3 2', '2 1',
                                                        '3 3'], 'O'),
                                                      (['1 1', '2 2', '2 1', '2 3', '3 1'], 'X'),
                                                      (['2 1', '3 2', '2 2', '1 3', '2 3'], 'X'),
                                                      (['3 1', '2 2', '3 2', '2 3', '3 3'], 'X'),
                                                      (['1 3', '1 1', '2 2', '2 1', '2 3',
                                                        '3 1'], 'O'),
                                                      (['1 3', '1 1', '2 2', '2 1', '2 3',
                                                        '3 1'], 'O'),
                                                      (['1 3', '1 1', '2 2', '2 1', '2 3',
                                                        '3 1'], 'O')
                                                      ])
    def test_victory_case(self, my_game, input_data, expected, capfd):
        """
        Checks the vistory case of start_game method
        :param my_game: tic_tac game class from fixture
        :param input_data: input players picks of fields
        :param expected: 'O' or 'X"
        :param capfd: pytest fixture for using std out
        :return: nothing
        """
        with mock.patch('builtins.input', side_effect=input_data):
            assert my_game.start_game() == expected
            out = capfd.readouterr()[0]
            assert WELCOME_MESSAGE in out
            assert "Time for X" in out
            assert "Time for O" in out
            assert f"Winner is {expected}!" in out

    def test_draw_case(self, my_game, capfd):
        """
        Checks the draw case of the start_game method
        :param my_game: tic_tac game class from fixture
        :param capfd: pytest fixture for using std out
        :return: nothing
        """
        input_data = ['1 1', '1 2', '1 3', '2 1', '2 2', '3 3', '2 3', '3 1', '3 2']
        with mock.patch('builtins.input', side_effect=input_data):
            assert my_game.start_game() == 'Draw'
            out = capfd.readouterr()[0]
            assert WELCOME_MESSAGE in out
            assert "Time for X" in out
            assert "Time for O" in out
            assert "Draw" in out

    @pytest.mark.parametrize('input_data, expected', [(['some_string some_string', 'X'],
                                                       input_type_error),
                                                      (['some_string 3', 'X'], input_type_error),
                                                      (['3 some_string', 'X'], input_type_error),
                                                      (['3 3', 'X'], True),
                                                      (['3 3', 'O'], True),
                                                      (['1 6', 'X'], input_range_error),
                                                      (['6 6', 'X'], input_range_error),
                                                      (['6 1', 'X'], input_range_error),
                                                      (['6', 'X'], input_number_of_int_error),
                                                      (['6', 'O'], input_number_of_int_error),
                                                      (['1 \u00b9', 'X'], input_type_error),
                                                      (['\u00b9 \u00b9', 'X'], input_type_error),
                                                      (['\u00b9 1', 'X'], input_type_error),
                                                      (['\u00b9 1', 'X'], input_type_error),
                                                      (['\u00b9 \u00b9', 'X'], input_type_error),
                                                      (['1 \u00b9', 'X'], input_type_error)])
    def test_validation_range_and_format(self, my_game, input_data, expected):
        """
        Checks validation method in case of incorrect input
        :param my_game: tic_tac game class from fixture
        :param input_data: one players pick of field
        :param expected: error message
        :return: nothing
        """
        assert my_game.validate_input_and_add(input_data[0], input_data[1]) == expected

    @pytest.mark.parametrize('first_symbol, second_symbol, expected',
                             [('X', 'O', input_occupation_error),
                              ('O', 'X', input_occupation_error)])
    def test_validation_occupation(self, my_game, first_symbol, second_symbol, expected):
        """
        Tests validation method in case, when player picks already filled field
        :param my_game: tic_tac game class from fixture
        :param first_symbol: 'O' or 'X'
        :param second_symbol: 'O' or 'X'
        :param expected: error message
        :return: nothing
        """
        line, column = random.randint(1, 3), random.randint(1, 3)
        input_data = str(line) + ' ' + str(column)
        my_game.validate_input_and_add(input_data, first_symbol)
        assert my_game.validate_input_and_add(input_data, second_symbol) == expected

    @pytest.mark.parametrize('input_data,  expected', [(['1 1', '2 1', '2 2', '3 1', '3 3'], True),
                                                       (['3 1', '1 1', '2 2', '2 1', '1 3'], True),
                                                       (['1 1', '2 2', '1 2', '2 1', '1 3'], True),
                                                       (['2 1', '1 2', '2 2', '1 1', '2 3'], True),
                                                       (['3 1', '1 2', '3 2', '1 1', '3 3'], True),
                                                       (['1 1', '2 2', '2 1', '2 3', '3 1'], True),
                                                       (['2 1', '3 2', '2 2', '1 3', '2 3'], True),
                                                       (['3 1', '2 2', '3 2', '2 3', '3 3'], True),
                                                       (['1 3'], False),
                                                       (['1 1', '1 2', '1 3', '2 1', '2 2', '3 3',
                                                         '2 3', '3 1', '3 2'], False),
                                                       ])
    def test_winner_checker(self, my_game, input_data, expected):
        """
        Checks check_winner method of tictac game class
        :param my_game: tic_tac game class from fixture
        :param input_data: input players picks of fields
        :param expected: True of False
        :return: nothing
        """
        my_game.board = fill_the_board(input_data, my_game.board)
        assert my_game.check_winner() == expected

    @pytest.mark.parametrize('input_data', [(['1 1', '1 2', '1 3', '2 1', '2 2', '3 3',
                                              '2 3', '3 1', '3 2']),
                                            (['1 1']),
                                            ([])
                                            ])
    def test_draw_board(self, my_game, capfd, input_data):
        """
        Сhecks for console output
        :param my_game: tic_tac game class from fixture
        :param capfd: pytest fixture for using std out
        :param input_data: input players picks of fields
        :return: nothing
        """
        my_game.board = fill_the_board(input_data, my_game.board)
        my_game.show_board()
        out = capfd.readouterr()[0]
        assert out
