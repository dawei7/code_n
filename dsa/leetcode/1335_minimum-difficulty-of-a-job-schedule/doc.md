# Minimum Difficulty of a Job Schedule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1335 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-difficulty-of-a-job-schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/).

### Goal
Schedule jobs in their given order over exactly `d` days. Each day must contain at least one job, and a day's difficulty is the maximum job difficulty assigned to that day. Minimize the total difficulty.

### Function Contract
**Inputs**

- `jobDifficulty`: difficulty of each job in fixed order.
- `d`: number of days.

**Return value**

The minimum possible total difficulty, or `-1` if scheduling is impossible.

### Examples
**Example 1**

- Input: `jobDifficulty = [6,5,4,3,2,1]`, `d = 2`
- Output: `7`

**Example 2**

- Input: `jobDifficulty = [9,9,9]`, `d = 4`
- Output: `-1`

**Example 3**

- Input: `jobDifficulty = [1,1,1]`, `d = 3`
- Output: `3`

---

## Solution
### Approach
Dynamic programming over ordered partitions.

### Complexity Analysis
- **Time Complexity**: `O(d * n^2)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(job_difficulty, d):
    n = len(job_difficulty)
    if n < d:
        return -1
    dp = job_difficulty[:]
    for i in range(n - 2, -1, -1):
        dp[i] = max(job_difficulty[i], dp[i + 1])

    for day in range(2, d + 1):
        next_dp = [float("inf")] * n
        for i in range(n - day + 1):
            hardest = 0
            for cut in range(i, n - day + 1):
                hardest = max(hardest, job_difficulty[cut])
                next_dp[i] = min(next_dp[i], hardest + dp[cut + 1])
        dp = next_dp
    return dp[0]
```
</details>
