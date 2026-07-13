# Number of Ways Where Square of Number Is Equal to Product of Two Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1577 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/).

### Goal
Count triplets where the square of one number from one array equals the product
of two numbers from the other array.

### Function Contract
**Inputs**

- `nums1`: the first integer array.
- `nums2`: the second integer array.

**Return value**

The total number of valid triplets across both directions.

### Examples
**Example 1**

- Input: `nums1 = [7, 4], nums2 = [5, 2, 8, 9]`
- Output: `1`

**Example 2**

- Input: `nums1 = [1, 1], nums2 = [1, 1, 1]`
- Output: `9`

**Example 3**

- Input: `nums1 = [7, 7, 8, 3], nums2 = [1, 2, 9, 7]`
- Output: `2`

---

## Solution
### Approach
Count products of all unordered pairs in one array, then for each value in the
other array add the frequency of `value * value`. Do this in both directions:
squares from `nums1` against pair products from `nums2`, and squares from
`nums2` against pair products from `nums1`.

### Complexity Analysis
- **Time Complexity**: `O(n^2 + m^2)`.
- **Space Complexity**: `O(n^2 + m^2)` in the worst case for product counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums1, nums2):
    def pair_products(values):
        products = Counter()
        for i, first in enumerate(values):
            for second in values[i + 1 :]:
                products[first * second] += 1
        return products

    products1 = pair_products(nums1)
    products2 = pair_products(nums2)

    return sum(products2[value * value] for value in nums1) + sum(
        products1[value * value] for value in nums2
    )
```
</details>
