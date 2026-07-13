# Number of Subarrays With LCM Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2470 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-subarrays-with-lcm-equal-to-k](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/).

### Goal
Given an array of positive integers and an integer `k`, determine the total count of contiguous subarrays where the Least Common Multiple (LCM) of all elements within that subarray is exactly equal to `k`.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).
- `k`: A positive integer representing the target LCM value.

**Return value**

- An integer representing the count of contiguous subarrays whose LCM equals `k`.

### Examples
**Example 1**

- Input: `nums = [3, 6, 2, 7, 1], k = 6`
- Output: `4`
- Explanation: The subarrays with LCM 6 are [3, 6], [3, 6, 2], [6], and [6, 2].

**Example 2**

- Input: `nums = [3], k = 2`
- Output: `0`
- Explanation: No subarray has an LCM of 2.

**Example 3**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `6`
- Explanation: All subarrays [1], [1], [1], [1, 1], [1, 1], and [1, 1, 1] have an LCM of 1.

---

## Solution
### Approach
The solution utilizes the property that the LCM of a sequence can be computed iteratively: `lcm(a, b, c) = lcm(lcm(a, b), c)`. Since the LCM of a subarray is non-decreasing as we extend the subarray, we can iterate through all possible starting positions and expand the subarray, updating the running LCM. We prune the search if the current LCM exceeds `k` or is not a divisor of `k`.

### Complexity Analysis
- **Time Complexity**: `O(n^2 * log(max(nums)))`, where `n` is the length of the array. We iterate through all subarrays, and each LCM calculation takes logarithmic time relative to the values.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the current LCM and the total count.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0

    for i in range(n):
        current_lcm = nums[i]
        for j in range(i, n):
            current_lcm = lcm(current_lcm, nums[j])

            # If current_lcm exceeds k or is not a divisor of k,
            # any further extension will not result in an LCM of k.
            if current_lcm > k or k % current_lcm != 0:
                break

            if current_lcm == k:
                count += 1

    return count
```
</details>
