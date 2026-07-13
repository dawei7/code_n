# Maximum Total Reward Using Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3180 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-total-reward-using-operations-i](https://leetcode.com/problems/maximum-total-reward-using-operations-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-total-reward-using-operations-i/).

### Goal
Given an array of reward values, you start with a current total reward of 0. You can perform an operation: select an integer `x` from the array such that `x` is strictly greater than your current total reward. If you select `x`, your total reward increases by `x`. The goal is to find the maximum possible total reward you can achieve by performing this operation any number of times.

### Function Contract
**Inputs**

- `rewardValues`: A list of integers representing the available rewards.

**Return value**

- An integer representing the maximum total reward achievable.

### Examples
**Example 1**

- Input: `rewardValues = [1, 1, 3, 3]`
- Output: `4`

**Example 2**

- Input: `rewardValues = [1, 6, 4, 3, 2]`
- Output: `11`

**Example 3**

- Input: `rewardValues = [1, 5, 10]`
- Output: `15`

---

## Solution
### Approach
The problem is a variation of the 0/1 Knapsack problem. Since we want to find all reachable sums, we can use Dynamic Programming. By sorting the rewards, we ensure that we only consider adding a reward `x` if it is greater than the current sum. Using bit manipulation (specifically bitsets), we can represent the set of reachable sums efficiently. If `dp` is a bitmask where the `i`-th bit is 1 if sum `i` is reachable, then adding a reward `x` corresponds to `dp |= (dp & mask) << x`, where `mask` only includes bits less than `x`.

### Complexity Analysis
- **Time Complexity**: `O(N log N + N * M / W)`, where `N` is the number of rewards, `M` is the maximum possible reward (sum of all elements), and `W` is the word size (typically 64). Sorting takes `O(N log N)`, and the bitset operations take `O(N * M / W)`.
- **Space Complexity**: `O(M / W)` to store the bitmask representing reachable sums.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(reward_values: list[int]) -> int:
    # Sort rewards to process them in increasing order
    # This ensures that when we consider reward x, we only care about
    # sums that are strictly less than x.
    rewardValues = sorted(set(reward_values))

    # dp is a bitmask where the i-th bit is 1 if sum i is reachable.
    # Initially, only sum 0 is reachable.
    dp = 1

    for x in rewardValues:
        # We can only add x if the current sum 's' is < x.
        # This corresponds to taking the bits of dp that are less than x,
        # shifting them left by x, and ORing them into the current dp.
        # (dp & ((1 << x) - 1)) extracts bits 0 to x-1.
        dp |= (dp & ((1 << x) - 1)) << x

    # The answer is the highest bit set in the bitmask.
    return dp.bit_length() - 1
```
</details>
