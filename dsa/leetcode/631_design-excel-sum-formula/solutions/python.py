from collections import Counter, defaultdict


Cell = tuple[int, int]


class Excel:
    def __init__(self, height: int, width: str):
        self._values = [[0] * (ord(width) - ord("A") + 1) for _ in range(height)]
        self._formulas: dict[Cell, Counter[Cell]] = {}
        self._dependents: dict[Cell, Counter[Cell]] = defaultdict(Counter)

    @staticmethod
    def _cell(reference: str) -> Cell:
        return int(reference[1:]) - 1, ord(reference[0]) - ord("A")

    def _references(self, references: list[str]) -> Counter[Cell]:
        result: Counter[Cell] = Counter()
        for reference in references:
            endpoints = reference.split(":")
            top, left = self._cell(endpoints[0])
            bottom, right = self._cell(endpoints[-1])
            for row in range(top, bottom + 1):
                for column in range(left, right + 1):
                    result[row, column] += 1
        return result

    def _remove_formula(self, cell: Cell) -> None:
        formula = self._formulas.pop(cell, None)
        if formula is None:
            return
        for source, multiplicity in formula.items():
            targets = self._dependents[source]
            targets[cell] -= multiplicity
            if targets[cell] == 0:
                del targets[cell]
            if not targets:
                del self._dependents[source]

    def _propagate(self, cell: Cell, difference: int) -> None:
        if difference == 0:
            return
        for target, multiplicity in list(self._dependents.get(cell, {}).items()):
            change = difference * multiplicity
            row, column = target
            self._values[row][column] += change
            self._propagate(target, change)

    def set(self, row: int, column: str, value: int) -> None:
        cell = row - 1, ord(column) - ord("A")
        old_value = self._values[cell[0]][cell[1]]
        self._remove_formula(cell)
        self._values[cell[0]][cell[1]] = value
        self._propagate(cell, value - old_value)

    def get(self, row: int, column: str) -> int:
        return self._values[row - 1][ord(column) - ord("A")]

    def sum(self, row: int, column: str, references: list[str]) -> int:
        cell = row - 1, ord(column) - ord("A")
        old_value = self._values[cell[0]][cell[1]]
        self._remove_formula(cell)

        formula = self._references(references)
        value = sum(
            self._values[source[0]][source[1]] * multiplicity
            for source, multiplicity in formula.items()
        )
        self._formulas[cell] = formula
        for source, multiplicity in formula.items():
            self._dependents[source][cell] += multiplicity

        self._values[cell[0]][cell[1]] = value
        self._propagate(cell, value - old_value)
        return value


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    excel: Excel | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "Excel":
            excel = Excel(*args)
            output.append(None)
        elif operation == "set":
            excel.set(*args)
            output.append(None)
        elif operation == "get":
            output.append(excel.get(*args))
        else:
            output.append(excel.sum(*args))
    return output
