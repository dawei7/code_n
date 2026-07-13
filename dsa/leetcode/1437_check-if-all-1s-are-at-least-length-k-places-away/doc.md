# Check If All 1's Are at Least Length K Places Away

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1437 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-all-1s-are-at-least-length-k-places-away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/).

### Goal
Check whether every pair of `1` bits in the binary array has at least `k` zeroes between them.

### Function Contract
**Inputs**

- `nums`: a binary array.
- `k`: the required minimum number of zeroes between consecutive `1`s.

**Return value**

`true` if all `1`s are sufficiently separated, otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1,0,0,0,1,0,0,1], k = 2`
- Output: `true`

**Example 2**

- Input: `nums = [1,0,0,1,0,1], k = 2`
- Output: `false`

**Example 3**

- Input: `nums = [0,1,0,0,1], k = 1`
- Output: `true`

---

## Solution
### Approach
Track the index of the previous `1`. When another `1` is found, the index gap must be greater than `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, k):
    previous = None
    for index, value in enumerate(nums):
        if value == 1:
            if previous is not None and index - previous <= k:
                return False
            previous = index
    return True
```
</details>
