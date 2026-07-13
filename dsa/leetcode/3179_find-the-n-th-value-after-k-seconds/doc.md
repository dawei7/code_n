# Find the N-th Value After K Seconds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3179 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation, Combinatorics, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-n-th-value-after-k-seconds](https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/).

### Goal
Given an array of size `n` initialized with all 1s, simulate a process that repeats `k` times. In each second, every element at index `i` is updated to be the sum of all elements from index `0` to `i` in the current array. Determine the value at the last index (index `n-1`) after exactly `k` seconds have elapsed, returning the result modulo 10^9 + 7.

### Function Contract
**Inputs**

- `n` (int): The number of elements in the array.
- `k` (int): The number of seconds to perform the update process.

**Return value**

- `int`: The value at the last index of the array after `k` seconds, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `n = 4, k = 5`
- Output: `56`

**Example 2**

- Input: `n = 5, k = 3`
- Output: `35`

---

## Solution
### Approach
The problem can be modeled using combinatorics. After `k` seconds, the value at index `i` (0-indexed) is given by the binomial coefficient `C(i + k, i)` or equivalently `C(i + k, k)`. Since we need the value at index `n-1` after `k` seconds, we calculate `C((n-1) + k, k)`. This is derived from the property that the prefix sum operation is equivalent to moving down the Pascal's triangle.

### Complexity Analysis
- **Time Complexity**: `O(n)`: We compute the binomial coefficient using the multiplicative formula, which requires a single loop up to `n`.
- **Space Complexity**: `O(1)`: We only store a few integer variables for the calculation.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, k: int) -> int:
    """
    Calculates the value at index n-1 after k seconds.
    The value at index i after k seconds is C(i + k, i).
    For index n-1, this is C(n - 1 + k, n - 1) = C(n + k - 1, k).
    """
    MOD = 10**9 + 7

    # We need to calculate C(n + k - 1, k)
    # C(N, K) = N! / (K! * (N-K)!)
    # Here N = n + k - 1, K = k
    # C(n + k - 1, k) = [(n+k-1) * (n+k-2) * ... * (n)] / k!

    N = n + k - 1
    K = min(k, n - 1)

    if K < 0:
        return 0
    if K == 0:
        return 1

    # Calculate C(N, K)
    numerator = 1
    denominator = 1
    for i in range(K):
        numerator = (numerator * (N - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD

    # Modular inverse using Fermat's Little Theorem
    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
```
</details>
