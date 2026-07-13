# Special Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2741 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [special-permutations](https://leetcode.com/problems/special-permutations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/special-permutations/).

### Goal
Given a 0-indexed integer array `nums` containing $n$ distinct positive integers, find the total number of "special" permutations of `nums`. A permutation is considered **special** if, for every adjacent pair of elements in the permutation, one of the elements divides the other. Specifically, for all $0 \le i < n - 1$, either `nums[i] % nums[i+1] == 0` or `nums[i+1] % nums[i] == 0`.

Since the total number of special permutations can be very large, return the result modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums`: `List[int]` — An array of $n$ distinct positive integers, where $2 \le n \le 14$.

**Return value**

- `int` — The total number of special permutations modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [2, 3, 6]`
- Output: `2`
- Explanation: The special permutations are:
  - `[3, 6, 2]` (since 6 is divisible by 3, and 6 is divisible by 2)
  - `[2, 6, 3]` (since 6 is divisible by 2, and 6 is divisible by 3)

**Example 2**

- Input: `nums = [1, 4, 3]`
- Output: `2`
- Explanation: The special permutations are:
  - `[3, 1, 4]` (since 3 is divisible by 1, and 4 is divisible by 1)
  - `[4, 1, 3]` (since 4 is divisible by 1, and 3 is divisible by 1)

---

## Solution
### Approach
The problem can be modeled as finding the number of Hamiltonian paths in a directed graph where an edge exists between $u$ and $v$ if $u$ divides $v$ or $v$ divides $u$. Since the number of elements $n$ is very small ($n \le 14$), we can solve this efficiently using **Dynamic Programming with Bitmasking**.

### State Representation
We define our DP state as `dp(mask, last_idx)`:
- `mask`: A bitmask of length $n$ where the $i$-th bit is set to `1` if the element `nums[i]` has already been placed in the permutation, and `0` otherwise.
- `last_idx`: The index of the last element placed in the permutation.

### Transitions
To transition from a state `(mask, last_idx)`:
1. We iterate through all possible next elements `nxt` that have not been visited yet (i.e., the `nxt`-th bit in `mask` is `0`).
2. If `nums[last_idx]` divides `nums[nxt]` or `nums[nxt]` divides `nums[last_idx]`, we can transition to the state `(mask | (1 << nxt), nxt)`.
3. The base case is reached when `mask == (1 << n) - 1` (all elements have been placed), which contributes `1` to the count of valid permutations.

To optimize transitions, we precompute an adjacency list `adj` where `adj[i]` contains all indices `j` that satisfy the divisibility condition with `i`.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n^2 \cdot 2^n)$. There are $n \cdot 2^n$ states in our DP table. From each state, we transition to at most $n$ other states. For $n = 14$, the number of operations is roughly $14^2 \cdot 2^{14} \approx 3.2 \times 10^6$, which easily runs within the time limit.
- **Space Complexity**: $\mathcal{O}(n \cdot 2^n)$ to store the memoization table of size $2^n \times n$, plus $\mathcal{O}(n^2)$ space for the precomputed adjacency list.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    # Precompute divisibility relations to optimize transitions
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    adj[i].append(j)

    # memo[mask][last_idx] stores the number of valid ways to complete
    # the permutation given the current mask of visited elements and the last visited index.
    memo = [[-1] * n for _ in range(1 << n)]
    target_mask = (1 << n) - 1

    def dp(mask: int, last_idx: int) -> int:
        if mask == target_mask:
            return 1
        if memo[mask][last_idx] != -1:
            return memo[mask][last_idx]

        ans = 0
        for nxt in adj[last_idx]:
            if not (mask & (1 << nxt)):
                ans = (ans + dp(mask | (1 << nxt), nxt)) % MOD

        memo[mask][last_idx] = ans
        return ans

    total_permutations = 0
    # Start the permutation with each element as the first element
    for i in range(n):
        total_permutations = (total_permutations + dp(1 << i, i)) % MOD

    return total_permutations
```
</details>
