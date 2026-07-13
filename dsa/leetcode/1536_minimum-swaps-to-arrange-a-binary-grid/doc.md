# Minimum Swaps to Arrange a Binary Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1536 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-swaps-to-arrange-a-binary-grid](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/).

### Goal
Reorder the rows of a binary square grid using adjacent row swaps so every row
has enough trailing zeros for the grid to be valid.

### Function Contract
**Inputs**

- `grid`: an `n x n` matrix containing `0` and `1`.

**Return value**

The minimum number of adjacent row swaps, or `-1` if no valid ordering exists.

### Examples
**Example 1**

- Input: `grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]`
- Output: `-1`

**Example 3**

- Input: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]`
- Output: `0`

---

## Solution
### Approach
For each row, count trailing zeros. Row `i` needs at least `n - 1 - i` trailing
zeros. Greedily find the first row at or below `i` that satisfies the need, then
bubble it upward with adjacent swaps. If none exists, the answer is `-1`.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    n = len(grid)
    trailing = []
    for row in grid:
        zeros = 0
        for value in reversed(row[:n]):
            if value == 0:
                zeros += 1
            else:
                break
        trailing.append(zeros)

    swaps = 0
    for i in range(n):
        need = n - i - 1
        j = i
        while j < n and trailing[j] < need:
            j += 1
        if j == n:
            return -1
        while j > i:
            trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
            swaps += 1
            j -= 1
    return swaps
```
</details>
