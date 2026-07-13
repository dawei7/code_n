# Maximum Sum of Distinct Subarrays With Length K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2461 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-of-distinct-subarrays-with-length-k](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/).

### Goal
Given an integer array and a window size `k`, identify all contiguous subarrays of length exactly `k` that contain only unique elements. Among these valid subarrays, calculate the sum of their elements and return the maximum sum found. If no such subarray exists, return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.
- `k`: An integer representing the required length of the contiguous subarray.

**Return value**

- An integer representing the maximum sum of any valid subarray of length `k` with all distinct elements.

### Examples
**Example 1**

- Input: `nums = [1,5,4,2,9,9,9], k = 3`
- Output: `15`
- Explanation: Valid subarrays of length 3 are [1,5,4], [5,4,2], [4,2,9]. The sums are 10, 11, and 15 respectively. The maximum is 15.

**Example 2**

- Input: `nums = [4,4,4], k = 3`
- Output: `0`
- Explanation: No subarray of length 3 has distinct elements.

**Example 3**

- Input: `nums = [1,1,1,7,8,9], k = 3`
- Output: `24`
- Explanation: The only valid subarray is [7,8,9] with sum 24.

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (or frequency array) to maintain the count of elements within the current window. This allows for $O(1)$ updates to the window sum and $O(1)$ checks for uniqueness, ensuring the window remains valid as it traverses the array.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array once, and each element is added and removed from the window at most once.
- **Space Complexity**: `O(min(n, m))`, where `m` is the range of values in the array, as the hash map stores at most `k` distinct elements at any given time.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    if k > n:
        return 0

    max_sum = 0
    current_sum = 0
    counts = defaultdict(int)
    distinct_count = 0

    for i in range(n):
        # Add current element to window
        val = nums[i]
        if counts[val] == 0:
            distinct_count += 1
        counts[val] += 1
        current_sum += val

        # Remove element sliding out of window
        if i >= k:
            out_val = nums[i - k]
            counts[out_val] -= 1
            if counts[out_val] == 0:
                distinct_count -= 1
            current_sum -= out_val

        # Check if window is valid
        if i >= k - 1:
            if distinct_count == k:
                max_sum = max(max_sum, current_sum)

    return max_sum
```
</details>
