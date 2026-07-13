# Find the Integer Added to Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3132 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-integer-added-to-array-ii](https://leetcode.com/problems/find-the-integer-added-to-array-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-integer-added-to-array-ii/).

### Goal
Given two integer arrays `nums1` and `nums2`, determine the smallest integer `x` such that `nums2` can be formed by taking `nums1`, adding `x` to every element, and then removing exactly two elements from the resulting array.

### Function Contract
**Inputs**

- `nums1`: A list of integers (length `n`).
- `nums2`: A list of integers (length `n - 2`).

**Return value**

- An integer representing the smallest possible value of `x` that satisfies the condition.

### Examples
**Example 1**

- Input: `nums1 = [4,20,16,12,8]`, `nums2 = [14,18,10]`
- Output: `-2`
- Explanation: After adding -2 to `nums1`, we get `[2, 18, 14, 10, 6]`. Removing 2 and 6 leaves `[18, 14, 10]`, which matches `nums2`.

**Example 2**

- Input: `nums1 = [3,5,5,3]`, `nums2 = [7,7]`
- Output: `2`
- Explanation: After adding 2 to `nums1`, we get `[5, 7, 7, 5]`. Removing 5 and 5 leaves `[7, 7]`, which matches `nums2`.

**Example 3**

- Input: `nums1 = [1,1,1,1]`, `nums2 = [1,1]`
- Output: `0`

---

## Solution
### Approach
The problem is solved by sorting both arrays. Since we must remove exactly two elements from `nums1`, the potential difference `x` must be one of the values derived from `nums2[0] - nums1[i]` for `i` in `[0, 1, 2]`. We iterate through these three possible candidates for `x` and verify if the remaining elements of `nums1` (after adding `x`) can form `nums2` using a two-pointer approach.

### Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting, where `n` is the length of `nums1`. The verification step takes `O(n)` and is performed a constant number of times.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int]) -> int:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    n = len(nums1)
    m = len(nums2)

    def check(diff: int) -> bool:
        # Try to match nums2 using two pointers on nums1
        # We are allowed to skip exactly 2 elements in nums1
        p1 = 0
        p2 = 0
        skips = 0
        while p1 < n and p2 < m:
            if nums1[p1] + diff == nums2[p2]:
                p1 += 1
                p2 += 1
            else:
                skips += 1
                p1 += 1
                if skips > 2:
                    return False
        return p2 == m

    # The possible difference must be formed by nums2[0] - nums1[i]
    # where i is one of the first 3 elements (because we only remove 2)
    candidates = set()
    for i in range(3):
        candidates.add(nums2[0] - nums1[i])

    # Sort candidates to find the smallest valid one
    for diff in sorted(list(candidates)):
        if check(diff):
            return diff

    return 0
```
</details>
