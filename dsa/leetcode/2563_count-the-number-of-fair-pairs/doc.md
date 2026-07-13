# Count the Number of Fair Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2563 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-fair-pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-fair-pairs/).

### Goal
Given an array of integers and two boundary values, identify the total number of index pairs (i, j) such that i < j and the sum of the elements at these indices falls within the inclusive range [lower, upper].

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `lower`: An integer representing the minimum inclusive sum.
- `upper`: An integer representing the maximum inclusive sum.

**Return value**

- An integer representing the count of pairs (i, j) where i < j and lower <= nums[i] + nums[j] <= upper.

### Examples
**Example 1**

- Input: `nums = [0,1,7,4,4,5], lower = 3, upper = 6`
- Output: `6`

**Example 2**

- Input: `nums = [1,7,9,2,5], lower = 11, upper = 11`
- Output: `1`

**Example 3**

- Input: `nums = [1,2,3], lower = 1, upper = 1`
- Output: `0`

---

## Solution
### Approach
The problem is solved by sorting the array first, which allows us to use the Two Pointers technique. Since the order of elements does not matter for the sum, sorting enables us to efficiently count pairs that satisfy the condition `sum <= target` by using two pointers moving inward. We calculate the count of pairs with sum <= upper and subtract the count of pairs with sum < lower.

### Complexity Analysis
- **Time Complexity**: O(n log n), where n is the length of the array, due to the sorting step. The two-pointer traversal takes O(n).
- **Space Complexity**: O(1) or O(n) depending on the sorting implementation's space requirements (Python's Timsort is O(n)).

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left, bisect_right

def count_pairs_with_sum_less_than(nums, target):
    """
    Helper function to count pairs (i, j) with i < j such that nums[i] + nums[j] < target.
    Uses two pointers on a sorted array.
    """
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            # All elements between left and right form a valid pair with nums[left]
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

def solve(nums: list[int], lower: int, upper: int) -> int:
    """
    Calculates the number of fair pairs by finding pairs with sum <= upper
    and subtracting pairs with sum < lower.
    """
    nums.sort()

    # Pairs with sum <= upper is equivalent to sum < upper + 1
    count_upper = count_pairs_with_sum_less_than(nums, upper + 1)

    # Pairs with sum < lower
    count_lower = count_pairs_with_sum_less_than(nums, lower)

    return count_upper - count_lower
```
</details>
