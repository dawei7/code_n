## Description

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.
### Function Contract

**Inputs**

- `nums`: A non-empty integer array.

**Return value**

Return the maximum product among all non-empty contiguous subarrays of `nums`.

### Examples

#### Example 1

- **Input:** `nums = [2,3,-2,4]`
- **Output:** `6`
- **Explanation:** [2,3] has the largest product 6.
#### Example 2

- **Input:** `nums = [-2,0,-1]`
- **Output:** `0`
- **Explanation:** The result cannot be 2, because [-2,-1] is not a subarray.
### Constraints

- $1 \le \text{nums.length} \le 2 * 10^{4}$

- $-10 \le \text{nums}[i] \le 10$

- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.