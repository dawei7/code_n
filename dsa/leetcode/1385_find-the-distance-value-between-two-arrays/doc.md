# Find the Distance Value Between Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1385 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-distance-value-between-two-arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/).

### Goal
Count how many values in `arr1` are farther than distance `d` from every value in `arr2`.

### Function Contract
**Inputs**

- `arr1`: the first list of integers.
- `arr2`: the second list of integers.
- `d`: the allowed distance threshold.

**Return value**

The number of elements `x` in `arr1` such that `abs(x - y) > d` for every `y` in `arr2`.

### Examples
**Example 1**

- Input: `arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2`
- Output: `2`

**Example 2**

- Input: `arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3`
- Output: `2`

**Example 3**

- Input: `arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6`
- Output: `1`

---

## Solution
### Approach
Sorting plus binary search. Sort `arr2`; for each value in `arr1`, only its insertion neighbors in `arr2` can be closest, so checking those neighbors is enough.

### Complexity Analysis
- **Time Complexity**: `O(m log m + n log m)` where `n = len(arr1)` and `m = len(arr2)`.
- **Space Complexity**: `O(m)` if sorting a copy of `arr2`, or `O(1)` extra if sorting in place.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1385: Find the Distance Value Between Two Arrays."""

from bisect import bisect_left


def solve(arr1: list[int], arr2: list[int], d: int) -> int:
    arr2.sort()
    answer = 0
    for value in arr1:
        pos = bisect_left(arr2, value)
        close = False
        if pos < len(arr2) and abs(arr2[pos] - value) <= d:
            close = True
        if pos > 0 and abs(arr2[pos - 1] - value) <= d:
            close = True
        if not close:
            answer += 1
    return answer
```
</details>
