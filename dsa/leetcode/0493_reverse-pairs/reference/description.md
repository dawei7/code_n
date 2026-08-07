## Description

Given an integer array `nums`, return *the number of **reverse pairs** in the array*.

A **reverse pair** is a pair `(i, j)` where:

- $0 \le i < j < \text{nums.length}$ and

- $\text{nums}[i] > 2 * \text{nums}[j]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,3,2,3,1]`
- **Output:** `2`
- **Explanation:** The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
#### Example 2

- **Input:** `nums = [2,4,3,5,1]`
- **Output:** `3`
- **Explanation:** The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
### Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$