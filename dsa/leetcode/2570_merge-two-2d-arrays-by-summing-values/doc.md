# Merge Two 2D Arrays by Summing Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2570 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [merge-two-2d-arrays-by-summing-values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/).

### Goal
Given two 2D arrays representing sparse vectors where each element is a pair `[id, value]`, merge them into a single 2D array. If an `id` appears in both input arrays, sum their corresponding values. The resulting array must be sorted by `id` in ascending order.

### Function Contract
**Inputs**

- `nums1`: A list of lists, where each inner list contains two integers `[id, val]`.
- `nums2`: A list of lists, where each inner list contains two integers `[id, val]`.

**Return value**

- A list of lists representing the merged sparse vectors, sorted by `id`.

### Examples
**Example 1**

- Input: `nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]`
- Output: `[[1,6],[2,3],[3,2],[4,6]]`

**Example 2**

- Input: `nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]`
- Output: `[[1,3],[2,4],[3,6],[4,3],[5,5]]`

**Example 3**

- Input: `nums1 = [[1,1]], nums2 = [[1,2]]`
- Output: `[[1,3]]`

---

## Solution
### Approach
The problem can be solved efficiently using the **Two Pointers** technique. Since the input arrays are already sorted by `id`, we can traverse both arrays simultaneously, comparing the current `id`s and appending the smaller one (or summing if they match) to the result list. Alternatively, a **Hash Map** (or `collections.defaultdict`) can be used to aggregate values by `id` and then sort the keys.

### Complexity Analysis
- **Time Complexity**: `O(N + M)`, where `N` and `M` are the lengths of `nums1` and `nums2` respectively, as we iterate through each array exactly once.
- **Space Complexity**: `O(N + M)` to store the resulting merged array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    """
    Merges two sorted 2D arrays by summing values for matching IDs using the Two Pointers approach.
    """
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        id1, val1 = nums1[i]
        id2, val2 = nums2[j]

        if id1 == id2:
            result.append([id1, val1 + val2])
            i += 1
            j += 1
        elif id1 < id2:
            result.append([id1, val1])
            i += 1
        else:
            result.append([id2, val2])
            j += 1

    # Append remaining elements from either array
    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result
```
</details>
