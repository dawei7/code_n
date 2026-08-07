## Description

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.
### Function Contract

**Inputs**

- `nums`: The non-empty integer array whose distinct values are to be ranked.

**Return value**

Return the third-largest distinct value when it exists; otherwise, return the largest value.

### Examples

#### Example 1

- **Input:** `nums = [3,2,1]`
- **Output:** `1`
- **Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
#### Example 2

- **Input:** `nums = [1,2]`
- **Output:** `2`
- **Explanation:**
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
#### Example 3

- **Input:** `nums = [2,2,3,1]`
- **Output:** `1`
- **Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

**Follow up:** Can you find an `O(n)` solution?