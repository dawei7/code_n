# Count the Number of Infection Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2954 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-infection-sequences](https://leetcode.com/problems/count-the-number-of-infection-sequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-infection-sequences/).

### Goal
Given an integer `n` representing the total number of computers (indexed 0 to n-1) and an array `sick` representing the indices of initially infected computers, calculate the total number of distinct sequences in which the remaining healthy computers can become infected. An infection spreads to adjacent healthy computers at each time step. The result should be returned modulo 10^9 + 7.

### Function Contract
**Inputs**

- `n`: An integer representing the total number of computers.
- `sick`: A list of integers representing the indices of initially infected computers.

**Return value**

- An integer representing the total number of valid infection sequences modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `n = 5, sick = [0, 4]`
- Output: `4`

**Example 2**

- Input: `n = 4, sick = [1]`
- Output: `3`

**Example 3**

- Input: `n = 4, sick = [0, 1, 2, 3]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using combinatorics. We identify the gaps of healthy computers between infected ones.
1. For gaps at the ends (before the first sick computer or after the last), there is only one way to fill them (inward).
2. For gaps between two sick computers of size `k`, there are `2^(k-1)` ways to fill them.
3. The total number of ways is the multinomial coefficient of the sizes of all gaps multiplied by the product of the ways to fill each internal gap.

### Complexity Analysis
- **Time Complexity**: `O(n)` to precompute factorials and modular inverses.
- **Space Complexity**: `O(n)` to store factorials and their inverses.

### Reference Implementations
<details>
<summary>python</summary>

```python
MOD = 10**9 + 7

def solve(n: int, sick: list[int]) -> int:
    if not sick:
        return 0

    # Precompute factorials for combinations
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        num = fact[n]
        den = (inv[r] * inv[n - r]) % MOD
        return (num * den) % MOD

    gaps = []
    # Gap before the first sick computer
    gaps.append(sick[0])
    # Gaps between sick computers
    for i in range(len(sick) - 1):
        gaps.append(sick[i + 1] - sick[i] - 1)
    # Gap after the last sick computer
    gaps.append(n - 1 - sick[-1])

    total_healthy = n - len(sick)
    ans = fact[total_healthy]

    # Divide by the factorial of each gap size (multinomial coefficient)
    for g in gaps:
        ans = (ans * inv[g]) % MOD

    # Multiply by 2^(k-1) for each internal gap of size k
    for i in range(1, len(gaps) - 1):
        if gaps[i] > 0:
            ans = (ans * pow(2, gaps[i] - 1, MOD)) % MOD

    return ans
```
</details>
