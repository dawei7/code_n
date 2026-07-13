# Find the Number of Subarrays Where Boundary Elements Are Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3113 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-subarrays-where-boundary-elements-are-maximum](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/).

### Goal
Given an array of integers, identify the total count of contiguous subarrays where both the first and last elements are equal to the maximum value present within that specific subarray.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the total count of valid subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 3, 2]`
- Output: `6`
- Explanation: The valid subarrays are [1], [4], [3], [3], [2], and [3, 3].

**Example 2**

- Input: `nums = [3, 3, 3]`
- Output: `6`
- Explanation: All subarrays [3], [3], [3], [3, 3], [3, 3], and [3, 3, 3] are valid.

**Example 3**

- Input: `nums = [1]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Monotonic Decreasing Stack**. By maintaining a stack of pairs `(value, count)`, we can track the occurrences of the current maximum value. As we iterate through the array, if we encounter a value smaller than the stack top, it cannot be the maximum for any subarray extending past it. If we encounter a value equal to the stack top, we increment the count of that value. If we encounter a larger value, we pop smaller elements from the stack because they can no longer be the maximum for any subarray including the new, larger element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array. Each element is pushed onto and popped from the stack at most once.
- **Space Complexity**: `O(n)` in the worst case (e.g., a strictly decreasing array) to store the stack elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of subarrays where the first and last elements
    are the maximum of that subarray using a monotonic stack.
    """
    # stack stores tuples of (value, count_of_this_value_in_current_sequence)
    stack = []
    total_subarrays = 0

    for x in nums:
        # Maintain a monotonic decreasing stack.
        # If we see a value larger than the top, the previous smaller values
        # can no longer be the maximum for any subarray extending to the current index.
        while stack and stack[-1][0] < x:
            stack.pop()

        if stack and stack[-1][0] == x:
            # If the current value is the same as the top, it extends all
            # previous subarrays that had this value as the maximum.
            count = stack[-1][1] + 1
            stack.pop()
            stack.append((x, count))
            total_subarrays += count
        else:
            # If the current value is smaller than the top (or stack is empty),
            # it starts a new potential maximum sequence of length 1.
            stack.append((x, 1))
            total_subarrays += 1

    return total_subarrays
```
</details>
