# Find the Number of Good Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3162 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-good-pairs-i](https://leetcode.com/problems/find-the-number-of-good-pairs-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-good-pairs-i/).

### Goal
Given two integer arrays `nums1` and `nums2` and an integer `k`, identify the total count of "good" index pairs `(i, j)`. A pair is considered good if the element at `nums1[i]` is perfectly divisible by the product of `nums2[j]` and `k` (i.e., `nums1[i] % (nums2[j] * k) == 0`).

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.
- `k`: A positive integer multiplier.

**Return value**

- An integer representing the total count of pairs `(i, j)` that satisfy the divisibility condition.

### Examples
**Example 1**

- Input: `nums1 = [1, 3, 4], nums2 = [1, 3, 4], k = 3`
- Output: `1`
- Explanation: Only the pair (1, 0) is good because 3 % (1 * 3) == 0.

**Example 2**

- Input: `nums1 = [1, 2, 4, 12], nums2 = [2, 4], k = 3`
- Output: `2`
- Explanation: Pairs (3, 0) and (3, 1) are good because 12 % (2 * 3) == 0 and 12 % (4 * 3) == 0.

**Example 3**

- Input: `nums1 = [10], nums2 = [2], k = 1`
- Output: `1`

---

## Solution
### Approach
The problem can be solved using a brute-force approach with nested loops, which is efficient given the constraints of this specific version (I). For larger constraints, one could optimize by using a frequency map (Hash Table) to count occurrences of `nums2[j] * k` and iterating through `nums1` to check divisors.

### Complexity Analysis
- **Time Complexity**: `O(N * M)`, where `N` is the length of `nums1` and `M` is the length of `nums2`.
- **Space Complexity**: `O(1)`, as we only use a counter variable to track the number of good pairs.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[int], nums2: List[int], k: int) -> int:
    """
    Calculates the number of good pairs (i, j) such that
    nums1[i] is divisible by (nums2[j] * k).
    """
    count = 0
    # Pre-calculate the modified values of nums2 to avoid redundant multiplication
    multipliers = [x * k for x in nums2]

    for val1 in nums1:
        for val2_mod in multipliers:
            if val1 % val2_mod == 0:
                count += 1

    return count
```
</details>
