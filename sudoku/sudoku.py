"""Sudoku solver"""

from pprint import pprint
import warnings


def new_board():
    b = {
        f"{x+1}{y+1}": {
            "val": 0,
            "x": x + 1,
            "y": y + 1,
            "box": 1 + x // 3 + (y // 3) * 3,
        }
        for y in range(9)
        for x in range(9)
    }
    return b


def parse_board_string(s):
    b = new_board()
    s = s.replace(" ", "")
    for y in range(9):
        for x in range(9):
            b[f"{x+1}{y+1}"]["val"] = s[y * 9 + x]
    return b


def get_neighbours(t, b):
    neighbours = []
    target = b[t]
    for k, c in b.items():
        if k == t:
            pass
        if any(
            (c["x"] == target["x"], c["y"] == target["y"], c["box"] == target["box"])
        ):
            neighbours.append(k)
    return neighbours


def legal_board(b):
    for k, c in b.items():
        if c["val"] == ".":
            continue
        neighbours = get_neighbours(k, b)
        for n in neighbours:
            if k != n and c["val"] == b[n]["val"]:
                warnings.warn(f"[{k}: {c['val']}] = [{n}: {b[n]['val']}]")
                return False
    return True


def board_to_string(b, k="val"):
    s = ""
    for c in b.values():
        x = int(c["x"]) - 1
        y = int(c["y"]) - 1
        if x in [3, 6]:
            s += "|"
        s += str(c[k])
        if x == 8:
            s += "\n"
            if y in [3, 6]:
                s += "---|---|---\n"
    return s


def main():
    s = (
        "..4 6.. .3."
        ".5. 831 ..9"
        ".13 ... .27"
        ""
        "196 2.. ..3"
        ".4. .9. ..."
        ".3. .57 ..."
        ""
        "... ..5 9.2"
        "56. 9.8 ..."
        "... ... 1.."
    )

    board = parse_board_string(s)

    pprint(board, sort_dicts=False)

    print()
    print(board_to_string(board))
    print()
    print(board_to_string(board, "box"))
    print()
    print(board_to_string(board, "x"))
    print()
    print(board_to_string(board, "y"))
    print()
    print(legal_board(board))

    board["11"]["val"] = "4"
    print()
    print(board_to_string(board))
    print()
    print(legal_board(board))


if __name__ == "__main__":
    main()
