# Maximum Difference Between Adjacent Elements in a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3423 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-difference-between-adjacent-elements-in-a-circular-array](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/).

### Goal
Given an array of integers, calculate the maximum absolute difference between any two adjacent elements. Because the array is circular, the last element is considered adjacent to the first element.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`) where the length is at least 2.

**Return value**

- An integer representing the maximum absolute difference found between any two adjacent elements in the circular arrangement.

### Examples
**Example 1**

- Input: `nums = [1, 2, 4]`
- Output: `3`
- Explanation: The differences are |1-2|=1, |2-4|=2, and |4-1|=3. The maximum is 3.

**Example 2**

- Input: `nums = [1, 3, 9, 1]`
- Output: `8`
- Explanation: The differences are |1-3|=2, |3-9|=6, |9-1|=8, and |1-1|=0. The maximum is 8.

**Example 3**

- Input: `nums = [5, 5]`
- Output: `0`
- Explanation: The differences are |5-5|=0 and |5-5|=0. The maximum is 0.

---

## Solution
### Approach
Linear scan (iteration). We iterate through the array once, calculating the absolute difference between `nums[i]` and `nums[i+1]` for all indices, including the wrap-around case where we compare the last element with the first.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the array, as we perform a single pass over the input.
- **Space Complexity**: `O(1)`, as we only store the running maximum and a few index pointers.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    max_diff = 0

    # Iterate through the array to compare adjacent elements
    for i in range(n):
        # Use modulo operator to handle the circular adjacency (last element to first)
        diff = abs(nums[i] - nums[(i + 1) % n])
        if diff > max_diff:
            max_diff = diff

    return max_diff
```
</details>
