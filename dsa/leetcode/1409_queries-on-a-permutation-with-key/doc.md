# Queries on a Permutation With Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1409 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [queries-on-a-permutation-with-key](https://leetcode.com/problems/queries-on-a-permutation-with-key/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/queries-on-a-permutation-with-key/).

### Goal
Maintain a permutation of numbers `1..m`. For each query value, report its current zero-based index, then move that value to the front of the permutation.

### Function Contract
**Inputs**

- `queries`: the values to look up and move.
- `m`: the largest value in the initial permutation `1..m`.

**Return value**

A list of indices, one for each query before it is moved to the front.

### Examples
**Example 1**

- Input: `queries = [3,1,2,1], m = 5`
- Output: `[2,1,2,1]`

**Example 2**

- Input: `queries = [4,1,2,2], m = 4`
- Output: `[3,1,2,0]`

**Example 3**

- Input: `queries = [7,5,5,8,3], m = 8`
- Output: `[6,5,0,7,5]`

---

## Solution
### Approach
Simulation or indexed order statistics. The direct solution keeps a list and moves queried values to the front; an optimized solution uses a Fenwick tree with reserved front positions to support index queries and moves in logarithmic time.

### Complexity Analysis
- **Time Complexity**: `O(qm)` for direct simulation, or `O((q + m) log(q + m))` with a Fenwick tree.
- **Space Complexity**: `O(m)` for simulation, or `O(q + m)` for the Fenwick tree approach.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1409: Queries on a Permutation With Key."""


class _Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


def solve(queries: list[int], m: int) -> list[int]:
    q = len(queries)
    bit = _Fenwick(q + m + 2)
    positions = {value: q + value for value in range(1, m + 1)}
    for pos in positions.values():
        bit.add(pos, 1)

    answer: list[int] = []
    front = q
    for value in queries:
        pos = positions[value]
        answer.append(bit.sum(pos) - 1)
        bit.add(pos, -1)
        positions[value] = front
        bit.add(front, 1)
        front -= 1
    return answer
```
</details>
