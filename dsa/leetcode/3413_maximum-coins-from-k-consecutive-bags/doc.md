# Maximum Coins From K Consecutive Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3413 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-coins-from-k-consecutive-bags](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/).

### Goal
Given a set of non-overlapping intervals representing bags of coins, determine the maximum number of coins you can collect by choosing a contiguous range of length `k`. The range can partially overlap with the bags, in which case you collect a proportional amount of coins from that bag.

### Function Contract
**Inputs**

- `coins`: A list of lists where each element `[start, end, coins]` represents a bag covering the range `[start, end]` containing `coins` total.
- `k`: An integer representing the length of the window you can place on the number line.

**Return value**

- An integer representing the maximum possible coins collected.

### Examples
**Example 1**

- Input: `coins = [[8,10,1],[1,3,2],[5,6,4]], k = 2`
- Output: `6`

**Example 2**

- Input: `coins = [[1,10,3]], k = 2`
- Output: `1`

**Example 3**

- Input: `coins = [[1,10,3]], k = 12`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a combination of **Sorting**, **Prefix Sums**, and the **Sliding Window** technique. First, we sort the bags by their start positions. We then compute prefix sums of the coins to allow $O(1)$ range queries. For each bag, we consider two scenarios: the window ends at the bag's end or starts at the bag's start. We use binary search (`bisect_right`) to efficiently find the range of bags fully contained within the window of length `k` and handle the partial overlaps at the boundaries.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the number of bags. Sorting takes $O(n \log n)$, and iterating through the bags with binary search takes $O(n \log n)$.
- **Space Complexity**: $O(n)$ to store the prefix sums and the sorted list of bags.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_right


def solve(coins: list[list[int]], k: int) -> int:
    def best_starting_at_left(intervals: list[list[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        starts = [left for left, _, _ in intervals]
        prefix = [0] * (n + 1)
        for index, (left, right, value) in enumerate(intervals):
            prefix[index + 1] = prefix[index] + (right - left + 1) * value

        answer = 0
        for index in range(n):
            window_right = intervals[index][0] + k - 1
            last = bisect_right(starts, window_right) - 1
            if last < index:
                continue

            current = prefix[last] - prefix[index]
            left, right, value = intervals[last]
            overlap = min(right, window_right) - left + 1
            if overlap > 0:
                current += overlap * value
            answer = max(answer, current)

        return answer

    reflected = [[-right, -left, value] for left, right, value in coins]
    return max(best_starting_at_left([coin[:] for coin in coins]), best_starting_at_left(reflected))
```
</details>
