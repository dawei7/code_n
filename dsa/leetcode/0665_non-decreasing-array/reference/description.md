## Description

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if $\text{nums}[i] \le nums[i + 1]$ holds for every `i` (**0-based**) such that ($0 \le i \le n - 2$).
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [4,2,3]`
- **Output:** `true`
- **Explanation:** You could modify the first 4 to 1 to get a non-decreasing array.
#### Example 2

- **Input:** `nums = [4,2,1]`
- **Output:** `false`
- **Explanation:** You cannot get a non-decreasing array by modifying at most one element.
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{4}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$