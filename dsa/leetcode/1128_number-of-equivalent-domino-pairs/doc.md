# Number of Equivalent Domino Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1128 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-equivalent-domino-pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-equivalent-domino-pairs/).

### Goal
Count pairs of dominoes that show the same two numbers, allowing the two halves of a domino to be swapped.

### Function Contract
**Inputs**

- `dominoes`: list of two-number dominoes `[a, b]`.

**Return value**

The number of index pairs `(i, j)` with `i < j` whose dominoes are equivalent.

### Examples
**Example 1**

- Input: `dominoes = [[1,2],[2,1],[3,4],[5,6]]`
- Output: `1`

**Example 2**

- Input: `dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]`
- Output: `3`

**Example 3**

- Input: `dominoes = [[2,2],[2,2],[2,2]]`
- Output: `3`

---

## Solution
### Approach
Canonical key normalization and frequency counting.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` for the fixed domino value range, or `O(k)` for `k` distinct normalized dominoes.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1128: Number of Equivalent Domino Pairs."""

from collections import Counter


def solve(dominoes: list[list[int]]) -> int:
    counts: Counter[tuple[int, int]] = Counter()
    pairs = 0
    for a, b in dominoes:
        key = (a, b) if a <= b else (b, a)
        pairs += counts[key]
        counts[key] += 1
    return pairs
```
</details>
