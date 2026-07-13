# Maximum Points Tourist Can Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3332 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-points-tourist-can-earn](https://leetcode.com/problems/maximum-points-tourist-can-earn/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-points-tourist-can-earn/).

### Goal
A tourist is planning a trip over a fixed number of days across several cities. Each day, the tourist can either stay in their current city or travel to a different city. The points earned depend on the city visited and the day of the visit. Additionally, there are specific travel costs (or bonuses) associated with moving between any two cities. The objective is to determine the maximum total points the tourist can accumulate by the end of the trip.

### Function Contract
**Inputs**

- `n`: An integer representing the number of cities.
- `k`: An integer representing the number of days.
- `stayScore`: A 2D list of integers where `stayScore[day][city]` is the points earned for staying in `city` on `day`.
- `travelScore`: A 2D list of integers where `travelScore[i][j]` is the points earned for traveling from city `i` to city `j`.

**Return value**

- An integer representing the maximum total points possible after `k` days.

### Examples
**Example 1**

- Input: `n = 2, k = 1, stayScore = [[2, 3]], travelScore = [[0, 2], [1, 0]]`
- Output: `3`

**Example 2**

- Input: `n = 2, k = 2, stayScore = [[1, 3], [4, 1]], travelScore = [[0, 2], [1, 0]]`
- Output: `7`

**Example 3**

- Input: `n = 3, k = 1, stayScore = [[4, 1, 2]], travelScore = [[0, 3, 3], [1, 0, 1], [2, 1, 0]]`
- Output: `4`

---

## Solution
### Approach
Dynamic Programming. We maintain a state `dp[day][city]` representing the maximum points earned up to `day` ending in `city`. The transition involves checking all possible previous cities from which the tourist could have arrived (or stayed) on the current day.

### Complexity Analysis
- **Time Complexity**: `O(k * n^2)`, where `k` is the number of days and `n` is the number of cities, as we iterate through each day and evaluate transitions between all pairs of cities.
- **Space Complexity**: `O(n)` if optimized to store only the current and previous day's results, or `O(k * n)` for the full DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
    dp = [0] * n

    for day in range(k):
        new_dp = [0] * n
        for curr_city in range(n):
            best_prev = dp[curr_city] + stayScore[day][curr_city]

            for prev_city in range(n):
                if prev_city != curr_city:
                    best_prev = max(best_prev, dp[prev_city] + travelScore[prev_city][curr_city])

            new_dp[curr_city] = best_prev
        dp = new_dp

    return max(dp)
```
</details>
