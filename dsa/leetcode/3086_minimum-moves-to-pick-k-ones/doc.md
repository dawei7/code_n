# Minimum Moves to Pick K Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3086 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-moves-to-pick-k-ones](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/).

### Goal
Given a binary array `nums` and integers `k` and `maxChanges`, determine the minimum number of operations required to collect `k` ones. An operation consists of either moving a one to an adjacent index or changing a zero to a one. You are allowed at most `maxChanges` operations to flip zeros to ones. When moving a one, the cost is the absolute difference between the current and target indices.

### Function Contract
**Inputs**

- `nums`: A list of integers containing only 0s and 1s.
- `k`: The total number of ones to collect.
- `maxChanges`: The maximum number of zeros that can be converted into ones.

**Return value**

- An integer representing the minimum total moves required to gather `k` ones.

### Examples
**Example 1**

- Input: `nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1`
- Output: `3`

**Example 2**

- Input: `nums = [0,0,0,0], k = 2, maxChanges = 3`
- Output: `4`

**Example 3**

- Input: `nums = [1,0,0,0,0,1], k = 2, maxChanges = 0`
- Output: `5`

---

## Solution
### Approach
The problem is solved by combining three strategies:
1. **Direct Conversion**: If `maxChanges` is sufficient, we can convert zeros to ones adjacent to existing ones.
2. **Sliding Window**: For existing ones, we use a sliding window of size `k` to find the optimal cluster. The cost to move all ones in a window to the median position is calculated efficiently using prefix sums.
3. **Greedy Selection**: We prioritize using `maxChanges` to flip zeros that are immediately adjacent to the target window, as these cost only 1 move each.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the length of the array. We iterate through the array to collect indices of ones and use prefix sums to calculate window costs in constant time.
- **Space Complexity**: `O(N)` to store the indices of the ones present in the input array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from itertools import accumulate


def solve(nums: list[int], k: int, maxChanges: int) -> int:
    ones = [i for i, value in enumerate(nums) if value == 1]
    if not ones:
        return k * 2

    adjacent_pickups = 0
    n = len(nums)
    for index in ones:
        count = 1
        if index > 0 and nums[index - 1] == 1:
            count += 1
        if index + 1 < n and nums[index + 1] == 1:
            count += 1
        adjacent_pickups = max(adjacent_pickups, count)

    adjacent_pickups = min(adjacent_pickups, k)
    if adjacent_pickups + maxChanges >= k:
        return adjacent_pickups - 1 + (k - adjacent_pickups) * 2

    needed_existing = k - maxChanges
    prefix = list(accumulate(ones, initial=0))
    best = 10**30

    for left in range(len(ones) - needed_existing + 1):
        right = left + needed_existing - 1
        mid = (left + right) // 2
        center = ones[mid]

        left_cost = center * (mid - left + 1) - (prefix[mid + 1] - prefix[left])
        right_cost = (prefix[right + 1] - prefix[mid]) - center * (right - mid + 1)
        best = min(best, left_cost + right_cost)

    return best + maxChanges * 2
```
</details>
