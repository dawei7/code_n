# Prime Pairs With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2761 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [prime-pairs-with-target-sum](https://leetcode.com/problems/prime-pairs-with-target-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/prime-pairs-with-target-sum/).

### Goal
Given an integer `n`, identify all unique pairs of prime numbers `(x, y)` such that their sum equals `n` and `x <= y`. The result should be returned as a list of pairs sorted in ascending order of the first element. If no such pairs exist, return an empty list.

### Function Contract
**Inputs**

- `n`: An integer representing the target sum.

**Return value**

- A list of lists, where each inner list contains two integers `[x, y]` such that `x + y == n`, `x` and `y` are prime, and `x <= y`.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `[[3, 7], [5, 5]]`

**Example 2**

- Input: `n = 2`
- Output: `[]`

**Example 3**

- Input: `n = 1`
- Output: `[]`

---

## Solution
### Approach
The problem is solved using the **Sieve of Eratosthenes** to precompute all prime numbers up to `n`. Once the sieve is generated, we iterate from `2` up to `n // 2`. For each integer `i`, we check if both `i` and `n - i` are marked as prime in our sieve. If they are, we add the pair `[i, n - i]` to our result list.

### Complexity Analysis
- **Time Complexity**: `O(n log log n)` due to the Sieve of Eratosthenes, followed by an `O(n)` linear scan to find the pairs.
- **Space Complexity**: `O(n)` to store the boolean array representing the primality of numbers up to `n`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int) -> list[list[int]]:
    if n < 4:
        return []

    # Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    result = []
    # Iterate to find pairs (x, y) such that x + y = n and x <= y
    for x in range(2, n // 2 + 1):
        y = n - x
        if is_prime[x] and is_prime[y]:
            result.append([x, y])

    return result
```
</details>
