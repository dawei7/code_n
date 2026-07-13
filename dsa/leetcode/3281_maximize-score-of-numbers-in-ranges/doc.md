# Maximize Score of Numbers in Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3281 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-score-of-numbers-in-ranges](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/).

### Goal
Given a sorted array of intervals `start` and an integer `d`, select one integer $x_i$ from each interval $[start[i], start[i] + d]$ such that the minimum absolute difference between any two selected integers $|x_i - x_j|$ is maximized.

### Function Contract
**Inputs**

- `start`: A list of integers representing the starting points of intervals.
- `d`: An integer representing the length of each interval.

**Return value**

- An integer representing the maximum possible minimum difference between any two chosen numbers.

### Examples
**Example 1**

- Input: `start = [6, 0, 3], d = 2`
- Output: `4`
- Explanation: We can pick 0, 4, and 8. The differences are |4-0|=4, |8-4|=4, |8-0|=8. The minimum is 4.

**Example 2**

- Input: `start = [2, 6, 13, 13], d = 5`
- Output: `5`
- Explanation: We can pick 2, 7, 12, 17. The minimum difference is 5.

**Example 3**

- Input: `start = [1, 10], d = 1`
- Output: `9`
- Explanation: We can pick 1 and 10. The difference is 9.

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the minimum difference is monotonic (if a difference $k$ is achievable, any difference $k' < k$ is also achievable), we can binary search for the largest possible value of $k$. The feasibility check is performed greedily: for a target difference $k$, we pick the smallest possible value for the first interval, then for each subsequent interval, we pick the smallest value that is at least $k$ greater than the previously chosen value.

### Complexity Analysis
- **Time Complexity**: $O(n \log(M))$, where $n$ is the length of the `start` array and $M$ is the range of possible differences (max value of `start` + `d`). Sorting takes $O(n \log n)$, and the binary search performs $O(\log M)$ checks, each taking $O(n)$.
- **Space Complexity**: $O(1)$ (excluding the space required for sorting).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(start: list[int], d: int) -> int:
    start.sort()
    n = len(start)
    if n < 2:
        return 0

    def can_achieve(min_diff: int) -> bool:
        last_val = start[0]
        for i in range(1, n):
            # We need to pick a value x such that:
            # 1. start[i] <= x <= start[i] + d
            # 2. x >= last_val + min_diff
            target = last_val + min_diff

            # The smallest valid x is max(start[i], target)
            current_val = max(start[i], target)

            if current_val > start[i] + d:
                return False
            last_val = current_val
        return True

    low = 0
    high = start[-1] + d - start[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue

        if can_achieve(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
```
</details>
