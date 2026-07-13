# Maximum Sum of Two Non-Overlapping Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1031 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-of-two-non-overlapping-subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/).

### Goal
Given an array and two subarray lengths, choose one subarray of each length with no overlap so their total sum is maximized.

### Function Contract
**Inputs**

- `nums`: List[int]
- `firstLen`: int
- `secondLen`: int

**Return value**

int - maximum combined sum

### Examples
**Example 1**

- Input: `nums = [0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen = 1, secondLen = 2`
- Output: `20`

**Example 2**

- Input: `nums = [3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen = 3, secondLen = 2`
- Output: `29`

**Example 3**

- Input: `nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen = 4, secondLen = 3`
- Output: `31`

---

## Solution
### Approach
Prefix sums plus one-pass best-left-window tracking.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for prefix sums

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1031: Maximum Sum of Two Non-Overlapping Subarrays."""


def solve(nums: list[int], first_len: int, second_len: int) -> int:
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    def window_sum(left: int, length: int) -> int:
        return prefix[left + length] - prefix[left]

    def best_order(left_len: int, right_len: int) -> int:
        best_left = window_sum(0, left_len)
        answer = 0
        for right_start in range(left_len, len(nums) - right_len + 1):
            best_left = max(best_left, window_sum(right_start - left_len, left_len))
            answer = max(answer, best_left + window_sum(right_start, right_len))
        return answer

    return max(best_order(first_len, second_len), best_order(second_len, first_len))
```
</details>
