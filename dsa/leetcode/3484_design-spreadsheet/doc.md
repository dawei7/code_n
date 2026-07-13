# Design Spreadsheet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3484 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-spreadsheet](https://leetcode.com/problems/design-spreadsheet/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-spreadsheet/).

### Goal
Design a spreadsheet system that supports setting values in specific cells (identified by row and column) and evaluating formulas. Formulas can involve simple arithmetic or references to other cells (e.g., "A1:B2" representing a range sum). The system must handle dynamic updates where changing a cell's value automatically propagates to any dependent formulas.

### Function Contract
**Inputs**

- `rows`: Integer representing the number of rows.
- `cols`: Integer representing the number of columns.
- `operations`: A list of commands, where each command is either `set(r, c, val)`, `get(r, c)`, or `sum(r, c, r1, c1, r2, c2)`.

**Return value**

- A list of integers representing the results of all `get` and `sum` operations.

### Examples
**Example 1**

- Input: `rows=3, cols=3, ops=[set(1, 1, 5), get(1, 1)]`
- Output: `[5]`

**Example 2**

- Input: `rows=3, cols=3, ops=[set(1, 1, 1), set(1, 2, 2), sum(2, 2, 1, 1, 1, 2)]`
- Output: `[3]`

**Example 3**

- Input: `rows=3, cols=3, ops=[set(1, 1, 1), sum(1, 2, 1, 1, 1, 1), set(1, 1, 2), get(1, 2)]`
- Output: `[1, 2]`

---

## Solution
### Approach
The system utilizes a **Directed Acyclic Graph (DAG)** to track cell dependencies. Each cell maintains a list of formulas that depend on it. When a cell's value is updated, we perform a topological update or re-evaluation of dependent cells. A **Hash Map** is used to store current cell values and their associated formula definitions.

### Complexity Analysis
- **Time Complexity**: `O(K * (N + M))` where `K` is the number of operations, `N` is the number of cells in a range, and `M` is the number of dependencies.
- **Space Complexity**: `O(R * C + D)` where `R*C` is the grid size and `D` is the total number of dependencies stored.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
