## Description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.
### Function Contract

**Inputs**

- `nums`: The mutable integer array to transform.

**Return value**

Return `None`. After mutation, the nonzero values retain their original relative order and all zeroes occupy the final positions.

### Examples
#### Example 1

- **Input:** `nums = [0,1,0,3,12]`
- **Output:** `[1,3,12,0,0]`
#### Example 2

- **Input:** `nums = [0]`
- **Output:** `[0]`
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

**Follow up:** Could you minimize the total number of operations done?