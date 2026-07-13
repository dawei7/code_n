# Shortest Subarray With OR at Least K II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3097 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-subarray-with-or-at-least-k-ii](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/).

### Goal
Given an array of non-negative integers and an integer `k`, find the length of the shortest non-empty subarray such that the bitwise OR of all elements in that subarray is at least `k`. If no such subarray exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: A non-negative integer representing the target threshold.

**Return value**

- An integer representing the minimum length of a subarray whose bitwise OR is $\ge k$, or -1 if no such subarray exists.

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
The problem is solved using a **Sliding Window** approach combined with **Bit Frequency Counting**. Since the bitwise OR operation is monotonic (adding an element never decreases the OR sum), we can maintain a window `[left, right]` and track the count of set bits at each of the 30 possible positions (since integers are up to $10^9$). When the current OR sum is $\ge k$, we shrink the window from the left to find the minimal length.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot \log(\max(nums)))$, where $n$ is the length of the array. For each element, we perform constant-time bitwise operations (30 bits).
- **Space Complexity**: $O(1)$, as we only store a fixed-size array of size 30 to track bit counts, regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    if k == 0:
        return 1

    n = len(nums)
    min_len = float('inf')
    bit_counts = [0] * 32
    current_or = 0
    left = 0

    def update_or(val, delta):
        nonlocal current_or
        for i in range(32):
            if (val >> i) & 1:
                bit_counts[i] += delta

        new_or = 0
        for i in range(32):
            if bit_counts[i] > 0:
                new_or |= (1 << i)
        return new_or

    for right in range(n):
        current_or = update_or(nums[right], 1)

        while current_or >= k:
            min_len = min(min_len, right - left + 1)
            current_or = update_or(nums[left], -1)
            left += 1

    return int(min_len) if min_len != float('inf') else -1
```
</details>
