# Maximum Sum With at Most K Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3462 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-with-at-most-k-elements](https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/).

### Goal
Given a 2D matrix and an array of limits for each row, select at most $k$ elements from the matrix such that the sum of the selected elements is maximized. For each row $i$, you are allowed to pick at most `limits[i]` elements.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.
- `limits`: A list of integers where `limits[i]` is the maximum number of elements that can be picked from row `i`.
- `k`: An integer representing the total maximum number of elements to be selected from the entire grid.

**Return value**

- An integer representing the maximum possible sum of the selected elements.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]], limits = [1, 2], k = 2`
- Output: `7`
- Explanation: We can pick 4 from row 1 (limit 2) and 3 from row 0 (limit 1). Total = 7.

**Example 2**

- Input: `grid = [[5, 3, 7], [8, 2, 6]], limits = [2, 2], k = 3`
- Output: `21`
- Explanation: Pick 7 and 5 from row 0, and 8 from row 1. Total = 20. Wait, 7+5+8 = 20. Actually, 7+8+6 = 21.

**Example 3**

- Input: `grid = [[10]], limits = [1], k = 1`
- Output: `10`

---

## Solution
### Approach
The problem is solved using a Greedy approach combined with sorting. For each row, we identify the largest `limits[i]` elements. We collect all these candidates from all rows into a single pool, sort them in descending order, and select the top `k` elements to maximize the sum.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot M \log M + K \log K)$, where $N$ is the number of rows, $M$ is the number of columns, and $K$ is the total elements to pick. Sorting each row takes $O(N \cdot M \log M)$, and selecting the top $K$ takes $O(N \cdot M \log(N \cdot M))$.
- **Space Complexity**: $O(N \cdot M)$ to store the candidate elements collected from the rows.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(grid: list[list[int]], limits: list[int], k: int) -> int:
    """
    Calculates the maximum sum by picking at most k elements from the grid,
    respecting the row-specific limits.
    """
    candidates = []

    # For each row, pick the largest 'limits[i]' elements.
    # We use a min-heap to keep track of the largest elements in each row.
    for i in range(len(grid)):
        row = grid[i]
        limit = limits[i]

        # Get the largest 'limit' elements from the current row
        # nlargest is efficient for small limits, or sorting for larger ones.
        row_largest = heapq.nlargest(limit, row)
        candidates.extend(row_largest)

    # Now we have a pool of candidates. We want the largest k from this pool.
    # Sorting the candidates descending and taking the first k.
    candidates.sort(reverse=True)

    return sum(candidates[:k])
```
</details>
