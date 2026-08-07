## Description

Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

A **mode** of a sequence of numbers is defined as the element that appears the **maximum** number of times in the sequence.

A sequence of numbers contains a** unique mode** if it has only one mode.

A sequence of numbers `seq` of size 5 contains a **unique middle mode** if the *middle element* ($\text{seq}[2]$) is a **unique mode**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,1,1,1,1,1]

**Output:** 6

**Explanation:**

`[1, 1, 1, 1, 1]` is the only subsequence of size 5 that can be formed, and it has a unique middle mode of 1. This subsequence can be formed in 6 different ways, so the output is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,2,3,3,4]

**Output:** 4

**Explanation:**

`[1, 2, 2, 3, 4]` and `[1, 2, 3, 3, 4]` each have a unique middle mode because the number at index 2 has the greatest frequency in the subsequence. `[1, 2, 2, 3, 3]` does not have a unique middle mode because 2 and 3 appear twice.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [0,1,2,3,4,5,6,7,8]

**Output:** 0

**Explanation:**

There is no subsequence of length 5 with a unique middle mode.

</div>
### Constraints

- $5 \le \text{nums.length} \le 1000$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$