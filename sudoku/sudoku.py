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
            "options": "123456789",
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


def prune_options(t, b, set_one=True):
    target = b[t]
    if target["val"] in "123456789":
        return target["val"], []
    neighbours = get_neighbours(t, b)
    causes = list()
    for k in neighbours:
        if b[k]["val"] in target["options"]:
            target["options"] = target["options"].replace(b[k]["val"], "")
            causes.append((k, b[k]["val"]))
    if set_one and len(target["options"])==1:
        target["val"] = target["options"]
    return target["options"], causes


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


def completed_board(b):
    return all([b[k]["val"] in "123456789" for k in b]) and legal_board(b)


def board_to_string(b, k="val"):
    s = ""
    for c in b.values():
        x = int(c["x"])
        y = int(c["y"])
        s += str(c[k])
        if x in [3, 6]:
            s += "|"
        if x == 9:
            s += "\n"
            if y in [3, 6]:
                s += "---|---|---\n"
    return s


def tree(t, b, depth=2):
    """Brute force"""


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

    s = (
        ".2. 6.4 3.7"
        ".4. ... 1.."
        "8.7 .5. ..."
        ".7. .9. .61"
        "6.. 5.2 ..4"
        "59. .7. .3."
        "... .2. 4.3"
        "..2 ... .8."
        "4.9 8.3 .2."
    )

    s = (
        "6.5 ..2 ..7"
        "..7 .9. 2.3"
        "2.8 ..6 54."
        "... .3. 8.."
        ".1. 428 .5."
        "..6 .1. ..."
        ".84 9.. 7.1"
        "9.2 .8. 4.."
        "3.. 2.. 6.8"
    )

    board = parse_board_string(s)
    print(legal_board(board))

    #pprint(board, sort_dicts=False)

    print()
    print(board_to_string(board))
    #print()
    #print(board_to_string(board, "box"))
    #print()
    #print(board_to_string(board, "x"))
    #print()
    #print(board_to_string(board, "y"))
    #print()
    #print(legal_board(board))

    #board["11"]["val"] = "4"
    #print()
    #print(board_to_string(board))
    #print()
    #print(legal_board(board))

    #pprint(prune_options("11", board))


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

if __name__ == "__main__":
    main()
