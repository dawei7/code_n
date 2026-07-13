# Longest Alternating Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2765 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-alternating-subarray](https://leetcode.com/problems/longest-alternating-subarray/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-alternating-subarray/).

### Goal
Given an array of integers, identify the length of the longest contiguous subarray where the difference between consecutive elements alternates between 1 and -1. Specifically, for a subarray `nums[i...j]` to be valid, `nums[k+1] - nums[k]` must be `1` if `k-i` is even, and `-1` if `k-i` is odd. If no such subarray of length at least 2 exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the length of the longest alternating subarray, or -1 if no valid subarray of length 2 or greater is found.

### Examples
**Example 1**

- Input: `nums = [3, 4, 5, 4]`
- Output: `2` (The longest is `[4, 5]` or `[5, 4]`)

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 1, 2]`
- Output: `4`

---

## Solution
### Approach
The problem is solved using a linear scan (sliding window/two-pointer approach). We maintain a current length counter that resets or increments based on the expected alternating difference. By iterating through the array once, we track the state of the expected difference (1 or -1) and update the global maximum length whenever a valid sequence is extended.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the data.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the current state and the maximum length found.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    max_len = -1
    n = len(nums)

    # We look for subarrays of length at least 2
    # Start index i, current length length
    i = 0
    while i < n - 1:
        # Check if the first pair is valid (difference must be 1)
        if nums[i + 1] - nums[i] == 1:
            length = 2
            # Continue checking the alternating pattern
            # The expected difference alternates between -1 and 1
            # For index k, the difference should be 1 if (k-i) is even, -1 if odd
            curr = i + 1
            while curr < n - 1:
                expected_diff = -1 if (curr - i) % 2 == 1 else 1
                if nums[curr + 1] - nums[curr] == expected_diff:
                    length += 1
                    curr += 1
                else:
                    break
            max_len = max(max_len, length)
            # Optimization: jump to the end of this sequence
            i = curr
        else:
            i += 1

    return max_len
```
</details>
