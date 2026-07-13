# Minimum Operations to Make Median of Array Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3107 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-median-of-array-equal-to-k](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/).

### Goal
Given an array of integers and a target integer `k`, determine the minimum number of increment or decrement operations required to transform the array such that its median becomes exactly `k`. The median of an array with an odd length `n` is defined as the element at the sorted index `n // 2`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the target median value.

**Return value**

- An integer representing the minimum total operations (sum of absolute differences) needed to make the median equal to `k`.

### Examples
**Example 1**

- Input: `nums = [2, 5, 6, 8, 5], k = 4`
- Output: `2`

**Example 2**

- Input: `nums = [2, 5, 6, 8, 5], k = 7`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 6], k = 4`
- Output: `0`

---

## Solution
### Approach
The problem relies on a **Greedy approach** combined with **Sorting**. By sorting the array, we identify the current median. If the current median is less than `k`, we must increase the median and any elements to its right that are smaller than `k`. If the current median is greater than `k`, we must decrease the median and any elements to its left that are larger than `k`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the sorting step, where `n` is the length of the array. The subsequent linear scan takes `O(n)`.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to make the median of nums equal to k.
    """
    nums = sorted(nums)
    n = len(nums)
    mid = n // 2

    operations = 0

    # If the current median is less than k, we need to increase the median
    # and potentially elements to the right of the median.
    if nums[mid] < k:
        for i in range(mid, n):
            if nums[i] < k:
                operations += (k - nums[i])
            else:
                # Since the array is sorted, if nums[i] >= k,
                # no further elements need to be increased.
                break

    # If the current median is greater than k, we need to decrease the median
    # and potentially elements to the left of the median.
    elif nums[mid] > k:
        for i in range(mid, -1, -1):
            if nums[i] > k:
                operations += (nums[i] - k)
            else:
                # Since the array is sorted, if nums[i] <= k,
                # no further elements need to be decreased.
                break

    return operations
```
</details>
