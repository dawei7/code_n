# Find Indices With Index and Value Difference I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2903 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-indices-with-index-and-value-difference-i](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/).

### Goal
Given an array of integers, determine if there exists a pair of indices `(i, j)` such that the absolute difference between the indices is at least `indexDifference` and the absolute difference between the values at those indices is at least `valueDifference`. If such a pair exists, return the indices; otherwise, return `[-1, -1]`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `indexDifference`: An integer representing the minimum required distance between indices.
- `valueDifference`: An integer representing the minimum required absolute difference between values.

**Return value**

- A list of two integers `[i, j]` satisfying the conditions, or `[-1, -1]` if no such pair exists.

### Examples
**Example 1**

- Input: `nums = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4`
- Output: `[0, 3]`

**Example 2**

- Input: `nums = [2, 1], indexDifference = 0, valueDifference = 0`
- Output: `[0, 0]`

**Example 3**

- Input: `nums = [1, 2, 3], indexDifference = 2, valueDifference = 4`
- Output: `[-1, -1]`

---

## Solution
### Approach
The problem can be solved using a brute-force approach with nested loops. Since the constraints for this specific version (Part I) are small (typically $n \le 100$), an $O(n^2)$ approach is sufficient. We iterate through all possible pairs `(i, j)` and check if `abs(i - j) >= indexDifference` and `abs(nums[i] - nums[j]) >= valueDifference`.

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the length of the input array, as we check all pairs.
- **Space Complexity**: $O(1)$, as we only use a constant amount of extra space.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                return [i, j]
    return [-1, -1]
```
</details>
