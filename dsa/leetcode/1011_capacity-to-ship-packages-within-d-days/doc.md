# Capacity To Ship Packages Within D Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1011 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [capacity-to-ship-packages-within-d-days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/).

### Goal
Given package weights in fixed order and a number of days, choose the smallest ship capacity that can deliver all packages within that many days without reordering packages.

### Function Contract
**Inputs**

- `weights`: List[int] package weights in shipping order
- `days`: int maximum number of shipping days

**Return value**

int - minimum feasible ship capacity

### Examples
**Example 1**

- Input: `weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5`
- Output: `15`

**Example 2**

- Input: `weights = [3, 2, 2, 4, 1, 4], days = 3`
- Output: `6`

**Example 3**

- Input: `weights = [1, 2, 3, 1, 1], days = 4`
- Output: `3`

---

## Solution
### Approach
Binary search on the answer with greedy feasibility simulation.

### Complexity Analysis
- **Time Complexity**: `O(n log(sum(weights)))`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1011: Capacity To Ship Packages Within D Days."""


def solve(weights: list[int], days: int) -> int:
    def can_ship(capacity: int) -> bool:
        used_days = 1
        load = 0
        for weight in weights:
            if load + weight > capacity:
                used_days += 1
                load = 0
            load += weight
        return used_days <= days

    low = max(weights)
    high = sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship(mid):
            high = mid
        else:
            low = mid + 1
    return low
```
</details>
