# Distinct Prime Factors of Product of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2521 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [distinct-prime-factors-of-product-of-array](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/).

### Goal
Given an array of integers, calculate the total number of unique prime factors present across the prime factorization of the product of all elements in the array. Essentially, you need to find the size of the union of prime factor sets for every number in the input array.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the count of distinct prime factors found across all numbers in the input array.

### Examples
**Example 1**

- Input: `nums = [2, 4, 3, 7, 10, 6]`
- Output: `4`
- Explanation: The product is 10080. The prime factors are 2, 3, 5, and 7.

**Example 2**

- Input: `nums = [2, 4, 8, 16]`
- Output: `1`
- Explanation: The only prime factor is 2.

**Example 3**

- Input: `nums = [3, 7, 11]`
- Output: `3`
- Explanation: The prime factors are 3, 7, and 11.

---

## Solution
### Approach
The solution utilizes trial division to perform prime factorization on each number in the input array. By maintaining a global `set` data structure, we collect all unique prime factors encountered. Since the maximum value of an element is typically small (up to 1000 in this problem context), trial division up to the square root of each number is highly efficient.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot \sqrt{M})$, where $N$ is the number of elements in the array and $M$ is the maximum value in the array. For each number, we perform trial division up to its square root.
- **Space Complexity**: $O(P)$, where $P$ is the number of distinct prime factors across all elements. In the worst case, this is bounded by the number of primes up to $M$.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of distinct prime factors of the product of all elements in nums.
    """
    distinct_primes = set()

    for n in nums:
        d = 2
        temp = n
        # Trial division up to sqrt(temp)
        while d * d <= temp:
            if temp % d == 0:
                distinct_primes.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        # If temp > 1, the remaining value is a prime factor
        if temp > 1:
            distinct_primes.add(temp)

    return len(distinct_primes)
```
</details>
