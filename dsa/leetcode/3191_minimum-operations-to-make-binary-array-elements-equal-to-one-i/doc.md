# Minimum Operations to Make Binary Array Elements Equal to One I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-binary-array-elements-equal-to-one-i](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/).

### Goal
Given a binary array, you are permitted to perform an operation that flips the values of three consecutive elements (0 becomes 1, 1 becomes 0). Determine the minimum number of operations required to transform every element in the array into 1. If it is impossible to achieve this state, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) containing only 0s and 1s.

**Return value**

- An integer representing the minimum number of operations, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [0, 1, 1, 1, 0, 0]`
- Output: `3`

**Example 2**

- Input: `nums = [0, 1, 1, 1]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a **Greedy approach**. Since an operation on index `i` affects `i`, `i+1`, and `i+2`, we iterate through the array from left to right. Whenever we encounter a 0 at index `i`, we must perform an operation starting at `i` to flip it to 1, as no future operations (starting at `i+1` or later) can affect index `i`. If we reach a point where there are fewer than 3 elements remaining and we encounter a 0, it is impossible to complete the task.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single linear scan.
- **Space Complexity**: `O(1)`, as we modify the input array in-place (or use a counter) without requiring additional data structures proportional to the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum operations to make all elements 1 using a greedy approach.
    """
    nums = list(nums)
    n = len(nums)
    operations = 0

    for i in range(n):
        # If we encounter a 0, we must flip the window starting at i
        if nums[i] == 0:
            # Check if there are enough elements left to perform the operation
            if i + 2 >= n:
                return -1

            # Perform the flip for the window [i, i+1, i+2]
            # We only need to flip the current and the next two.
            # Since we only care about the current index being 1,
            # we can just increment the operation count.
            nums[i] = 1 - nums[i]
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            operations += 1

    return operations
```
</details>
