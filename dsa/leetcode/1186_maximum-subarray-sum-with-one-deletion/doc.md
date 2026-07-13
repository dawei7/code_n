# Maximum Subarray Sum with One Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-subarray-sum-with-one-deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/).

### Goal
Find the maximum sum of a non-empty contiguous subarray after deleting at most one element from that subarray.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The largest possible subarray sum with zero or one deletion.

### Examples
**Example 1**

- Input: `arr = [1,-2,0,3]`
- Output: `4`

**Example 2**

- Input: `arr = [1,-2,-2,3]`
- Output: `3`

**Example 3**

- Input: `arr = [-1,-1,-1,-1]`
- Output: `-1`

---

## Solution
### Approach
Kadane-style dynamic programming with two states.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr):
    keep = arr[0]
    delete = 0
    answer = arr[0]
    for value in arr[1:]:
        delete = max(delete + value, keep)
        keep = max(keep + value, value)
        answer = max(answer, keep, delete)
    return answer
```
</details>
