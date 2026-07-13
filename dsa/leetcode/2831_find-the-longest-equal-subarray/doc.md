# Find the Longest Equal Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2831 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-longest-equal-subarray](https://leetcode.com/problems/find-the-longest-equal-subarray/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-longest-equal-subarray/).

### Goal
Given an array of integers and an integer `k`, determine the length of the longest subarray that can be formed by deleting at most `k` elements such that all remaining elements in the subarray are equal.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum number of elements that can be removed.

**Return value**

- An integer representing the maximum possible length of an equal-element subarray after at most `k` deletions.

### Examples
**Example 1**

- Input: `nums = [1,3,2,3,1,3], k = 3`
- Output: `3`

**Example 2**

- Input: `nums = [1,1,2,2,1,1], k = 2`
- Output: `4`

**Example 3**

- Input: `nums = [1,2,3,4], k = 0`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Sliding Window** approach combined with a **Hash Map** (or dictionary). We store the indices of each unique number in the array. For each number, we treat its list of indices as a sequence and use a sliding window to find the longest subsequence of indices `[i_start, ..., i_end]` such that the number of elements between them that are *not* equal to the target value (calculated as `(indices[end] - indices[start]) - (end - start)`) is less than or equal to `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We iterate through the array once to group indices and then perform a linear scan over the index lists.
- **Space Complexity**: `O(n)` to store the indices of each element in the hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Group the indices of each number
    pos_map = defaultdict(list)
    for i, num in enumerate(nums):
        pos_map[num].append(i)

    max_len = 0

    # For each number, find the longest window of indices
    # such that the number of gaps between them is <= k
    for val in pos_map:
        indices = pos_map[val]
        left = 0
        for right in range(len(indices)):
            # The number of elements to delete to make the subarray
            # from indices[left] to indices[right] equal is:
            # (total distance between indices) - (number of elements in the window - 1)
            # which simplifies to: (indices[right] - indices[left]) - (right - left)
            while (indices[right] - indices[left]) - (right - left) > k:
                left += 1

            # The length of the equal subarray is the number of elements in the window
            max_len = max(max_len, right - left + 1)

    return max_len
```
</details>
