# Form Smallest Number From Two Digit Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2605 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [form-smallest-number-from-two-digit-arrays](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/).

### Goal
Given two arrays of single-digit integers, determine the smallest possible number that can be formed by concatenating one digit from each array. If the arrays share common digits, the smallest common digit is the answer. Otherwise, the smallest number is formed by taking the minimum digit from each array and placing the smaller digit in the tens place and the larger in the units place.

### Function Contract
**Inputs**

- `nums1`: A list of integers where each element is between 1 and 9.
- `nums2`: A list of integers where each element is between 1 and 9.

**Return value**

- An integer representing the smallest possible number formed by combining digits from both arrays.

### Examples
**Example 1**

- Input: `nums1 = [4, 1, 3], nums2 = [5, 7]`
- Output: `15`

**Example 2**

- Input: `nums1 = [3, 5, 2, 6], nums2 = [3, 1, 7, 5]`
- Output: `3`

**Example 3**

- Input: `nums1 = [6, 4, 3, 2], nums2 = [1, 5, 8]`
- Output: `12`

---

## Solution
### Approach
The problem is solved using Set Intersection and Greedy Selection. By converting the arrays into sets, we can identify common elements in $O(N+M)$ time. If the intersection is non-empty, the minimum value in the intersection is the result. If empty, we select the minimum digit from each set and construct the smallest two-digit number by sorting them.

### Complexity Analysis
- **Time Complexity**: $O(N + M)$, where $N$ and $M$ are the lengths of `nums1` and `nums2` respectively, due to set construction and iteration.
- **Space Complexity**: $O(1)$, as the sets contain at most 9 unique digits (constant space).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int]) -> int:
    set1 = set(nums1)
    set2 = set(nums2)

    # Check for common digits
    common = set1.intersection(set2)
    if common:
        return min(common)

    # If no common digits, pick the smallest from each
    min1 = min(set1)
    min2 = min(set2)

    # Form the smallest two-digit number
    if min1 < min2:
        return min1 * 10 + min2
    else:
        return min2 * 10 + min1
```
</details>
