from collections import Counter, defaultdict, deque


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

    def refresh_dependents(self, cell):
        affected = {cell}
        stack = [cell]
        while stack:
            source = stack.pop()
            for target in self.dependents.get(source, {}):
                if target not in affected:
                    affected.add(target)
                    stack.append(target)

        indegree = {
            target: sum(source in affected for source in self.formulas.get(target, {})) for target in affected
        }
        ready = deque(target for target, degree in indegree.items() if degree == 0)
        while ready:
            source = ready.popleft()
            for target in self.dependents.get(source, {}):
                indegree[target] -= 1
                if indegree[target] == 0:
                    formula = self.formulas[target]
                    self.values[target[0]][target[1]] = sum(
                        self.values[dependency[0]][dependency[1]] * multiplicity
                        for dependency, multiplicity in formula.items()
                    )
                    ready.append(target)

    def set(self, row: int, column: str, val: int) -> None:
        cell = row - 1, ord(column) - ord("A")
        old_value = self.values[cell[0]][cell[1]]
        self.remove_formula(cell)
        self.values[cell[0]][cell[1]] = val
        if val != old_value:
            self.refresh_dependents(cell)

    def get(self, row: int, column: str) -> int:
        return self.values[row - 1][ord(column) - ord("A")]

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        cell = row - 1, ord(column) - ord("A")
        old_value = self.values[cell[0]][cell[1]]
        self.remove_formula(cell)

        formula = self.references(numbers)
        value = sum(self.values[source[0]][source[1]] * multiplicity for source, multiplicity in formula.items())
        self.formulas[cell] = formula
        for source, multiplicity in formula.items():
            self.dependents[source][cell] += multiplicity

        self.values[cell[0]][cell[1]] = value
        if value != old_value:
            self.refresh_dependents(cell)
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
