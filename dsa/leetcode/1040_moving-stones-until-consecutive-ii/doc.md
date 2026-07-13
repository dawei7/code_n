# Moving Stones Until Consecutive II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1040 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [moving-stones-until-consecutive-ii](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/moving-stones-until-consecutive-ii/).

### Goal
Given stone positions on a number line, each move relocates an endpoint stone to an unoccupied non-endpoint position. Return the minimum and maximum number of moves needed to make all stones occupy consecutive positions.

### Function Contract
**Inputs**

- `stones`: List[int] distinct stone positions

**Return value**

List[int] - `[minimum_moves, maximum_moves]`

### Examples
**Example 1**

- Input: `stones = [7, 4, 9]`
- Output: `[1, 2]`

**Example 2**

- Input: `stones = [6, 5, 4, 3, 10]`
- Output: `[2, 3]`

**Example 3**

- Input: `stones = [100, 101, 102, 103, 104]`
- Output: `[0, 0]`

---

## Solution
### Approach
Sorting plus sliding window.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1040: Moving Stones Until Consecutive II."""


def solve(stones: list[int]) -> list[int]:
    stones.sort()
    n = len(stones)
    max_moves = max(
        stones[-1] - stones[1] + 1 - (n - 1),
        stones[-2] - stones[0] + 1 - (n - 1),
    )

    min_moves = n
    left = 0
    for right, stone in enumerate(stones):
        while stone - stones[left] + 1 > n:
            left += 1
        already = right - left + 1
        if already == n - 1 and stone - stones[left] + 1 == n - 1:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - already)
    return [min_moves, max_moves]
```
</details>
