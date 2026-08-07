## Description

Given an integer array `nums` and an integer `k`, return *the* $$k^{\text{th}}$$ *largest element in the array*.

Note that it is the $$k^{\text{th}}$$largest element in the sorted order, not the$$k^{\text{th}}$$ distinct element.

Can you solve it without sorting?
### Function Contract

**Inputs**

- `nums`: The integer array whose elements are ranked with duplicates retained.
- `k`: The one-based rank counted from the largest element.

**Return value**

Return the value at rank `k` in descending sorted order.

### Examples
#### Example 1

- **Input:** `nums = [3,2,1,5,6,4], k = 2`
- **Output:** `5`
#### Example 2

- **Input:** `nums = [3,2,3,1,2,4,5,5,6], k = 4`
- **Output:** `4`
### Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$