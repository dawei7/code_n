# Maximize Active Section with Trade II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3501 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-active-section-with-trade-ii](https://leetcode.com/problems/maximize-active-section-with-trade-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-active-section-with-trade-ii/).

### Goal
Given an array of integers representing activity levels and a maximum allowed trade-off value, determine the length of the longest contiguous subarray where the difference between the maximum and minimum elements does not exceed the specified trade-off limit.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the activity levels.
- `k`: An integer representing the maximum allowed difference between the maximum and minimum values in the subarray.

**Return value**

- An integer representing the length of the longest valid contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [8, 2, 4, 7], k = 4`
- Output: `2`
- Explanation: The subarray `[8, 4]` is invalid (diff 4), but `[2, 4]` or `[4, 7]` are valid. The longest valid subarray is `[2, 4]` or `[4, 7]` or `[8]` etc. Actually, `[2, 4]` has length 2.

**Example 2**

- Input: `nums = [10, 1, 2, 4, 7, 2], k = 5`
- Output: `4`
- Explanation: The subarray `[1, 2, 4, 2]` has max 4 and min 1, diff 3 <= 5. Length is 4.

**Example 3**

- Input: `nums = [4, 2, 2, 2, 4, 4, 2, 2], k = 0`
- Output: `3`
- Explanation: The subarray `[2, 2, 2]` has max 2 and min 2, diff 0 <= 0. Length is 3.

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Monotonic Deque** (or two deques) to maintain the minimum and maximum values of the current window in $O(1)$ amortized time. Alternatively, a Segment Tree could be used, but the sliding window approach is optimal for contiguous subarrays.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as each element is added and removed from the deques at most once.
- **Space Complexity**: $O(n)$ in the worst case to store the deques.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left, bisect_right


class RangeMax:
    def __init__(self, values: list[int]):
        self.size = 1
        while self.size < len(values):
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for index, value in enumerate(values):
            self.tree[self.size + index] = value
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0
        left += self.size
        right += self.size
        best = 0
        while left <= right:
            if left % 2 == 1:
                best = max(best, self.tree[left])
                left += 1
            if right % 2 == 0:
                best = max(best, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return best


def solve(s: str, queries: list[list[int]]) -> list[int]:
    n = len(s)
    ones_prefix = [0] * (n + 1)
    for index, char in enumerate(s):
        ones_prefix[index + 1] = ones_prefix[index] + (char == "1")

    runs: list[tuple[str, int, int]] = []
    start = 0
    for index in range(1, n + 1):
        if index == n or s[index] != s[start]:
            runs.append((s[start], start, index - 1))
            start = index

    candidates: list[tuple[int, int, int, int, int]] = []
    for run_index in range(1, len(runs) - 1):
        char, left, right = runs[run_index]
        if char == "1" and runs[run_index - 1][0] == "0" and runs[run_index + 1][0] == "0":
            left_zero_start = runs[run_index - 1][1]
            right_zero_end = runs[run_index + 1][2]
            full_gain = (left - left_zero_start) + (right_zero_end - right)
            candidates.append((left, right, left_zero_start, right_zero_end, full_gain))

    starts = [candidate[0] for candidate in candidates]
    ends = [candidate[1] for candidate in candidates]
    tree = RangeMax([candidate[4] for candidate in candidates])

    def actual_gain(index: int, left_bound: int, right_bound: int) -> int:
        left, right, left_zero_start, right_zero_end, _full = candidates[index]
        if left <= left_bound or right >= right_bound:
            return 0
        return (left - max(left_bound, left_zero_start)) + (min(right_bound, right_zero_end) - right)

    answer: list[int] = []
    total_ones = ones_prefix[n]
    for left, right in queries:
        first = bisect_right(starts, left)
        last = bisect_left(ends, right) - 1
        gain = 0
        if first <= last:
            gain = max(gain, actual_gain(first, left, right))
            if first != last:
                gain = max(gain, actual_gain(last, left, right))
                gain = max(gain, tree.query(first + 1, last - 1))
        answer.append(total_ones + gain)
    return answer
```
</details>
