# Minimum Cost to Equalize Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3139 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-equalize-array](https://leetcode.com/problems/minimum-cost-to-equalize-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-equalize-array/).

### Goal
Given an array of integers, determine the minimum cost to make all elements equal to some target value $T$, where $T \ge \max(\text{nums})$. You can increment any element by 1 at a cost of `cost1`, or increment two distinct elements by 1 at a cost of `cost2`. The goal is to find the minimum total cost across all possible target values $T$ (specifically, $T$ can range from $\max(\text{nums})$ to $2 \times \max(\text{nums})$).

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `cost1`: An integer representing the cost to increment a single element.
- `cost2`: An integer representing the cost to increment two distinct elements.

**Return value**

- An integer representing the minimum cost to make all elements equal, modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [4,1], cost1 = 5, cost2 = 2`
- Output: `15`

**Example 2**

- Input: `nums = [2,3,3,3,5], cost1 = 2, cost2 = 1`
- Output: `6`

**Example 3**

- Input: `nums = [3,5,3], cost1 = 1, cost2 = 3`
- Output: `4`

---

## Solution
### Approach
The problem is solved by iterating over possible target values $T$. For a fixed $T$, let $S$ be the sum of differences $(T - \text{nums}[i])$ and $M$ be the maximum difference. If $2 \times M \le S$, we can pair up increments efficiently using `cost2` as much as possible. If $2 \times M > S$, we are forced to use `cost1` for the remaining increments of the maximum element after pairing all other elements. We use mathematical optimization to calculate the cost for each $T$ and take the minimum.

### Complexity Analysis
- **Time Complexity**: $O(N)$, where $N$ is the length of the array, due to the initial pass to find the sum and max, followed by a linear scan over the possible target values.
- **Space Complexity**: $O(1)$, as we only store a few variables regardless of input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], cost1: int, cost2: int) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    min_val = min(nums)
    max_val = max(nums)
    total_sum = sum(nums)
    MOD = 10**9 + 7

    def get_cost(target):
        s = n * target - total_sum
        m = target - min_val

        # If we can pair up almost all increments
        if 2 * m <= s:
            # Use cost2 for s // 2 pairs, cost1 for s % 2
            return (s // 2) * min(2 * cost1, cost2) + (s % 2) * cost1
        else:
            # We are forced to use cost1 for the excess of the max element
            # The number of pairs we can form is (s - m)
            # The remaining (m - (s - m)) = 2m - s elements must be filled with cost1
            pairs = s - m
            remainder = m - pairs
            return pairs * min(2 * cost1, cost2) + remainder * cost1

    ans = float('inf')
    # The target can range from max_val to 2 * max_val
    # We check target = max_val and target = max_val + 1 separately
    # because the logic for the "bottleneck" element changes.
    for target in range(max_val, 2 * max_val + 1):
        ans = min(ans, get_cost(target))

    return ans % MOD
```
</details>
