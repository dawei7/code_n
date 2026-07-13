# Number of Ways to Earn Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2585 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-to-earn-points](https://leetcode.com/problems/number-of-ways-to-earn-points/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-to-earn-points/).

### Goal
Given a target total score and a list of available question types, where each type has a specific point value and a limited count of questions available, determine the total number of distinct ways to achieve exactly the target score. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `target`: An integer representing the exact score to reach.
- `types`: A list of lists, where each inner list `[count_i, marks_i]` indicates that there are `count_i` questions available, each worth `marks_i` points.

**Return value**

- An integer representing the number of ways to reach the target score, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `target = 6, types = [[6,1],[3,2],[2,3]]`
- Output: `7`

**Example 2**

- Input: `target = 5, types = [[50,1],[50,2],[50,5]]`
- Output: `4`

**Example 3**

- Input: `target = 18, types = [[6,1],[3,2],[2,3]]`
- Output: `1`

---

## Solution
### Approach
This problem is a variation of the **Bounded Knapsack Problem**. It can be solved using **Dynamic Programming** with a 1D array (space-optimized) or a 2D array. We maintain a DP table where `dp[s]` represents the number of ways to achieve score `s`. For each question type, we update the DP table by considering taking 0 to `count_i` questions of that type.

### Complexity Analysis
- **Time Complexity**: O(target * N * max(count_i)), where N is the number of question types. This can be optimized to O(target * N) using prefix sums or sliding window techniques to update the DP table.
- **Space Complexity**: O(target) to store the number of ways to reach each score up to the target.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(target: int, types: list[list[int]]) -> int:
    MOD = 10**9 + 7

    # dp[i] stores the number of ways to get a total score of i
    dp = [0] * (target + 1)
    dp[0] = 1

    for count, marks in types:
        new_dp = [0] * (target + 1)
        # We use a prefix sum approach to update the DP table efficiently.
        # For a specific question type with 'count' items of 'marks' value:
        # new_dp[j] = sum(dp[j - k * marks]) for 0 <= k <= count
        # This is equivalent to:
        # new_dp[j] = new_dp[j - marks] + dp[j] - dp[j - (count + 1) * marks]

        for j in range(target + 1):
            # Current ways to reach j using previous types
            new_dp[j] = dp[j]

            # Add ways by taking 1 to 'count' items of current type
            if j >= marks:
                new_dp[j] = (new_dp[j] + new_dp[j - marks]) % MOD

            # Subtract ways that exceed the 'count' limit
            if j >= (count + 1) * marks:
                new_dp[j] = (new_dp[j] - dp[j - (count + 1) * marks] + MOD) % MOD

        dp = new_dp

    return dp[target]
```
</details>
