from collections import Counter, defaultdict
from typing import List


class Excel:
    def __init__(self, height: int, width: str):
        self.values = [[0] * (ord(width) - ord("A") + 1) for _ in range(height)]
        self.formulas = {}
        self.dependents = defaultdict(Counter)

    def cell(self, reference):
        return int(reference[1:]) - 1, ord(reference[0]) - ord("A")

    def references(self, references):
        result = Counter()
        for reference in references:
            endpoints = reference.split(":")
            top, left = self.cell(endpoints[0])
            bottom, right = self.cell(endpoints[-1])
            for row in range(top, bottom + 1):
                for column in range(left, right + 1):
                    result[row, column] += 1
        return result

    def remove_formula(self, cell):
        formula = self.formulas.pop(cell, None)
        if formula is None:
            return
        for source, multiplicity in formula.items():
            targets = self.dependents[source]
            targets[cell] -= multiplicity
            if targets[cell] == 0:
                del targets[cell]
            if not targets:
                del self.dependents[source]

    def propagate(self, cell, difference):
        if difference == 0:
            return
        for target, multiplicity in list(self.dependents.get(cell, {}).items()):
            change = difference * multiplicity
            self.values[target[0]][target[1]] += change
            self.propagate(target, change)

    def set(self, row: int, column: str, val: int) -> None:
        cell = row - 1, ord(column) - ord("A")
        old_value = self.values[cell[0]][cell[1]]
        self.remove_formula(cell)
        self.values[cell[0]][cell[1]] = val
        self.propagate(cell, val - old_value)

    def get(self, row: int, column: str) -> int:
        return self.values[row - 1][ord(column) - ord("A")]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = row - 1, ord(column) - ord("A")
        old_value = self.values[cell[0]][cell[1]]
        self.remove_formula(cell)

        formula = self.references(numbers)
        value = sum(
            self.values[source[0]][source[1]] * multiplicity
            for source, multiplicity in formula.items()
        )
        self.formulas[cell] = formula
        for source, multiplicity in formula.items():
            self.dependents[source][cell] += multiplicity

        self.values[cell[0]][cell[1]] = value
        self.propagate(cell, value - old_value)
        return value
