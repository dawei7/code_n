# Number of Zero-Filled Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2348 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-zero-filled-subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-zero-filled-subarrays/).

### Goal
Given an array of integers, count the total number of contiguous subarrays that consist entirely of zeros. A subarray is a contiguous non-empty sequence of elements within the original array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`). The array can contain positive, negative, and zero values.

**Return value**

- An integer (`int`) representing the total count of zero-filled subarrays.

### Examples
**Example 1**

- Input: `nums = [0,0,0,2,0,0]`
- Output: `9`
- Explanation:
  - The first block `[0,0,0]` (indices 0-2) contributes `3 * (3+1) / 2 = 6` zero-filled subarrays: `[0]`, `[0]`, `[0]`, `[0,0]`, `[0,0]`, `[0,0,0]`.
  - The second block `[0,0]` (indices 4-5) contributes `2 * (2+1) / 2 = 3` zero-filled subarrays: `[0]`, `[0]`, `[0,0]`.
  - Total: `6 + 3 = 9`.

**Example 2**

- Input: `nums = [1,2,3]`
- Output: `0`
- Explanation: There are no zeros in the array, so no zero-filled subarrays can be formed.

**Example 3**

- Input: `nums = [0]`
- Output: `1`
- Explanation: A single zero forms one zero-filled subarray: `[0]`.

---

## Solution
### Approach
The problem can be solved by iterating through the array and identifying contiguous blocks of zeros. For any contiguous block of `k` zeros, the number of zero-filled subarrays that can be formed within that block is `k * (k + 1) / 2`. This is the sum of integers from 1 to `k` (i.e., 1 subarray of length 1, 1 subarray of length 2, ..., 1 subarray of length `k`).

The algorithm involves:
1.  Initializing a total count for zero-filled subarrays and a counter for the current consecutive zeros.
2.  Iterating through the input array.
3.  If the current element is `0`, increment the consecutive zero counter.
4.  If the current element is not `0` (or if the end of the array is reached), it signifies the end of a block of zeros. At this point, calculate the number of subarrays contributed by the `current_zero_count` using the formula `current_zero_count * (current_zero_count + 1) / 2` and add it to the total count. Then, reset the `current_zero_count` to `0`.
5.  After the loop finishes, a final check is needed to add any subarrays from a block of zeros that might end at the very end of the array.

This approach is a form of iterative counting or a single-pass scan.

### Complexity Analysis
- **Time Complexity**: `O(N)`
  The algorithm iterates through the input array `nums` exactly once. Each element is processed in constant time. Therefore, the time complexity is directly proportional to the number of elements `N` in the array.
- **Space Complexity**: `O(1)`
  The algorithm uses a few constant-space variables (`total_subarrays`, `current_zero_count`) regardless of the input array's size. No additional data structures that grow with `N` are used.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the total number of zero-filled subarrays in the given array.

    A zero-filled subarray is a contiguous subarray where every element is 0.
    For any contiguous block of k zeros, it contributes k * (k + 1) / 2 zero-filled subarrays.

    Args:
        nums: A list of integers.

    Returns:
        The total count of zero-filled subarrays.
    """
    total_subarrays = 0
    current_zero_count = 0

    for num in nums:
        if num == 0:
            # If the current element is 0, increment the count of consecutive zeros.
            current_zero_count += 1
        else:
            # If the current element is not 0, it breaks a sequence of zeros.
            # Add the subarrays formed by the previous sequence of zeros to the total.
            # A sequence of k zeros forms k * (k + 1) / 2 subarrays.
            total_subarrays += current_zero_count * (current_zero_count + 1) // 2
            # Reset the consecutive zero count.
            current_zero_count = 0

    # After the loop, there might be a pending sequence of zeros at the end of the array.
    # Add the subarrays formed by this final sequence to the total.
    total_subarrays += current_zero_count * (current_zero_count + 1) // 2

    return total_subarrays
```
</details>
