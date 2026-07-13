# Partition Array Into Three Parts With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1013 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [partition-array-into-three-parts-with-equal-sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/).

### Goal
Determine whether an array can be split into three nonempty contiguous parts that all have the same sum.

### Function Contract
**Inputs**

- `arr`: List[int]

**Return value**

bool - `True` if such a three-way split exists

### Examples
**Example 1**

- Input: `arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]`
- Output: `True`

**Example 2**

- Input: `arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]`
- Output: `False`

**Example 3**

- Input: `arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]`
- Output: `True`

---

## Solution
### Approach
Prefix accumulation and greedy segment counting.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1013: Partition Array Into Three Parts With Equal Sum."""


def solve(arr: list[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False

    target = total // 3
    parts = 0
    current = 0
    for value in arr:
        current += value
        if current == target:
            parts += 1
            current = 0
    return parts >= 3
```
</details>
