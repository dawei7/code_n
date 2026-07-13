# The k Strongest Values in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1471 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-k-strongest-values-in-an-array](https://leetcode.com/problems/the-k-strongest-values-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-k-strongest-values-in-an-array/).

### Goal
Return the `k` strongest values in the array. Strength is measured by distance from the median, with the larger value breaking ties.

### Function Contract
**Inputs**

- `arr`: a list of integers.
- `k`: the number of strongest values to return.

**Return value**

A list containing any valid order of the `k` strongest values.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5], k = 2`
- Output: `[5,1]`

**Example 2**

- Input: `arr = [1,1,3,5,5], k = 3`
- Output: `[5,5,1]`

**Example 3**

- Input: `arr = [6,7,11,7,6,8], k = 4`
- Output: `[11,8,6,6]`

---

## Solution
### Approach
Sorting by custom strength. Sort the array, find the median at index `(n - 1) // 2`, then rank values by `(abs(value - median), value)`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` if returning a sorted copy.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr, k):
    if not arr or k <= 0:
        return []
    ordered = sorted(arr)
    median = ordered[(len(ordered) - 1) // 2]
    return sorted(arr, key=lambda value: (abs(value - median), value), reverse=True)[:k]
```
</details>
