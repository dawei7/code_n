# Minimum Sum of Mountain Triplets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2909 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-sum-of-mountain-triplets-ii](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/).

### Goal
Given an array of integers, identify a triplet of indices `(i, j, k)` such that `i < j < k` and the values satisfy the condition `nums[i] < nums[j]` and `nums[k] < nums[j]`. The objective is to find the minimum possible sum of such a triplet (`nums[i] + nums[j] + nums[k]`). If no such triplet exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where `3 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^8`.

**Return value**

- An integer representing the minimum sum of a mountain triplet, or -1 if no valid triplet is found.

### Examples
**Example 1**

- Input: `nums = [8,6,1,5,3]`
- Output: `9`
- Explanation: The triplet (2, 3, 4) with values (1, 5, 3) satisfies the condition 1 < 5 and 3 < 5. Sum = 1 + 5 + 3 = 9.

**Example 2**

- Input: `nums = [5,4,8,7,10,2]`
- Output: `13`
- Explanation: The triplet (1, 2, 4) with values (4, 8, 7) satisfies the condition 4 < 8 and 7 < 8. Sum = 4 + 8 + 7 = 19. The triplet (1, 4, 5) with values (4, 10, 2) is not valid because 10 is not greater than 2. The triplet (0, 2, 3) with values (5, 8, 7) is valid. Sum = 5 + 8 + 7 = 20. The minimum is 13 from (1, 2, 3) is not possible, but (0, 2, 5) is not valid. The minimum is 13.

**Example 3**

- Input: `nums = [6,5,4,3,2,1]`
- Output: `-1`
- Explanation: No triplet satisfies the mountain condition.

---

## Solution
### Approach
The problem is solved using a **Prefix and Suffix Minimum** approach. By precomputing the minimum value to the left of every index `i` and the minimum value to the right of every index `i`, we can treat each index `j` as the potential peak of a mountain. For a fixed `j`, the minimum sum is `min_left[j] + nums[j] + min_right[j]`, provided that `min_left[j] < nums[j]` and `min_right[j] < nums[j]`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We perform three linear passes: one to compute prefix minimums, one for suffix minimums, and one to calculate the minimum sum.
- **Space Complexity**: `O(n)` to store the prefix and suffix minimum arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return -1

    # min_left[i] stores the minimum value in nums[0...i-1]
    min_left = [float('inf')] * n
    curr_min = nums[0]
    for i in range(1, n):
        min_left[i] = curr_min
        if nums[i] < curr_min:
            curr_min = nums[i]

    # min_right[i] stores the minimum value in nums[i+1...n-1]
    min_right = [float('inf')] * n
    curr_min = nums[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = curr_min
        if nums[i] < curr_min:
            curr_min = nums[i]

    min_sum = float('inf')
    found = False

    # Check each index as a potential peak
    for i in range(1, n - 1):
        if min_left[i] < nums[i] and min_right[i] < nums[i]:
            current_triplet_sum = min_left[i] + nums[i] + min_right[i]
            if current_triplet_sum < min_sum:
                min_sum = current_triplet_sum
                found = True

    return int(min_sum) if found else -1
```
</details>
