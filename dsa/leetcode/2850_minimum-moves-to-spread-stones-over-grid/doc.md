# Minimum Moves to Spread Stones Over Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2850 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-moves-to-spread-stones-over-grid](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/).

### Goal
Given a 3x3 grid where each cell contains a non-negative number of stones, calculate the minimum total Manhattan distance required to redistribute the stones such that every cell contains exactly one stone. A move consists of shifting one stone to an adjacent cell (up, down, left, or right).

### Function Contract
**Inputs**

- `grid`: A list of lists of integers (3x3 matrix) where the sum of all elements is exactly 9.

**Return value**

- An integer representing the minimum total moves required to reach a state where every cell has exactly one stone.

### Examples
**Example 1**

- Input: `grid = [[1,1,0],[1,1,0],[1,1,0]]`
- Output: `3`

**Example 2**

- Input: `grid = [[1,3,0],[1,0,0],[1,0,3]]`
- Output: `4`

---

## Solution
### Approach
The problem is solved using **Backtracking**. We identify all cells with zero stones (targets) and all cells with more than one stone (sources). We then recursively attempt to match every source stone to a target cell, calculating the Manhattan distance for each assignment and keeping track of the minimum total distance found across all permutations.

### Complexity Analysis
- **Time Complexity**: $O(N!)$, where $N$ is the number of cells with excess stones. In the worst case, we are permuting the distribution of stones, but since the grid is fixed at 3x3, the search space is small and manageable.
- **Space Complexity**: $O(N)$, where $N$ is the number of cells with excess stones, due to the recursion stack depth.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> int:
    sources = []
    targets = []

    for r in range(3):
        for c in range(3):
            if grid[r][c] > 1:
                for _ in range(grid[r][c] - 1):
                    sources.append((r, c))
            elif grid[r][c] == 0:
                targets.append((r, c))

    if not targets:
        return 0

    def get_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    memo = {}

    def backtrack(idx, current_targets):
        if idx == len(sources):
            return 0

        state = (idx, tuple(current_targets))
        if state in memo:
            return memo[state]

        res = float('inf')
        src = sources[idx]

        for i in range(len(current_targets)):
            if current_targets[i] == -1:
                current_targets[i] = 1
                dist = get_dist(src, targets[i])
                res = min(res, dist + backtrack(idx + 1, current_targets))
                current_targets[i] = -1

        memo[state] = res
        return res

    return backtrack(0, [-1] * len(targets))
```
</details>
