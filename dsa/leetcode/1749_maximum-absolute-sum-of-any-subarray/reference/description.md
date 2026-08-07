## Description

You are given an integer array `nums`. The **absolute sum** of a subarray `[nums_l, nums_l+1, ..., nums_r-1, nums_r]` is $abs(\text{nums}_{l} + \text{nums}_{l}+1 + ... + \text{nums}_{r}-1 + \text{nums}_{r})$.

Return *the **maximum** absolute sum of any **(possibly empty)** subarray of *`nums`.

Note that `abs(x)` is defined as follows:

- If `x` is a negative integer, then $abs(x) = -x$.

- If `x` is a non-negative integer, then $abs(x) = x$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,-3,2,3,-4]`
- **Output:** `5`
- **Explanation:** The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
#### Example 2

- **Input:** `nums = [2,-5,1,-4,3,-2]`
- **Output:** `8`
- **Explanation:** The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$