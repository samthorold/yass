class Board:
    """Sudoku board.

    >>> Board()
    <Board(name=None)>
    >>> b = Board()
    >>> b.setup()

    """

    def __init__(self, name=None, regions=None, cells=None):
        self.name = name
        self.regions = regions if regions is not None else []
        self.cells if cells is not None else []

    def __repr__(self):
        return f"<Board(name={self.name})>"

    def setup(self):
        cols = [Region(str(i)) for i in range(1, 10)]
        rows = [Region(str(i)) for i in range(1, 10)]
        boxs = [Region(str(i)) for i in range(1, 10)]

        for i, col in enumerate(cols):
            for j, row in enumerate(rows):
                boxi = i // 3 + (j // 3) * 3
                cell = Cell(f"row={j+1}, col={i+1}, box={boxi+1}")
                # print(cell)
                col.add_cell(cell)
                row.add_cell(cell)
                boxs[boxi].add_cell(cell)


class Region:
    """Region of Cells in a sudoku board.

    >>> Region()
    <Region(name=None)>

    """

    def __init__(self, name=None, cells=None):
        self.name = name
        self.cells = cells if cells is not None else []

    def __repr__(self):
        return f"<Region(name={self.name})>"

    def add_cell(self, cell):
        self.cells.append(cell)
        cell.regions.append(self)


class Cell:
    """Cell in a sudoku board.

    >>> Cell()
    <Cell(name=None, val=None, poss=123456789)>

    """

    def __init__(self, val=None, poss=None, regions=None, name=None):
        self.val = val
        self.poss = poss if poss is not None else set(range(1, 10))
        self.regions = regions if regions is not None else []
        self.name = name

    def __repr__(self):
        poss = "".join(str(p) for p in self.poss)
        return f"<Cell(name={self.name}, val={self.val}, poss={poss})>"


if __name__ == "__main__":
    b = Board()
    b.setup()
