# Maximum Profit in Job Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1235 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-profit-in-job-scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-profit-in-job-scheduling/).

### Goal
Choose a set of non-overlapping jobs to maximize total profit. A job ending at time `t` does not conflict with a job starting at time `t`.

### Function Contract
**Inputs**

- `startTime`: job start times.
- `endTime`: job end times.
- `profit`: job profits at the same indices.

**Return value**

The maximum profit obtainable from compatible jobs.

### Examples
**Example 1**

- Input: `startTime = [1,2,3,3]`, `endTime = [3,4,5,6]`, `profit = [50,10,40,70]`
- Output: `120`

**Example 2**

- Input: `startTime = [1,2,3,4,6]`, `endTime = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`
- Output: `150`

**Example 3**

- Input: `startTime = [1,1,1]`, `endTime = [2,3,4]`, `profit = [5,6,4]`
- Output: `6`

---

## Solution
### Approach
Weighted interval scheduling with binary search.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_right


def solve(start_time, end_time, profit):
    jobs = sorted(zip(end_time, start_time, profit))
    ends = [0]
    dp = [0]
    for end, start, gain in jobs:
        best = dp[bisect_right(ends, start) - 1] + gain
        if best > dp[-1]:
            ends.append(end)
            dp.append(best)
    return dp[-1]
```
</details>
