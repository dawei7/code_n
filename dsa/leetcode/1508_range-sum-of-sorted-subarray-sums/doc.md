# Range Sum of Sorted Subarray Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1508 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [range-sum-of-sorted-subarray-sums](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/).

### Goal
Generate the sums of all non-empty subarrays, sort those sums, and return the
sum of the entries from rank `left` through rank `right`.

### Function Contract
**Inputs**

- `nums`: an array of positive integers.
- `n`: the length of `nums`.
- `left`: the first 1-based sorted position to include.
- `right`: the last 1-based sorted position to include.

**Return value**

The requested range sum modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 5`
- Output: `13`

**Example 2**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 3, right = 4`
- Output: `6`

**Example 3**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 10`
- Output: `50`

---

## Solution
### Approach
The direct approach builds every subarray sum, sorts the resulting list, and
sums the requested slice. Since the input values are positive, an optimized
version can also binary-search a sum threshold and count or sum subarrays below
it with a sliding window.

### Complexity Analysis
- **Time Complexity**: `O(n^2 log n)` for the direct sorted-sums method.
- **Space Complexity**: `O(n^2)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums, n, left, right):
    mod = 1_000_000_007
    n = min(len(nums), max(0, int(n)))
    sums = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            sums.append(total)
    sums.sort()
    left = max(1, int(left))
    right = min(len(sums), int(right))
    return sum(sums[left - 1:right]) % mod
```
</details>
