# Minimum Number of Seconds to Make Mountain Height Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3296 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-seconds-to-make-mountain-height-zero](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/).

### Goal
Given an initial mountain height and a list of workers with varying efficiency levels, determine the minimum time required to reduce the mountain's height to zero. Each worker $i$ takes $w_i \times k$ seconds to reduce the height by $k$ units, where $k$ is the number of units reduced in a single session. Workers can work simultaneously.

### Function Contract
**Inputs**

- `mountainHeight`: An integer representing the total height to be reduced.
- `workerTimes`: A list of integers where each element represents the base time coefficient for a specific worker.

**Return value**

- An integer representing the minimum total time (in seconds) required to reduce the mountain height to zero.

### Examples
**Example 1**

- Input: `mountainHeight = 4, workerTimes = [2, 1, 4]`
- Output: `3`

**Example 2**

- Input: `mountainHeight = 10, workerTimes = [3, 2, 2, 4]`
- Output: `12`

**Example 3**

- Input: `mountainHeight = 5, workerTimes = [1]`
- Output: `15`

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the time required to reduce the mountain is monotonic (if it can be reduced in $T$ seconds, it can also be reduced in $T+1$ seconds), we search for the smallest $T$ such that the sum of heights reduced by all workers within time $T$ is at least `mountainHeight`. For a given time $T$ and worker coefficient $w$, the number of units $k$ reduced is found by solving $w \cdot \frac{k(k+1)}{2} \le T$.

### Complexity Analysis
- **Time Complexity**: $O(W \log(\text{max\_time}))$, where $W$ is the number of workers and $\text{max\_time}$ is the upper bound of the search space (roughly $10^{18}$).
- **Space Complexity**: $O(1)$, as we only store a few variables for the binary search.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(mountainHeight: int, workerTimes: list[int]) -> int:
    """
    Calculates the minimum time to reduce mountainHeight to zero using binary search.
    For a worker with coefficient w, the time to reduce k units is w * (k * (k + 1) / 2).
    We solve for k: k^2 + k - 2 * (time / w) <= 0.
    Using quadratic formula: k <= (-1 + sqrt(1 + 8 * (time / w))) / 2.
    """

    def get_max_units(time: int, w: int) -> int:
        # Solve w * k * (k + 1) / 2 <= time
        # k^2 + k - 2 * time / w <= 0
        # Positive root of k^2 + k - C = 0 is (-1 + sqrt(1 + 4C)) / 2
        # Here C = 2 * time / w
        val = 2 * time // w
        k = int((math.isqrt(1 + 4 * val) - 1) // 2)
        return k

    def can_reduce(time: int) -> bool:
        total_units = 0
        for w in workerTimes:
            total_units += get_max_units(time, w)
            if total_units >= mountainHeight:
                return True
        return total_units >= mountainHeight

    # Binary search range:
    # Lower bound 0, Upper bound: worst case is one worker with max time
    # reducing all height. Max height 10^5, min worker time 1.
    # Time approx 10^5 * 10^5 * 1 / 2 = 5 * 10^9.
    # Using 10^18 to be safe for constraints.
    low = 0
    high = 10**18
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_reduce(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```
</details>
