# Minimum Time to Repair Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2594 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-repair-cars](https://leetcode.com/problems/minimum-time-to-repair-cars/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-repair-cars/).

### Goal
Given an array of integers representing the rank of each mechanic and the total number of cars to be repaired, determine the minimum time required to complete all repairs. Each mechanic with rank `r` can repair `n` cars in `r * n^2` time. Mechanics work simultaneously.

### Function Contract
**Inputs**

- `ranks`: A list of integers where `ranks[i]` is the rank of the i-th mechanic.
- `cars`: An integer representing the total number of cars that need to be repaired.

**Return value**

- An integer representing the minimum time required to repair all cars.

### Examples
**Example 1**

- Input: `ranks = [4, 2, 3, 1], cars = 10`
- Output: `16`

**Example 2**

- Input: `ranks = [5, 1, 8], cars = 6`
- Output: `16`

**Example 3**

- Input: `ranks = [1], cars = 1`
- Output: `1`

---

## Solution
### Approach
The problem exhibits a monotonic property: if it is possible to repair all cars within time `T`, it is also possible to repair them in any time `T' > T`. This allows us to use **Binary Search on the Answer**. We define the search space between 1 and the worst-case scenario (the fastest mechanic repairing all cars alone). For a given time `t`, the number of cars a mechanic with rank `r` can repair is `floor(sqrt(t / r))`.

### Complexity Analysis
- **Time Complexity**: `O(N * log(M))`, where `N` is the number of mechanics and `M` is the maximum possible time (rank of the fastest mechanic * cars^2).
- **Space Complexity**: `O(1)`, as we only use a few variables for the binary search bounds.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(ranks: list[int], cars: int) -> int:
    """
    Calculates the minimum time to repair all cars using binary search.
    """
    # The fastest mechanic is the one with the minimum rank.
    # In the worst case, the fastest mechanic repairs all cars.
    min_rank = min(ranks)

    # Binary search range:
    # Lower bound: 1
    # Upper bound: min_rank * cars^2 (time taken if fastest mechanic does all)
    low = 1
    high = min_rank * (cars ** 2)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        # Calculate total cars repaired by all mechanics in 'mid' time
        # A mechanic with rank r repairs n cars in r * n^2 time.
        # r * n^2 <= mid  =>  n^2 <= mid / r  =>  n <= sqrt(mid / r)
        total_repaired = 0
        for r in ranks:
            total_repaired += int(math.isqrt(mid // r))

        if total_repaired >= cars:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```
</details>
