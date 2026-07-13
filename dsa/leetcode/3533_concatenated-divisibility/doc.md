# Concatenated Divisibility

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3533 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [concatenated-divisibility](https://leetcode.com/problems/concatenated-divisibility/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/concatenated-divisibility/).

### Goal
Given an array of integers and an integer `k`, determine if there exists a non-empty subsequence of the array such that when the elements are concatenated in some order, the resulting large integer is divisible by `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available numbers.
- `k`: An integer representing the divisor.

**Return value**

- A boolean value: `True` if any permutation of a non-empty subsequence forms a number divisible by `k`, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `True` (e.g., "12" is divisible by 2)

**Example 2**

- Input: `nums = [4, 5], k = 3`
- Output: `False`

**Example 3**

- Input: `nums = [10, 2], k = 3`
- Output: `True` (e.g., "21" is divisible by 3)

---

## Solution
### Approach
The problem is solved using Dynamic Programming with Bitmasking. We track the possible remainders modulo `k` that can be formed using subsets of the input array. Since the order of concatenation matters, we precompute the remainder of each number `x` when shifted by the length of another number `y` (i.e., `x * 10^len(y) % k`). We use a DP table `dp[mask]` representing the set of possible remainders modulo `k` achievable using the subset of numbers indicated by the bitmask.

### Complexity Analysis
- **Time Complexity**: `O(2^n * n)`, where `n` is the number of elements in `nums`. We iterate through all possible subsets and for each, update the reachable remainders.
- **Space Complexity**: `O(2^n * k)`, to store the set of reachable remainders for every possible subset of the input array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> bool:
    n = len(nums)
    # Precompute lengths and powers of 10 mod k
    str_nums = [str(x) for x in nums]
    lengths = [len(s) for s in str_nums]
    remainders = [int(s) % k for s in str_nums]

    # powers[i][j] = 10^lengths[j] % k
    powers = [[0] * n for _ in range(n)]
    for i in range(n):
        p = pow(10, lengths[i], k)
        for j in range(n):
            powers[j][i] = p

    # dp[mask] stores a set of possible remainders modulo k
    # using the subset of numbers represented by the bitmask
    dp = [set() for _ in range(1 << n)]

    for i in range(n):
        dp[1 << i].add(remainders[i])

    for mask in range(1, 1 << n):
        if not dp[mask]:
            continue

        # Try adding a new number j not in mask
        for j in range(n):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                p_j = powers[j][mask] # 10^len(mask) % k
                # The new remainder is (current_remainder * 10^len(j) + remainder_j) % k
                # Wait, the order is: (existing_number * 10^len(new) + new_number) % k
                # So we need 10^len(new) % k

                # Correct logic:
                # If we append nums[j] to the end of the existing concatenation:
                # new_rem = (old_rem * 10^len(nums[j]) + nums[j]) % k

                shift = pow(10, lengths[j], k)
                for rem in dp[mask]:
                    new_rem = (rem * shift + remainders[j]) % k
                    dp[new_mask].add(new_rem)

    for mask in range(1, 1 << n):
        if 0 in dp[mask]:
            return True

    return False
```
</details>
