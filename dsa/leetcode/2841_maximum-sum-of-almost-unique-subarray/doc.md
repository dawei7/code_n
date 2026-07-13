# Maximum Sum of Almost Unique Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2841 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-of-almost-unique-subarray](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/).

### Goal
Given an array of integers and two constraints, `m` and `k`, find the maximum sum of any contiguous subarray of length `k` that contains at least `m` distinct elements. If no such subarray exists, return 0.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `m`: An integer representing the minimum number of distinct elements required.
- `k`: An integer representing the fixed length of the subarray.

**Return value**

- An integer representing the maximum sum found, or 0 if no valid subarray meets the criteria.

### Examples
**Example 1**

- Input: `nums = [2,6,7,3,1,7], m = 3, k = 4`
- Output: `18`
- Explanation: Subarrays of length 4 are [2,6,7,3] (sum 18, 4 distinct), [6,7,3,1] (sum 17, 4 distinct), [7,3,1,7] (sum 18, 3 distinct). Max is 18.

**Example 2**

- Input: `nums = [5,9,9,2,4,5,4], m = 1, k = 3`
- Output: `23`
- Explanation: Subarray [5,9,9] has sum 23 and 2 distinct elements (>= 1).

**Example 3**

- Input: `nums = [1,2,1,2,1,2,1], m = 3, k = 3`
- Output: `0`
- Explanation: All subarrays of length 3 have only 2 distinct elements, which is less than m=3.

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (or frequency dictionary) to maintain the count of distinct elements within the current window of size `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array once, and dictionary operations (insertion/deletion) are `O(1)` on average.
- **Space Complexity**: `O(k)`, as the hash map stores at most `k` distinct elements at any given time.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], m: int, k: int) -> int:
    n = len(nums)
    if k > n:
        return 0

    max_sum = 0
    current_sum = 0
    counts = defaultdict(int)

    # Initialize the first window
    for i in range(k):
        current_sum += nums[i]
        counts[nums[i]] += 1

    if len(counts) >= m:
        max_sum = current_sum

    # Slide the window across the array
    for i in range(k, n):
        # Add new element
        new_val = nums[i]
        old_val = nums[i - k]

        current_sum += new_val - old_val
        counts[new_val] += 1

        # Remove old element
        counts[old_val] -= 1
        if counts[old_val] == 0:
            del counts[old_val]

        # Check condition
        if len(counts) >= m:
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum
```
</details>
