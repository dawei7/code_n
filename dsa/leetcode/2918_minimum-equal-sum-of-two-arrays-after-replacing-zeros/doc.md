# Minimum Equal Sum of Two Arrays After Replacing Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2918 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-equal-sum-of-two-arrays-after-replacing-zeros](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/).

### Goal
Given two integer arrays containing non-negative integers and zeros, replace every zero with a positive integer (at least 1) such that the sum of elements in both arrays becomes equal. Determine the minimum possible sum that can be achieved. If it is impossible to make the sums equal, return -1.

### Function Contract
**Inputs**

- `nums1`: A list of non-negative integers.
- `nums2`: A list of non-negative integers.

**Return value**

- An integer representing the minimum equal sum, or -1 if no such sum exists.

### Examples
**Example 1**

- Input: `nums1 = [3,2,0,1], nums2 = [2,0,0,0]`
- Output: `7`

**Example 2**

- Input: `nums1 = [2,0,2,0], nums2 = [1,4]`
- Output: `-1`

**Example 3**

- Input: `nums1 = [1,0,0], nums2 = [1]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a Greedy approach. Since each zero must be replaced by at least 1, the minimum sum for an array is its current sum plus the count of zeros. If an array has no zeros, its sum is fixed. By comparing the minimum possible sums and the presence of zeros, we can determine if the arrays can be balanced. If one array has no zeros, its sum must be exactly equal to the other array's potential range. If both have zeros, we can always increase the smaller sum to match the larger one.

### Complexity Analysis
- **Time Complexity**: O(N + M), where N and M are the lengths of `nums1` and `nums2` respectively, as we iterate through each array once to calculate sums and zero counts.
- **Space Complexity**: O(1), as we only use a few variables to store sums and counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int]) -> int:
    sum1 = 0
    zeros1 = 0
    for x in nums1:
        if x == 0:
            zeros1 += 1
        else:
            sum1 += x

    sum2 = 0
    zeros2 = 0
    for x in nums2:
        if x == 0:
            zeros2 += 1
        else:
            sum2 += x

    min_sum1 = sum1 + zeros1
    min_sum2 = sum2 + zeros2

    # If an array has no zeros, its sum is fixed.
    # We can only increase the sum of an array if it contains at least one zero.

    if zeros1 == 0 and zeros2 == 0:
        return sum1 if sum1 == sum2 else -1

    if zeros1 == 0:
        return sum1 if sum1 >= min_sum2 else -1

    if zeros2 == 0:
        return sum2 if sum2 >= min_sum1 else -1

    # If both have zeros, the minimum equal sum is the max of the two minimums.
    return max(min_sum1, min_sum2)
```
</details>
