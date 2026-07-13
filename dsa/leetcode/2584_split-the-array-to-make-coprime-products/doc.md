# Split the Array to Make Coprime Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2584 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [split-the-array-to-make-coprime-products](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/split-the-array-to-make-coprime-products/).

### Goal
Determine if an array can be partitioned into two non-empty contiguous subarrays such that the product of all elements in the left subarray and the product of all elements in the right subarray share no common prime factors (i.e., their greatest common divisor is 1).

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le nums[i] \le 10^6$.

**Return value**

- An integer representing the index $i$ such that the prefix `nums[0...i]` and suffix `nums[i+1...n-1]` are coprime, or `-1` if no such split exists.

### Examples
**Example 1**

- Input: `nums = [4,7,8,15,3,5]`
- Output: `2`
- Explanation: Left product is $4 \times 7 \times 8 = 224$. Right product is $15 \times 3 \times 5 = 225$. $\gcd(224, 225) = 1$.

**Example 2**

- Input: `nums = [4,7,15,8,3,5]`
- Output: `-1`

**Example 3**

- Input: `nums = [2,3,3]`
- Output: `0`

---

## Solution
### Approach
The solution relies on **Prime Factorization** and **Interval Tracking**. Since the products can be extremely large, we avoid computing them directly. Instead, we track the "first" and "last" occurrence of every prime factor present in the array. A split is valid at index $i$ if no prime factor present in the prefix `nums[0...i]` appears in the suffix `nums[i+1...n-1]`. This is equivalent to checking if the maximum "last occurrence" index of all prime factors in the prefix is less than or equal to $i$.

### Complexity Analysis
- **Time Complexity**: $O(N \sqrt{M})$, where $N$ is the length of the array and $M$ is the maximum value in the array (due to prime factorization). This can be optimized to $O(N \log \log M)$ using a precomputed sieve.
- **Space Complexity**: $O(P)$, where $P$ is the number of distinct prime factors across all elements in the array.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math
from collections import defaultdict

def solve(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return -1

    # Map each prime factor to its first and last occurrence index
    first_occurrence = {}
    last_occurrence = {}

    def get_prime_factors(num):
        factors = set()
        d = 2
        temp = num
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
        return factors

    # Precompute prime factors for each number
    all_factors = []
    for i, x in enumerate(nums):
        factors = get_prime_factors(x)
        all_factors.append(factors)
        for p in factors:
            if p not in first_occurrence:
                first_occurrence[p] = i
            last_occurrence[p] = i

    # We need to find a split point i such that for all prime factors p
    # present in nums[0...i], their last occurrence is <= i.
    # This ensures no prime factor in the left part exists in the right part.

    max_last_idx = -1
    for i in range(n - 1):
        # Update the furthest index any prime factor in the current prefix reaches
        for p in all_factors[i]:
            max_last_idx = max(max_last_idx, last_occurrence[p])

        # If the furthest index any prime factor in the prefix reaches is <= i,
        # then no prime factor from the prefix exists in the suffix.
        if max_last_idx <= i:
            return i

    return -1
```
</details>
