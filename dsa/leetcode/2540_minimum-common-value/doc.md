# Minimum Common Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2540 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-common-value](https://leetcode.com/problems/minimum-common-value/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-common-value/).

### Goal
Given two arrays of integers sorted in non-decreasing order, identify the smallest integer that appears in both arrays. If no common integer exists, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers sorted in non-decreasing order.
- `nums2`: A list of integers sorted in non-decreasing order.

**Return value**

- An integer representing the smallest common value, or -1 if no intersection is found.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 3], nums2 = [2, 4]`
- Output: `2`

**Example 2**

- Input: `nums1 = [1, 2, 3, 6], nums2 = [2, 3, 4, 5]`
- Output: `2`

**Example 3**

- Input: `nums1 = [1, 2], nums2 = [3, 4]`
- Output: `-1`

---

## Solution
### Approach
The optimal approach utilizes the **Two Pointers** technique. Since both input arrays are already sorted, we can maintain a pointer for each array starting at index 0. By comparing the elements at the current pointers, we can increment the pointer pointing to the smaller value, as the larger value cannot possibly be the common minimum if a match exists further ahead. If the values are equal, we have found the smallest common integer.

### Complexity Analysis
- **Time Complexity**: `O(N + M)`, where `N` and `M` are the lengths of `nums1` and `nums2` respectively. In the worst case, we traverse each array exactly once.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for the two pointers.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    """
    Finds the minimum common value in two sorted arrays using the two-pointer technique.
    """
    i, j = 0, 0
    n, m = len(nums1), len(nums2)

    while i < n and j < m:
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return -1
```
</details>
