# Maximum Length of Subarray With Positive Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1567 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-length-of-subarray-with-positive-product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/).

### Goal
Find the longest contiguous subarray whose product is positive.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The maximum length of a subarray with positive product.

### Examples
**Example 1**

- Input: `nums = [1, -2, -3, 4]`
- Output: `4`

**Example 2**

- Input: `nums = [0, 1, -2, -3, -4]`
- Output: `3`

**Example 3**

- Input: `nums = [-1, -2, -3, 0, 1]`
- Output: `2`

---

## Solution
### Approach
Track two lengths while scanning: the longest subarray ending here with positive
product and the longest ending here with negative product. A positive number
extends both lengths, a negative number swaps the roles, and zero resets both.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    positive = 0
    negative = 0
    best = 0
    for num in nums:
        if num == 0:
            positive = 0
            negative = 0
        elif num > 0:
            positive += 1
            negative = negative + 1 if negative else 0
        else:
            positive, negative = (negative + 1 if negative else 0), positive + 1
        best = max(best, positive)
    return best
```
</details>
