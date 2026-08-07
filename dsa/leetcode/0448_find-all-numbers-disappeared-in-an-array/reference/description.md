## Description

Given an array `nums` of `n` integers where $\text{nums}[i]$ is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.
### Function Contract

**Inputs**

- `nums`: An integer array of length $n$ whose values all lie in $[1, n]$.

**Return value**

- Return an array containing every value in $[1, n]$ that is absent from `nums`.

### Examples
#### Example 1

- **Input:** `nums = [4,3,2,7,8,2,3,1]`
- **Output:** `[5,6]`
#### Example 2

- **Input:** `nums = [1,1]`
- **Output:** `[2]`
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le n$

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.