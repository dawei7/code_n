# Minimum Absolute Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1200 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-absolute-difference](https://leetcode.com/problems/minimum-absolute-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-absolute-difference/).

### Goal
Find all pairs of values with the smallest absolute difference among any two elements in the array.

### Function Contract
**Inputs**

- `arr`: array of distinct integers.

**Return value**

Pairs `[a, b]` in ascending order where `a < b` and `b - a` is the minimum possible difference.

### Examples
**Example 1**

- Input: `arr = [4,2,1,3]`
- Output: `[[1,2],[2,3],[3,4]]`

**Example 2**

- Input: `arr = [1,3,6,10,15]`
- Output: `[[1,3]]`

**Example 3**

- Input: `arr = [3,8,-10,23,19,-4,-14,27]`
- Output: `[[-14,-10],[19,23],[23,27]]`

---

## Solution
### Approach
Sorting and adjacent comparison.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for sorting/output depending on implementation.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr):
    arr.sort()
    best = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
    return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == best]
```
</details>
