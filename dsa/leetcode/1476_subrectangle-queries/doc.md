# Subrectangle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1476 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [subrectangle-queries](https://leetcode.com/problems/subrectangle-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/subrectangle-queries/).

### Goal
Design a matrix wrapper that can set every value in a subrectangle and retrieve the current value of a single cell.

### Function Contract
**Inputs**

- `rectangle`: the initial matrix.
- `operations`: a list of operations after construction. Each operation is `[name, args]`, where `name` is `"updateSubrectangle"` or `"getValue"`.

**Return value**

A list containing `null` for each update and the value returned by each query.

### Examples
**Example 1**

- Input: `rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]], operations = [["getValue",[0,2]],["updateSubrectangle",[0,0,3,2,5]],["getValue",[0,2]]]`
- Output: `[1,null,5]`

**Example 2**

- Input: `rectangle = [[1,1],[2,2]], operations = [["updateSubrectangle",[0,0,0,0,7]],["getValue",[0,0]],["getValue",[1,1]]]`
- Output: `[null,7,2]`

**Example 3**

- Input: `rectangle = [[3]], operations = [["getValue",[0,0]],["updateSubrectangle",[0,0,0,0,9]],["getValue",[0,0]]]`
- Output: `[3,null,9]`

---

## Solution
### Approach
Either apply each update directly to the matrix, or store updates lazily and answer queries by checking the most recent covering update. The direct approach is simple and fast enough for modest dimensions.

### Complexity Analysis
- **Time Complexity**: `O(area)` per direct update and `O(1)` per query.
- **Space Complexity**: `O(1)` extra beyond the stored matrix.

### Reference Implementations
<details>
<summary>python</summary>

```python
class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = [row[:] for row in rectangle]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


def solve(rectangle, operations):
    matrix = [list(row) for row in rectangle] if isinstance(rectangle, list) else [[rectangle]]
    if not matrix:
        matrix = [[0]]
    queries = SubrectangleQueries(matrix)
    output = []
    for raw_operation in operations:
        if not isinstance(raw_operation, list) or not raw_operation:
            continue
        name = str(raw_operation[0])
        args = raw_operation[1] if len(raw_operation) > 1 and isinstance(raw_operation[1], list) else []
        if name == "updateSubrectangle" and len(args) >= 5:
            row1, col1, row2, col2, value = map(int, args[:5])
            queries.updateSubrectangle(row1, col1, row2, col2, value)
            output.append(None)
        elif name == "getValue" and len(args) >= 2:
            row, col = map(int, args[:2])
            output.append(queries.getValue(row, col))
    return output
```
</details>
