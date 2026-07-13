# Minimum Average of Smallest and Largest Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3194 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-average-of-smallest-and-largest-elements](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/).

### Goal
Given an array of integers, repeatedly remove the current smallest and largest elements from the collection. Calculate the average of these two values for each pair removed. The objective is to return the minimum average value obtained across all such pairs.

### Function Contract
**Inputs**

- `nums`: A list of integers where the length is always even.

**Return value**

- A float representing the minimum average found among all pairs.

### Examples
**Example 1**

- Input: `nums = [7, 8, 3, 4, 15, 13, 4, 1]`
- Output: `5.5`

**Example 2**

- Input: `nums = [1, 9, 8, 3, 10, 5]`
- Output: `5.5`

**Example 3**

- Input: `nums = [1, 2, 3, 7, 8, 9]`
- Output: `5.0`

---

## Solution
### Approach
The problem is solved using a **Sorting and Two-Pointer** approach. By sorting the array, the smallest and largest elements are guaranteed to be at the current boundaries (left and right pointers). We iteratively compute the average of the elements at these pointers, move the pointers inward, and track the minimum average encountered.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the sorting step, where `n` is the number of elements in the array. The subsequent two-pointer traversal takes `O(n)`.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(n)`).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> float:
    """
    Calculates the minimum average of the smallest and largest elements
    by sorting the array and using two pointers.
    """
    nums = sorted(nums)
    n = len(nums)
    min_avg = float('inf')

    left = 0
    right = n - 1

    while left < right:
        current_avg = (nums[left] + nums[right]) / 2
        if current_avg < min_avg:
            min_avg = current_avg
        left += 1
        right -= 1

    return float(min_avg)
```
</details>
