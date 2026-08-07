## Description

You are given an integer array `nums`.

A **subsequence** is **stable** if it does not contain **three consecutive** elements with the **same** parity when the subsequence is read **in order** (i.e., consecutive **inside the subsequence**).

Return the number of stable subsequences.

Since the answer may be too large, return it **modulo** $10^{9} + 7$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,5]

**Output:** 6

**Explanation:**

- Stable subsequences are `[1]`, `[3]`, `[5]`, `[1, 3]`, `[1, 5]`, and `[3, 5]`.

- Subsequence `[1, 3, 5]` is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,4,2]

**Output:** 14

**Explanation:**

- The only subsequence that is not stable is `[2, 4, 2]`, which contains three consecutive even numbers.

- All other subsequences are stable. Thus, the answer is 14.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^​​​​​​​5$