# Filling Bookcase Shelves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [filling-bookcase-shelves](https://leetcode.com/problems/filling-bookcase-shelves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/filling-bookcase-shelves/).

### Goal
Place books in their given order onto shelves of fixed width. Each book has a width and height. Minimize the sum of shelf heights.

### Function Contract
**Inputs**

- `books`: list of `[thickness, height]` pairs in the order they must be placed.
- `shelfWidth`: maximum total thickness allowed on one shelf.

**Return value**

The minimum possible total height of the bookcase.

### Examples
**Example 1**

- Input: `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]`, `shelfWidth = 4`
- Output: `6`

**Example 2**

- Input: `books = [[1,3],[2,4],[3,2]]`, `shelfWidth = 6`
- Output: `4`

**Example 3**

- Input: `books = [[2,5],[2,6],[2,7]]`, `shelfWidth = 4`
- Output: `12`

---

## Solution
### Approach
Dynamic programming over ordered partitions.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1105: Filling Bookcase Shelves."""


def solve(books: list[list[int]], shelf_width: int) -> int:
    n = len(books)
    dp = [0] + [10**18] * n
    for i in range(1, n + 1):
        width = 0
        height = 0
        for j in range(i, 0, -1):
            width += books[j - 1][0]
            if width > shelf_width:
                break
            height = max(height, books[j - 1][1])
            dp[i] = min(dp[i], dp[j - 1] + height)
    return dp[n]
```
</details>
