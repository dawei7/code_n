import collections

class Spreadsheet:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = collections.defaultdict(int)
        self.formulas = {}  # (r, c) -> list of (r1, c1, r2, c2)
        self.dependencies = collections.defaultdict(list) # (r, c) -> list of cells that depend on it

    def set(self, r, c, val):
        self.values[(r, c)] = val
        if (r, c) in self.formulas:
            del self.formulas[(r, c)]
        self._update_dependencies(r, c)

    def get(self, r, c):
        if (r, c) in self.formulas:
            return self._evaluate_formula(r, c)
        return self.values.get((r, c), 0)

    def sum(self, r, c, r1, c1, r2, c2):
        self.formulas[(r, c)] = (r1, c1, r2, c2)
        val = self._evaluate_formula(r, c)
        self.values[(r, c)] = val
        return val

    def _evaluate_formula(self, r, c):
        r1, c1, r2, c2 = self.formulas[(r, c)]
        total = 0
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                total += self.get(i, j)
        return total

    def _update_dependencies(self, r, c):
        # In a full implementation, we would track reverse dependencies 
        # to trigger re-calculation of cells that depend on (r, c)
        pass

def solve(rows, cols, operations):
    sheet = Spreadsheet(rows, cols)
    results = []
    for op in operations:
        name = op[0]
        if name == 'set':
            sheet.set(op[1], op[2], op[3])
        elif name == 'get':
            results.append(sheet.get(op[1], op[2]))
        elif name == 'sum':
            results.append(sheet.sum(op[1], op[2], op[3], op[4], op[5], op[6]))
    return results
