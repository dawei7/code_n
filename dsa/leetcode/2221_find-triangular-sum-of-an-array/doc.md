# Find Triangular Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2221 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation, Combinatorics, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/find-triangular-sum-of-an-array/) |

## Problem Description

### Goal

Begin with a 0-indexed list of decimal digits. If it contains more than one element, create a list one position shorter whose value at index $i$ is `(nums[i] + nums[i + 1]) % 10`.

Replace the current list with this adjacent-sum list and repeat until exactly one digit remains. Return that final digit, called the triangular sum of the original array.

### Function Contract

**Inputs**

- `nums`: A nonempty list whose elements are integers from `0` through `9`.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the sole digit remaining after repeatedly applying the adjacent-sum transformation modulo 10.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5]`
- **Output:** `8`

#### Example 2

- **Input:** `nums = [5]`
- **Output:** `5`

#### Example 3

- **Input:** `nums = [9, 9]`
- **Output:** `8`
