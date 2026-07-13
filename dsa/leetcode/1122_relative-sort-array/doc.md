# Relative Sort Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1122 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [relative-sort-array](https://leetcode.com/problems/relative-sort-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/relative-sort-array/).

### Goal
Sort `arr1` so that values appearing in `arr2` come first and follow the order of `arr2`; values absent from `arr2` appear afterward in ascending order.

### Function Contract
**Inputs**

- `arr1`: array to reorder.
- `arr2`: array of distinct values that defines the priority order.

**Return value**

The reordered version of `arr1`.

### Examples
**Example 1**

- Input: `arr1 = [2,3,1,3,2,4,6,7,9,2,19]`, `arr2 = [2,1,4,3,9,6]`
- Output: `[2,2,2,1,4,3,3,9,6,7,19]`

**Example 2**

- Input: `arr1 = [28,6,22,8,44,17]`, `arr2 = [22,28,8,6]`
- Output: `[22,28,8,6,17,44]`

**Example 3**

- Input: `arr1 = [5,3,5,2]`, `arr2 = [3]`
- Output: `[3,2,5,5]`

---

## Solution
### Approach
Counting sort / custom ordering.

### Complexity Analysis
- **Time Complexity**: `O(n + k log k)` where `k` is the count of values not listed in `arr2`.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1122: Relative Sort Array."""

from collections import Counter


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = Counter(arr1)
    answer: list[int] = []
    for value in arr2:
        answer.extend([value] * counts.pop(value, 0))
    for value in sorted(counts):
        answer.extend([value] * counts[value])
    return answer
```
</details>
