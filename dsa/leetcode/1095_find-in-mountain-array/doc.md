# Find in Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1095 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-in-mountain-array](https://leetcode.com/problems/find-in-mountain-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-in-mountain-array/).

### Goal
Find the first index of `target` in a mountain array. A mountain array strictly increases up to one peak and then strictly decreases.

### Function Contract
**Inputs**

- `target`: value to search for.
- `mountain_arr`: mountain-array values. In LeetCode this is provided through a `MountainArray` object with `get(index)` and `length()`; locally it is represented as a list.

**Return value**

The smallest index containing `target`, or `-1` if `target` does not occur.

### Examples
**Example 1**

- Input: `target = 3, mountain_arr = [1, 2, 3, 4, 5, 3, 1]`
- Output: `2`

**Example 2**

- Input: `target = 3, mountain_arr = [0, 1, 2, 4, 2, 1]`
- Output: `-1`

**Example 3**

- Input: `target = 4, mountain_arr = [1, 5, 2]`
- Output: `-1`

---

## Solution
### Approach
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1095: Find in Mountain Array."""


def solve(target: int, mountain_arr) -> int:
    def get(index: int) -> int:
        if isinstance(mountain_arr, list):
            return mountain_arr[index]
        return mountain_arr.get(index)

    def length() -> int:
        if isinstance(mountain_arr, list):
            return len(mountain_arr)
        return mountain_arr.length()

    n = length()
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if get(mid) < get(mid + 1):
            left = mid + 1
        else:
            right = mid
    peak = left

    def search(lo: int, hi: int, ascending: bool) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            value = get(mid)
            if value == target:
                return mid
            if (value < target) == ascending:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    answer = search(0, peak, True)
    return answer if answer != -1 else search(peak + 1, n - 1, False)
```
</details>
