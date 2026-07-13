# Maximum Total Reward Using Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3181 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-total-reward-using-operations-ii](https://leetcode.com/problems/maximum-total-reward-using-operations-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-total-reward-using-operations-ii/).

### Goal
Given an array of reward values, you start with a current total reward of 0. You can select a reward value `x` from the array if `x` is strictly greater than your current total reward. Upon selection, your total reward increases by `x`. The objective is to determine the maximum possible total reward you can achieve by performing this operation any number of times.

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

- Input: `[1, 5, 10]`
- Output: `15`

---

## Solution
### Approach
The problem is a variation of the subset sum problem. Since the constraints on the values are large, we use bit manipulation to represent the set of reachable total rewards. By sorting the unique reward values, we can maintain a bitmask `bits` where the $i$-th bit is set if a total reward of $i$ is achievable. For each reward `x`, we update the bitmask using `bits |= (bits & ((1 << x) - 1)) << x`. This efficiently computes all reachable states in $O(N \log N + \frac{M \cdot N}{W})$ time, where $M$ is the maximum reward and $W$ is the word size.

### Complexity Analysis
- **Time Complexity**: $O(N \log N + \frac{M \cdot N}{W})$, where $N$ is the number of rewards, $M$ is the maximum possible reward, and $W$ is the word size (typically 64). The sorting takes $O(N \log N)$, and the bitwise operations take $O(M/W)$ per unique reward.
- **Space Complexity**: $O(M/W)$ to store the bitmask representing reachable states.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(reward_values: list[int]) -> int:
    # Sort and remove duplicates to optimize the DP transitions
    rewards = sorted(set(reward_values))

    # bits represents the set of reachable total rewards.
    # If the i-th bit is 1, then a total reward of i is possible.
    bits = 1

    for x in rewards:
        # We can only pick reward x if current_total < x.
        # This means we only care about reachable totals < x.
        # The mask (1 << x) - 1 extracts all bits from 0 to x-1.
        # Shifting by x adds x to all those reachable totals.
        bits |= (bits & ((1 << x) - 1)) << x

    # The answer is the highest bit set in the bitmask.
    return bits.bit_length() - 1
```
</details>
