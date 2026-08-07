## Description

You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [10,12,13,14]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [999,19,199]

**Output:** 10

**Explanation:**

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10^{4}$