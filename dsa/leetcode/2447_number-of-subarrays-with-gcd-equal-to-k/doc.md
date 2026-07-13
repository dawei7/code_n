# Number of Subarrays With GCD Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2447 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-subarrays-with-gcd-equal-to-k](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/).

### Goal
Given an integer array and a target integer `k`, determine the total count of contiguous subarrays where the greatest common divisor (GCD) of all elements within that subarray is exactly equal to `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums[i] <= 10^6.
- `k`: An integer representing the target GCD value.

**Return value**

- An integer representing the total number of contiguous subarrays whose GCD equals `k`.

### Examples
**Example 1**

- Input: `nums = [9, 3, 1, 2, 6, 3], k = 3`
- Output: `4`
- Explanation: The subarrays are [9, 3], [3], [3], [6, 3].

**Example 2**

- Input: `nums = [4], k = 7`
- Output: `0`
- Explanation: No subarray has a GCD of 7.

**Example 3**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`
- Explanation: All possible subarrays have a GCD of 1.

---

## Solution
### Approach
The solution utilizes the property that the GCD of a subarray is non-increasing as the subarray expands. By iterating through each starting index and expanding the subarray, we can maintain a running GCD. Since the GCD of a sequence can only change at most O(log(max(nums))) times, we can efficiently count valid subarrays.

### Complexity Analysis
- **Time Complexity**: O(n * log(max(nums))), where n is the length of the array. For each starting position, the GCD value changes at most logarithmic times relative to the maximum value in the array.
- **Space Complexity**: O(1), as we only use a few variables to track the current GCD and the running count.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays with GCD equal to k.
    Uses the property that GCD is non-increasing as we extend the subarray.
    """
    n = len(nums)
    count = 0

    for i in range(n):
        current_gcd = nums[i]
        for j in range(i, n):
            current_gcd = math.gcd(current_gcd, nums[j])

            if current_gcd == k:
                count += 1
            elif current_gcd < k:
                # Since the GCD can only decrease or stay the same,
                # if it drops below k, it will never return to k.
                break

    return count
```
</details>
