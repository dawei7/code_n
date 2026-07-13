# Maximize the Minimum Powered City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2528 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-the-minimum-powered-city](https://leetcode.com/problems/maximize-the-minimum-powered-city/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-the-minimum-powered-city/).

### Goal
Given an array representing the power stations in a city and a range `r`, each station provides power to all cities within distance `r`. The total power of a city is the sum of power from all stations within its range. You are allowed to add at most `k` new power stations anywhere in the city. The objective is to maximize the minimum power value across all cities after optimally placing the `k` stations.

### Function Contract
**Inputs**

- `stations`: A list of integers where `stations[i]` is the number of power stations at index `i`.
- `r`: An integer representing the range of each power station.
- `k`: An integer representing the maximum number of additional power stations you can add.

**Return value**

- An integer representing the maximum possible value of the minimum power among all cities.

### Examples
**Example 1**

- Input: `stations = [1,2,4,5,0], r = 1, k = 2`
- Output: `5`

**Example 2**

- Input: `stations = [4,4,4,4], r = 0, k = 3`
- Output: `4`

**Example 3**

- Input: `stations = [1,1,1,1], r = 1, k = 1`
- Output: `2`

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer** combined with a **Greedy approach** and a **Sliding Window/Difference Array** technique. Since the minimum power is monotonic (if a value `x` is achievable, any value less than `x` is also achievable), we binary search for the maximum possible minimum power. For a fixed target power, we use a greedy strategy to add stations at the rightmost possible position to cover the leftmost city that currently falls below the target.

### Complexity Analysis
- **Time Complexity**: `O(n log(max_power + k))`, where `n` is the number of cities. The binary search runs in logarithmic time relative to the potential power range, and the check function runs in `O(n)` using a sliding window or difference array.
- **Space Complexity**: `O(n)` to store the current power levels of the cities.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(stations: list[int], r: int, k: int) -> int:
    n = len(stations)

    # Initial power calculation using sliding window
    power = [0] * n
    current_sum = sum(stations[:r + 1])
    for i in range(n):
        power[i] = current_sum
        if i + r + 1 < n:
            current_sum += stations[i + r + 1]
        if i - r >= 0:
            current_sum -= stations[i - r]

    def check(target: int) -> bool:
        added_stations = 0
        diff = [0] * (n + 1)
        current_added = 0

        # We need to track the effect of added stations on the power array
        # We use a difference array to keep track of added power efficiently
        added_power = [0] * (n + 1)
        curr_added_val = 0

        for i in range(n):
            curr_added_val += added_power[i]
            actual_power = power[i] + curr_added_val

            if actual_power < target:
                needed = target - actual_power
                added_stations += needed
                if added_stations > k:
                    return False

                # Add stations at the rightmost possible position: i + r
                # This covers cities from i to i + 2*r
                pos = min(n - 1, i + r)
                curr_added_val += needed
                if pos + r + 1 < n:
                    added_power[pos + r + 1] -= needed
        return True

    low = min(power)
    high = min(power) + k
    ans = low

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
```
</details>
