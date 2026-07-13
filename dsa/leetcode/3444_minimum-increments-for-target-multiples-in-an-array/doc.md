# Minimum Increments for Target Multiples in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3444 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-increments-for-target-multiples-in-an-array](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/).

### Goal
Given an array of integers `nums` and an array of target divisors `targets`, determine the minimum total increment required to ensure that for every element in `targets`, there exists at least one element in `nums` that is divisible by that target. You can increment any element in `nums` by 1 as many times as you like.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available numbers.
- `targets`: A list of integers representing the required divisors.

**Return value**

- An integer representing the minimum total increments needed to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], targets = [3, 5]`
- Output: `2`
- Explanation: Increment 3 to 5 (cost 2). Now 3 is divisible by 3, and 5 is divisible by 5.

**Example 2**

- Input: `nums = [8, 4], targets = [10, 5, 3]`
- Output: `13`
- Explanation: Increment 8 to 10 (cost 2), 4 to 5 (cost 1), and 4 to 6 (cost 2). Total cost 5? No, we need to satisfy all targets.

**Example 3**

- Input: `nums = [1, 2], targets = [2, 3]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with Bitmasking. Since the number of targets is small (up to 4), we can represent the set of satisfied targets using a bitmask of length $2^m$. We precompute the cost to make each `nums[i]` divisible by any subset of `targets` using the Least Common Multiple (LCM) to find the smallest increment. The DP state `dp[mask]` stores the minimum cost to satisfy the subset of targets represented by `mask`.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot 2^m + 2^m \cdot 2^m)$, where $n$ is the length of `nums` and $m$ is the length of `targets`.
- **Space Complexity**: $O(2^m)$ to store the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(nums: list[int], target: list[int]) -> int:
    m = len(target)
    num_masks = 1 << m

    def get_lcm(a, b):
        if a == 0 or b == 0: return 0
        return abs(a * b) // math.gcd(a, b)

    lcms = [1] * num_masks
    for mask in range(1, num_masks):
        bit = mask & -mask
        index = bit.bit_length() - 1
        lcms[mask] = get_lcm(lcms[mask ^ bit], target[index])

    # dp[mask] is the min cost to satisfy the subset of targets represented by mask
    dp = [float('inf')] * num_masks
    dp[0] = 0

    for num in nums:
        new_dp = dp[:]
        costs = [0] * num_masks
        for submask in range(1, num_masks):
            costs[submask] = (-num) % lcms[submask]

        for mask, current in enumerate(dp):
            if current == float('inf'):
                continue
            for submask in range(num_masks):
                new_mask = mask | submask
                new_dp[new_mask] = min(new_dp[new_mask], current + costs[submask])
        dp = new_dp

    return int(dp[num_masks - 1])
```
</details>
