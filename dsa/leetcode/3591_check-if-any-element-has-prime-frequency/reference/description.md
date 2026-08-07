## Description

You are given an integer array `nums`.

Return `true` if the frequency of any element of the array is **prime**, otherwise, return `false`.

The **frequency** of an element `x` is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,5,4]

**Output:** true

**Explanation:**

4 has a frequency of two, which is a prime number.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4,5]

**Output:** false

**Explanation:**

All elements have a frequency of one.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,2,2,4,4]

**Output:** true

**Explanation:**

Both 2 and 4 have a prime frequency.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 100$