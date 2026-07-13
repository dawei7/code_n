# Maximum Prime Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3115 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-prime-difference](https://leetcode.com/problems/maximum-prime-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-prime-difference/).

### Goal
Given an integer array, identify the indices of the first and last prime numbers present in the array. The objective is to calculate the absolute difference between these two indices.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element is between 1 and 100.

**Return value**

- An integer representing the maximum distance (difference in indices) between any two prime numbers found in the array.

### Examples
**Example 1**

- Input: `nums = [4, 2, 9, 5, 3]`
- Output: `3`
- Explanation: The prime numbers are 2, 5, and 3 at indices 1, 3, and 4. The maximum difference is 4 - 1 = 3.

**Example 2**

- Input: `nums = [4, 8, 1, 2]`
- Output: `0`
- Explanation: The only prime number is 2 at index 3. The difference is 3 - 3 = 0.

**Example 3**

- Input: `nums = [10, 12, 14]`
- Output: `0`
- Explanation: No prime numbers exist; the logic handles this by returning 0.

---

## Solution
### Approach
The solution utilizes a primality test (specifically a helper function or precomputed sieve) to identify prime numbers. Since the constraints are small (numbers up to 100), a simple trial division or a boolean lookup table is efficient. We perform a single linear scan to find the index of the first prime and the index of the last prime, then return their difference.

### Complexity Analysis
- **Time Complexity**: `O(N * sqrt(M))`, where `N` is the length of the array and `M` is the maximum value in the array (100). Given the constraints, this is effectively `O(N)`.
- **Space Complexity**: `O(1)` (excluding the input array), as we only store two integer pointers for the indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(nums: list[int]) -> int:
    first_prime_idx = -1
    last_prime_idx = -1

    for i, num in enumerate(nums):
        if is_prime(num):
            if first_prime_idx == -1:
                first_prime_idx = i
            last_prime_idx = i

    if first_prime_idx == -1:
        return 0

    return last_prime_idx - first_prime_idx
```
</details>
