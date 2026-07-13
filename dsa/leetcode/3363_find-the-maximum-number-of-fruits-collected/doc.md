# Find the Maximum Number of Fruits Collected

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3363 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-maximum-number-of-fruits-collected](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/).

### Goal
Given an $n \times n$ grid of fruit counts, three children start at `(0, 0)`, `(0, n - 1)`, and `(n - 1, 0)`. Each child makes exactly `n - 1` moves and must finish at `(n - 1, n - 1)`, using the move options defined by the problem. Fruits in a room are collected once even if multiple children visit it. Return the maximum total fruits collected.

### Function Contract
**Inputs**

- `fruits`: A square grid where `fruits[i][j]` is the number of fruits in room `(i, j)`.

**Return value**

- An integer representing the maximum total fruits collected across the three defined paths.

### Examples
**Example 1**

- Input: `fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]`
- Output: `100`

**Example 2**

- Input: `fruits = [[1,1],[1,1]]`
- Output: `4`

**Example 3**

- Input: `fruits = [[5,100,1],[1,50,100],[100,1,5]]`
- Output: `262`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We decompose the movement into three distinct segments:
1. **Path 1 (Down-Right):** A simple diagonal path from $(0,0)$ to $(n-1, n-1)$.
2. **Path 2 (Down-Left):** A path starting from $(0, n-1)$ moving towards the bottom row.
3. **Path 3 (Up-Right):** A path starting from $(n-1, 0)$ moving towards the right column.
By calculating the maximum fruits for each path independently while respecting the boundary constraints, we aggregate the results.

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the grid, as we iterate through the matrix to compute DP states.
- **Space Complexity**: $O(n^2)$ to store the DP table, which can be optimized to $O(n)$ if only the current and previous rows are maintained.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(fruits: list[list[int]]) -> int:
    n = len(fruits)
    diagonal = sum(fruits[i][i] for i in range(n))

    def top_right_path() -> int:
        negative = -10**18
        previous = [negative] * n
        previous[n - 1] = fruits[0][n - 1]

        for row in range(1, n - 1):
            current = [negative] * n
            for col in range(row + 1, n):
                best = previous[col]
                if col > 0:
                    best = max(best, previous[col - 1])
                if col + 1 < n:
                    best = max(best, previous[col + 1])
                current[col] = best + fruits[row][col]
            previous = current

        return previous[n - 1]

    def bottom_left_path() -> int:
        negative = -10**18
        previous = [negative] * n
        previous[n - 1] = fruits[n - 1][0]

        for col in range(1, n - 1):
            current = [negative] * n
            for row in range(col + 1, n):
                best = previous[row]
                if row > 0:
                    best = max(best, previous[row - 1])
                if row + 1 < n:
                    best = max(best, previous[row + 1])
                current[row] = best + fruits[row][col]
            previous = current

        return previous[n - 1]

    return diagonal + top_right_path() + bottom_left_path()
```
</details>
