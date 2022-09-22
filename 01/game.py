"""
This module is my tic tac game. The players type in console number of line and column. If the field
on the board is empty, the symbol is put there. If the field is occupied, then you need to select
another one. Game will end after filling all fields.
"""


class TicTacGame:
    """
    Class of the TicTac game
    """

    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]

    def show_board(self):
        """
        Print the board
        :return: Nothing
        """
        for i in range(3):
            print("       |       |       ")
            print(f"   {self.board[i][0]}   |   {self.board[i][1]}   |   {self.board[i][2]}")
            if i != 2:
                print("_______|_______|_______")
            else:
                print("       |       |       ")

    def validate_input_and_add(self, input_data, symbol):
        """
        :param input_data: string with two int numbers and 'X' or 'O' which are separated by space
        :param symbol: 'O' or 'X'
        :return: True if input data is correct and some message if data is incorrect
        """
        if symbol not in ['X', 'O']:
            return 'Incorrect symbol'
        input_symbols = input_data.split()
        if input_symbols[0].isnumeric() and input_symbols[1].isnumeric():
            if 1 <= int(input_symbols[0]) <= 3 and 1 <= int(input_symbols[1]) <= 3:
                if self.board[int(input_symbols[0]) - 1][int(input_symbols[1]) - 1] == ' ':
                    self.board[int(input_symbols[0]) - 1][int(input_symbols[1]) - 1] = symbol
                    return True
                return 'This field is already occupied by another player. \nTry again!'
            return 'Incorrect input format: the numbers must be integers from 1 to 3. \nTry again!'
        return 'Incorrect input format: integers are needed! \nTry again!'

    def check_winner(self):
        """
        :return: True if there is winner and False if not
        """
        for i in range(3):
            row = self.board[i]
            column = [row[i] for row in self.board]
            main_diagonal = [self.board[i][i] for i in range(3)]
            side_diagonal = [self.board[2 - i][i] for i in range(3)]
            if row in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True
            if column in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True
            if main_diagonal in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True
            if side_diagonal in (['X', 'X', 'X'], ['O', 'O', 'O']):
                return True
        return False

    def start_game(self):
        """
        :return: The winners symbols if there is one winner and 'Draw' if there is none
        """
        print("Welcome to the TicTacGame.\n"
              "The format of input data: 'number_of_line number_of_column'")
        i = 1
        while True:
            symbol = 'X' if i % 2 == 1 else 'O'
            print(f'Time for {symbol}')
            validation_result = self.validate_input_and_add(input(), symbol)
            if isinstance(validation_result, str):
                print(validation_result)
                continue
            self.show_board()
            if i >= 5:
                result = self.check_winner()
                if result:
                    print(f"Winner is {symbol}!")
                    return symbol
            i += 1
            if i == 9:
                break
        print("Draw")
        return 'Draw'


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
