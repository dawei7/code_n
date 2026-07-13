# Minimum Absolute Difference Between Elements With Constraint

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2817 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-absolute-difference-between-elements-with-constraint](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/).

### Goal
Given an array of integers and a non-negative integer `x`, find the minimum absolute difference between any two elements `nums[i]` and `nums[j]` such that the absolute difference between their indices `i` and `j` is at least `x`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `x`: An integer representing the minimum required index distance.

**Return value**

- An integer representing the minimum absolute difference found between any two elements satisfying the index constraint.

### Examples
**Example 1**

- Input: `nums = [4,3,2,4], x = 2`
- Output: `0`
- Explanation: We can choose indices 0 and 3. |4 - 4| = 0, and |0 - 3| = 3 >= 2.

**Example 2**

- Input: `nums = [5,3,2,10,15], x = 1`
- Output: `1`
- Explanation: We can choose indices 1 and 2. |3 - 2| = 1, and |1 - 2| = 1 >= 1.

**Example 3**

- Input: `nums = [1,2,3,4], x = 3`
- Output: `3`
- Explanation: We can choose indices 0 and 3. |1 - 4| = 3, and |0 - 3| = 3 >= 3.

---

## Solution
### Approach
The problem is solved using a sliding window approach combined with a balanced binary search tree (or a sorted list). As we iterate through the array with index `i`, we maintain a collection of elements that satisfy the index constraint (i.e., elements at indices `0` to `i - x`). By using `bisect_left` on a sorted list, we can efficiently find the elements closest in value to `nums[i]` to calculate the minimum absolute difference.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the array. We iterate through the array once, and for each element, we perform insertion and binary search in a sorted list, both taking `O(log n)` time.
- **Space Complexity**: `O(n)` to store the elements in the sorted list.

### Reference Implementations
<details>
<summary>python</summary>

```python
import bisect

def solve(nums: list[int], x: int) -> int:
    if x == 0:
        return 0

    n = len(nums)
    sorted_elements = []
    min_diff = float('inf')

    # We iterate through the array. For each index i, we consider
    # elements at index j <= i - x.
    for i in range(x, n):
        # Add the element that just became valid (index i - x)
        val_to_add = nums[i - x]
        idx = bisect.bisect_left(sorted_elements, val_to_add)
        sorted_elements.insert(idx, val_to_add)

        # Find the closest values in the sorted list to nums[i]
        current_val = nums[i]
        pos = bisect.bisect_left(sorted_elements, current_val)

        # Check the element at pos (the smallest element >= current_val)
        if pos < len(sorted_elements):
            min_diff = min(min_diff, abs(sorted_elements[pos] - current_val))

        # Check the element at pos - 1 (the largest element < current_val)
        if pos > 0:
            min_diff = min(min_diff, abs(sorted_elements[pos - 1] - current_val))

        # Optimization: if we found 0, we can't do better
        if min_diff == 0:
            return 0

    return int(min_diff)
```
</details>
