## Description

Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array.

Return *the minimum number of patches required*.
### Function Contract

**Inputs**

- `nums`: A nonempty ascending array of positive integers.
- `n`: The inclusive upper endpoint of the values that must be representable.

**Return value**

Return the minimum number of elements that must be added so every value from `1` through `n` can be formed as a sum of selected array elements.

### Examples

#### Example 1

- **Input:** `nums = [1,3], n = 6`
- **Output:** `1`
- **Explanation:**
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
#### Example 2

- **Input:** `nums = [1,5,10], n = 20`
- **Output:** `2`
- **Explanation:** The two patches can be [2, 4].
#### Example 3

- **Input:** `nums = [1,2,2], n = 5`
- **Output:** `0`
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{4}$

- `nums` is sorted in **ascending order**.

- $1 \le n \le 2^{31} - 1$