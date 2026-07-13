# Height Checker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1051 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [height-checker](https://leetcode.com/problems/height-checker/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/height-checker/).

### Goal
Students are currently listed by height. Count how many positions differ from the nondecreasing height order.

### Function Contract
**Inputs**

- `heights`: List[int]

**Return value**

int - number of mismatched positions

### Examples
**Example 1**

- Input: `heights = [1, 1, 4, 2, 1, 3]`
- Output: `3`

**Example 2**

- Input: `heights = [5, 1, 2, 3, 4]`
- Output: `5`

**Example 3**

- Input: `heights = [1, 2, 3, 4, 5]`
- Output: `0`

---

## Solution
### Approach
Sorting comparison.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1051: Height Checker."""


def solve(heights: list[int]) -> int:
    return sum(actual != expected for actual, expected in zip(heights, sorted(heights)))
```
</details>
