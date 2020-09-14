from sudoku.io import web
from sudoku.sudoku import *


def main():
    pass


if __name__ == "__main__":
    string = web.get_string()
    board = parse_board_string(string)
    print(board_to_string(board))
    print(legal_board(board))

    for i in range(20):
        if i>100 or completed_board(board):
            break
        print(f"\n{i+1}\n---")
        for y in range(1, 10):
            for x in range(1, 10):
                k = f"{x}{y}"
                prune_options(k, board)
        print(board_to_string(board))
        print(legal_board(board))

