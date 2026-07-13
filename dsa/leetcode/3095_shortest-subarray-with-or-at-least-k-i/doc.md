# Shortest Subarray With OR at Least K I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3095 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-subarray-with-or-at-least-k-i](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/).

### Goal
Given an array of non-negative integers and an integer `k`, identify the length of the smallest contiguous subarray whose elements, when combined using the bitwise OR operation, result in a value greater than or equal to `k`. If no such subarray exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: A non-negative integer representing the target threshold.

**Return value**

- An integer representing the minimum length of a valid subarray, or -1 if no valid subarray is found.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `1`

**Example 2**

- Input: `nums = [2, 1, 8], k = 10`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2], k = 0`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a Brute Force approach (given the small constraints of this specific version of the problem) or a Sliding Window approach. Since the bitwise OR operation is monotonic (adding elements to a subarray can only increase or keep the OR sum the same), we can iterate through all possible subarrays and track the minimum length that satisfies the condition.

### Complexity Analysis
- **Time Complexity**: `O(n^2)` where `n` is the length of the array, as we check all possible subarrays.
- **Space Complexity**: `O(1)` as we only use a few variables to track the current OR sum and the minimum length.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    min_len = float('inf')

    for i in range(n):
        current_or = 0
        for j in range(i, n):
            current_or |= nums[j]
            if current_or >= k:
                min_len = min(min_len, j - i + 1)
                # Since we want the shortest, once we hit k,
                # we don't need to extend this specific start index further
                break

    return int(min_len) if min_len != float('inf') else -1
```
</details>
