class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
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


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    spreadsheet: Spreadsheet | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "Spreadsheet":
            spreadsheet = Spreadsheet(int(args[0]))
            output.append(None)
        elif operation == "setCell":
            assert spreadsheet is not None
            spreadsheet.setCell(str(args[0]), int(args[1]))
            output.append(None)
        elif operation == "resetCell":
            assert spreadsheet is not None
            spreadsheet.resetCell(str(args[0]))
            output.append(None)
        elif operation == "getValue":
            assert spreadsheet is not None
            output.append(spreadsheet.getValue(str(args[0])))
    return output
