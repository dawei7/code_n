# Longest Subarray of 1's After Deleting One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1493 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-subarray-of-1s-after-deleting-one-element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/).

### Goal
Delete exactly one element, then find the longest contiguous subarray containing only `1`s.

### Function Contract
**Inputs**

- `nums`: a binary array.

**Return value**

The maximum length of all-ones subarray after one deletion.

### Examples
**Example 1**

- Input: `nums = [1,1,0,1]`
- Output: `3`

**Example 2**

- Input: `nums = [0,1,1,1,0,1,1,0,1]`
- Output: `5`

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `2`

---

## Solution
### Approach
Sliding window with at most one zero. The window length minus one represents deleting one element.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    left = 0
    zeros = 0
    best = 0
    for right, value in enumerate(nums):
        zeros += value == 0
        while zeros > 1:
            zeros -= nums[left] == 0
            left += 1
        best = max(best, right - left)
    return best
```
</details>
