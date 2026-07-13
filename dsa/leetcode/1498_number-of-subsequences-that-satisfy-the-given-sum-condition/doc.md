# Number of Subsequences That Satisfy the Given Sum Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1498 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-subsequences-that-satisfy-the-given-sum-condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/).

### Goal
Count the non-empty subsequences whose smallest value plus largest value is at
most `target`. Return the count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `target`: the maximum allowed sum of the subsequence minimum and maximum.

**Return value**

The number of valid subsequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [3, 5, 6, 7], target = 9`
- Output: `4`

**Example 2**

- Input: `nums = [3, 3, 6, 8], target = 10`
- Output: `6`

**Example 3**

- Input: `nums = [2, 3, 3, 4, 6, 7], target = 12`
- Output: `61`

---

## Solution
### Approach
Sort the array and use two pointers. When `nums[left] + nums[right] <= target`,
every subset of the values between those endpoints can be combined with
`nums[left]`, so add `2 ** (right - left)` and move `left` forward. If the sum is
too large, move `right` backward. Precompute powers of two modulo
`1_000_000_007` for constant-time additions.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` for sorting plus a linear scan.
- **Space Complexity**: `O(n)` for the precomputed powers.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, target):
    mod = 1_000_000_007
    nums = sorted(nums)
    powers = [1] * (len(nums) + 1)
    for i in range(1, len(powers)):
        powers[i] = (powers[i - 1] * 2) % mod
    left, right = 0, len(nums) - 1
    answer = 0
    while left <= right:
        if nums[left] + nums[right] <= target:
            answer = (answer + powers[right - left]) % mod
            left += 1
        else:
            right -= 1
    return answer
```
</details>
