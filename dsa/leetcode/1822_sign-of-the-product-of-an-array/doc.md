# Sign of the Product of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1822 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sign-of-the-product-of-an-array](https://leetcode.com/problems/sign-of-the-product-of-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sign-of-the-product-of-an-array/).

### Goal
Determine the sign of the product of all numbers in the array without needing to compute the product itself.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return `1` for a positive product, `-1` for a negative product, and `0` if the product is zero.

### Examples
**Example 1**

- Input: `nums = [-1,-2,-3,-4,3,2,1]`
- Output: `1`

**Example 2**

- Input: `nums = [1,5,0,2,-3]`
- Output: `0`

**Example 3**

- Input: `nums = [-1,1,-1,1,-1]`
- Output: `-1`

---

## Solution
### Approach
If any value is zero, the product sign is zero. Otherwise count negative values; an even count gives a positive product and an odd count gives a negative product.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
