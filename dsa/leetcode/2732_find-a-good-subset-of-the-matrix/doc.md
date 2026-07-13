# Find a Good Subset of the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2732 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-a-good-subset-of-the-matrix](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/).

### Goal
Given a 0-indexed $m \times n$ binary matrix `grid`, find a non-empty subset of row indices such that the sum of elements in each column within this subset is at most half of the size of the subset.

Formally, if the chosen subset of rows has indices $r_1, r_2, \dots, r_k$, then for each column $j$ ($0 \le j < n$), the column sum $\sum_{i=1}^k \text{grid}[r_i][j] \le \lfloor k / 2 \rfloor$.

Return the chosen row indices sorted in ascending order. If there are multiple valid subsets, return any of them. If no such subset exists, return an empty list.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` — A 2D binary grid of size $m \times n$ where $1 \le m \le 10^4$ and $1 \le n \le 5$.

**Return value**

- `List[int]` — A sorted list of row indices forming a good subset, or an empty list if no such subset exists.

### Examples
**Example 1**

- Input: `grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]`
- Output: `[0,1]`
- Explanation: The subset of rows is $\{0, 1\}$. The size of the subset is $k = 2$.
  - Column 0 sum: $0 + 0 = 0 \le 1$
  - Column 1 sum: $1 + 0 = 1 \le 1$
  - Column 2 sum: $1 + 0 = 1 \le 1$
  - Column 3 sum: $0 + 1 = 1 \le 1$
  Since all column sums are $\le \lfloor 2 / 2 \rfloor = 1$, this is a valid subset.

**Example 2**

- Input: `grid = [[0]]`
- Output: `[0]`
- Explanation: The subset of rows is $\{0\}$. The size of the subset is $k = 1$.
  - Column 0 sum: $0 \le \lfloor 1 / 2 \rfloor = 0$.
  This is a valid subset.

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1]]`
- Output: `[]`
- Explanation: It is impossible to choose any non-empty subset of rows that satisfies the condition.

---

## Solution
### Approach
The problem can be significantly simplified by leveraging the small constraint on the number of columns ($n \le 5$).

### Key Mathematical Insight
If a valid subset of rows of any size $k$ exists, then **there must exist a valid subset of size 1 or 2**.

**Proof Sketch:**
1. **Size 1**: If there is any row consisting entirely of `0`s, selecting this single row ($k=1$) is always valid because the sum of each column is $0 \le \lfloor 1/2 \rfloor = 0$.
2. **Size 2**: If no row of all `0`s exists, any valid subset of size $k=2$ requires two rows $r_1$ and $r_2$ such that for every column $j$, at most one of the rows has a `1`. This is equivalent to saying that the bitwise AND of the binary representations of $r_1$ and $r_2$ is `0`.
3. **Size $k \ge 3$**: Suppose a valid subset of size $k \ge 3$ exists. If we assume that no pair of rows in this subset has a bitwise AND of `0`, then every pair of rows must share at least one column where both have a `1`.
   - The number of pairs of rows is $\binom{k}{2}$.
   - Each column $j$ can have at most $\lfloor k/2 \rfloor$ ones, which can cover at most $\binom{\lfloor k/2 \rfloor}{2}$ pairs of rows.
   - With $n \le 5$ columns, the maximum number of pairs we can cover is $n \binom{\lfloor k/2 \rfloor}{2} \le 5 \binom{\lfloor k/2 \rfloor}{2}$.
   - For all $k \ge 3$, we can show that $\binom{k}{2} > 5 \binom{\lfloor k/2 \rfloor}{2}$. By the Pigeonhole Principle, it is impossible to cover all pairs of rows. Thus, there must be at least one pair of rows that do not share any `1`s, meaning their bitwise AND is `0`.

### Algorithm Steps
1. Convert each row of the grid into a bitmask (an integer between $0$ and $2^n - 1$).
2. Store the first occurrence index of each unique bitmask in a hash map.
3. If the bitmask `0` (all zeros) is present, return its index as a list of size 1.
4. Otherwise, iterate through all pairs of unique bitmasks present in the hash map. If we find two bitmasks $u$ and $v$ such that $u \ \& \ v == 0$, return their indices sorted in ascending order.
5. If no such pair is found, return an empty list.

### Complexity Analysis
- **Time Complexity**: $O(m \cdot n + 4^n)$.
  - Converting the $m \times n$ grid into bitmasks takes $O(m \cdot n)$ time.
  - Since $n \le 5$, there are at most $2^n \le 32$ unique bitmasks.
  - Comparing all pairs of unique bitmasks takes $O((2^n)^2) = O(4^n)$ operations. For $n = 5$, this is at most $\binom{32}{2} = 496$ comparisons, which is $O(1)$.
  - Thus, the overall time complexity is dominated by the grid traversal: $O(m \cdot n)$.

- **Space Complexity**: $O(2^n)$.
  - We store at most $2^n$ unique bitmasks and their corresponding indices in a hash map.
  - For $n \le 5$, this requires storing at most 32 elements, which is $O(1)$ auxiliary space.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> List[int]:
    # Map each unique row pattern (as a bitmask) to its first occurrence index
    pattern_to_idx = {}
    for r_idx, row in enumerate(grid):
        mask = 0
        for val in row:
            mask = (mask << 1) | val
        if mask not in pattern_to_idx:
            pattern_to_idx[mask] = r_idx

    # Case 1: A row with all 0s exists
    if 0 in pattern_to_idx:
        return [pattern_to_idx[0]]

    # Case 2: Find two rows with bitwise AND equal to 0
    masks = list(pattern_to_idx.keys())
    n_masks = len(masks)
    for i in range(n_masks):
        for j in range(i + 1, n_masks):
            if (masks[i] & masks[j]) == 0:
                return sorted([pattern_to_idx[masks[i]], pattern_to_idx[masks[j]]])

    return []
```
</details>
