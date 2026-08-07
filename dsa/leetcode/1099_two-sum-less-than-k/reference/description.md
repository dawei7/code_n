## Description

Given an array `nums` of integers and integer `k`, return the maximum `sum` such that there exists `i < j` with $\text{nums}[i] + \text{nums}[j] = sum$ and `sum < k`. If no `i`, `j` exist satisfying this equation, return `-1`.
### Function Contract

**Inputs**

- `nums`: an array of $n$ integers.
- `k`: the exclusive upper bound for a pair sum.

The two chosen values must occupy distinct positions ordered as $i < j$. Equal numeric values may be paired when they occur at two different indices. A sum equal to `k` is not eligible.

**Return value**

Return the maximum $\text{nums}[i] + \text{nums}[j]$ that is strictly less than `k`. Return `-1` if no eligible pair exists.

### Examples

#### Example 1

- **Input:** `nums = [34,23,1,24,75,33,54,8], k = 60`
- **Output:** `58`
- **Explanation:** We can use 34 and 24 to sum 58 which is less than 60.
#### Example 2

- **Input:** `nums = [10,20,30], k = 15`
- **Output:** `-1`
- **Explanation:** In this case it is not possible to get a pair sum less that 15.
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 1000$

- $1 \le k \le 2000$