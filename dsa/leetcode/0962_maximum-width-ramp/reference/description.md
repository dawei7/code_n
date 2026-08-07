## Description

A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and $\text{nums}[i] \le \text{nums}[j]$. The **width** of such a ramp is $j - i$.

Given an integer array `nums`, return *the maximum width of a **ramp** in *`nums`. If there is no **ramp** in `nums`, return `0`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [6,0,8,2,1,5]`
- **Output:** `4`
- **Explanation:** The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
#### Example 2

- **Input:** `nums = [9,8,1,0,1,9,4,0,4,1]`
- **Output:** `7`
- **Explanation:** The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
### Constraints

- $2 \le \text{nums.length} \le 5 * 10^{4}$

- $0 \le \text{nums}[i] \le 5 * 10^{4}$