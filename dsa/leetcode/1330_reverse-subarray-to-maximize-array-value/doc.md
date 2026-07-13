# Reverse Subarray To Maximize Array Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1330 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reverse-subarray-to-maximize-array-value](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/).

### Goal
The value of an array is the sum of absolute differences between adjacent elements. Reverse at most one subarray to maximize that value.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The maximum possible array value after zero or one reversal.

### Examples
**Example 1**

- Input: `nums = [2,3,1,5,4]`
- Output: `10`

**Example 2**

- Input: `nums = [2,4,9,24,2,1,10]`
- Output: `68`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `3`

---

## Solution
### Approach
Greedy analysis of boundary gains.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    base = sum(abs(nums[i] - nums[i - 1]) for i in range(1, len(nums)))
    gain = 0
    low = float("inf")
    high = float("-inf")
    for i in range(1, len(nums)):
        a, b = nums[i - 1], nums[i]
        gain = max(gain, abs(nums[0] - b) - abs(a - b))
        gain = max(gain, abs(nums[-1] - a) - abs(a - b))
        low = min(low, max(a, b))
        high = max(high, min(a, b))
    gain = max(gain, 2 * (high - low))
    return base + gain
```
</details>
