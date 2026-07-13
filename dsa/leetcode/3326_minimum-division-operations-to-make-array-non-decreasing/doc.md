# Minimum Division Operations to Make Array Non Decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3326 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-division-operations-to-make-array-non-decreasing](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/).

### Goal
Given an array of integers, you are allowed to replace an element by dividing it by its greatest proper divisor. For a composite number, this leaves its smallest prime factor. The objective is to determine the minimum number of operations required to transform the array into a non-decreasing sequence. If it is impossible to achieve this state, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where $1 \le nums[i] \le 10^6$.

**Return value**

- An integer representing the minimum operations, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [25, 7]`
- Output: `1`
- Explanation: Divide 25 by its greatest proper divisor, 5, which leaves 5. The array becomes [5, 7], which is non-decreasing.

**Example 2**

- Input: `nums = [7, 7, 6]`
- Output: `-1`
- Explanation: 6 cannot be reduced to a value $\le 7$ that maintains the non-decreasing property.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `0`
- Explanation: The array is already non-decreasing.

---

## Solution
### Approach
The problem relies on **Number Theory** (specifically precomputing the smallest prime factor using a **Sieve of Eratosthenes**) and a **Greedy** strategy. Since we want to make the array non-decreasing with minimum operations, we process the array from right to left. For each element, if it is greater than the element to its right, we replace it with its smallest proper divisor. If the resulting value is still greater than the right neighbor, it is impossible to satisfy the condition.

### Complexity Analysis
- **Time Complexity**: $O(N + M \log \log M)$, where $N$ is the length of the array and $M$ is the maximum value in the array ($10^6$). The sieve takes $O(M \log \log M)$ and the array traversal takes $O(N)$.
- **Space Complexity**: $O(M)$ to store the smallest prime factors for all numbers up to $10^6$.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache


def _build_primes(limit: int = 1000) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if is_prime[value]:
            for multiple in range(value * value, limit + 1, value):
                is_prime[multiple] = False
    return [value for value in range(2, limit + 1) if is_prime[value]]


_PRIMES = _build_primes()


@lru_cache(maxsize=None)
def _smallest_prime_factor(value: int) -> int:
    if value < 4:
        return value
    for prime in _PRIMES:
        if prime * prime > value:
            return value
        if value % prime == 0:
            return prime
    return value


def solve(nums: list[int]) -> int:
    nums = nums[:]
    operations = 0

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            continue

        reduced = _smallest_prime_factor(nums[i])
        if reduced == nums[i] or reduced > nums[i + 1]:
            return -1

        nums[i] = reduced
        operations += 1

    return operations
```
</details>
