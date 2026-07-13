# Find the Power of K-Size Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-power-of-k-size-subarrays-i](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/).

### Goal
Given an array of integers and an integer `k`, identify the "power" of every contiguous subarray of length `k`. A subarray is considered "powerful" if all its elements are sorted in strictly increasing order with a difference of exactly 1 between consecutive elements. If a subarray is powerful, its power is its maximum element; otherwise, its power is -1.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the size of the sliding window.

**Return value**

- A list of integers representing the power of each contiguous subarray of length `k`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 3, 2, 5], k = 3`
- Output: `[3, 4, -1, -1, -1]`

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2], k = 4`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums = [3, 2, 3, 2, 3, 2], k = 2`
- Output: `[-1, 3, -1, 3, -1]`

---

## Solution
### Approach
The problem is solved using a **Sliding Window** approach combined with a **Consecutive Counter**. We maintain a count of how many consecutive elements satisfy the condition `nums[i] == nums[i-1] + 1`. If this count reaches `k`, the current window is powerful.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array exactly once.
- **Space Complexity**: `O(n - k + 1)` to store the resulting list of powers.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> List[int]:
    if k == 1:
        return nums

    n = len(nums)
    results = []
    # consecutive_count tracks how many elements in a row satisfy nums[i] == nums[i-1] + 1
    consecutive_count = 1

    for i in range(1, n):
        if nums[i] == nums[i - 1] + 1:
            consecutive_count += 1
        else:
            consecutive_count = 1

        # Once we have processed at least k-1 elements, we start checking windows
        if i >= k - 1:
            if consecutive_count >= k:
                results.append(nums[i])
            else:
                results.append(-1)

    return results
```
</details>
