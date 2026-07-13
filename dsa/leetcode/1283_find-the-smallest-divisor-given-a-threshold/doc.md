# Find the Smallest Divisor Given a Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1283 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-smallest-divisor-given-a-threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/).

### Goal
Find the smallest positive divisor such that the sum of each number divided by the divisor and rounded up is at most `threshold`.

### Function Contract
**Inputs**

- `nums`: positive integer array.
- `threshold`: maximum allowed rounded-up division sum.

**Return value**

The smallest divisor satisfying the threshold.

### Examples
**Example 1**

- Input: `nums = [1,2,5,9]`, `threshold = 6`
- Output: `5`

**Example 2**

- Input: `nums = [44,22,33,11,1]`, `threshold = 5`
- Output: `44`

**Example 3**

- Input: `nums = [2,3,5,7,11]`, `threshold = 11`
- Output: `3`

---

## Solution
### Approach
Binary search on the answer.

### Complexity Analysis
- **Time Complexity**: `O(n log max(nums))`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, threshold):
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        total = sum((value + mid - 1) // mid for value in nums)
        if total <= threshold:
            right = mid
        else:
            left = mid + 1
    return left
```
</details>
