class Spreadsheet:
    def __init__(self, rows: int):
        self.cells: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")
        return self._value(left) + self._value(right)

    def _value(self, token: str) -> int:
        if token[0].isdigit():
            return int(token)
        return self.cells.get(token, 0)
