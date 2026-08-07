## Description

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.
### Function Contract

**Inputs**

- `nums`: An array of distinct integers.

**Return value**

Return the complete power set of `nums`, including the empty subset and `nums` itself, without duplicates.

### Examples
#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`
#### Example 2

- **Input:** `nums = [0]`
- **Output:** `[[],[0]]`
### Constraints

- $1 \le \text{nums.length} \le 10$

- $-10 \le \text{nums}[i] \le 10$

- All the numbers of `nums` are **unique**.