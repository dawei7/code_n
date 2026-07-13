# Minimum Total Cost to Make Arrays Unequal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2499 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-total-cost-to-make-arrays-unequal](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/).

### Goal
Given two integer arrays of equal length, calculate the minimum cost to swap elements within the first array such that for all indices `i`, `nums1[i]` is not equal to `nums2[i]`. A swap between index `i` and `j` incurs a cost of `i + j`. If it is impossible to satisfy the condition, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the first array.
- `nums2`: A list of integers representing the second array.

**Return value**

- An integer representing the minimum total cost to satisfy the condition, or -1 if no such configuration exists.

### Examples
**Example 1**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 3, 4, 5]`
- Output: `10`

**Example 2**

- Input: `nums1 = [2, 2, 2, 2], nums2 = [1, 3, 4, 5]`
- Output: `0`

**Example 3**

- Input: `nums1 = [1, 2, 2, 2], nums2 = [1, 2, 2, 2]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a **Greedy approach with Frequency Counting**. First, identify all indices `i` where `nums1[i] == nums2[i]`. These indices must be resolved. We prioritize swapping these indices with other indices `j` where `nums1[j] != nums2[j]` and `nums1[j] != nums1[i]` and `nums2[j] != nums1[i]`. If we still have unresolved indices, we must swap them with each other. The constraint is that the most frequent element among the problematic indices cannot exceed half the total number of problematic indices.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the arrays, as we iterate through the arrays a constant number of times to count frequencies and calculate costs.
- **Space Complexity**: `O(n)` to store the frequency map of the problematic indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    bad_indices = []
    total_cost = 0

    # Identify indices where nums1[i] == nums2[i]
    for i in range(n):
        if nums1[i] == nums2[i]:
            bad_indices.append(i)
            total_cost += i

    if not bad_indices:
        return 0

    # Count frequencies of values at bad indices
    counts = Counter()
    for i in bad_indices:
        counts[nums1[i]] += 1

    # Find the most frequent element among bad indices
    max_freq_val, max_freq = counts.most_common(1)[0]

    # Number of swaps needed
    m = len(bad_indices)

    # Try to resolve conflicts by swapping with non-bad indices
    # A non-bad index j can be used if nums1[j] != max_freq_val and nums2[j] != max_freq_val
    needed = max_freq - (m - max_freq)

    for i in range(n):
        if needed <= 0:
            break
        if nums1[i] != nums2[i] and nums1[i] != max_freq_val and nums2[i] != max_freq_val:
            total_cost += i
            needed -= 1

    # If we still have conflicts, we must swap bad indices with each other
    if needed > 0:
        # Check if it's even possible to resolve
        # We need enough total bad indices to accommodate the most frequent one
        # The total number of bad indices is m. We need m >= 2 * max_freq
        if m < 2 * max_freq:
            return -1

        # Add the cost of swapping remaining bad indices
        # Each remaining swap costs the index value
        for i in range(m):
            if needed <= 0:
                break
            total_cost += bad_indices[i]
            needed -= 1

    return total_cost if needed <= 0 else -1
```
</details>
