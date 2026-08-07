## Description

You are given an array of integers `nums` of size 3.

Return the **maximum** possible number whose *binary representation* can be formed by **concatenating** the *binary representation* of **all** elements in `nums` in some order.

**Note** that the binary representation of any number *does not* contain leading zeros.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 30

**Explanation:**

Concatenate the numbers in the order `[3, 1, 2]` to get the result `"11110"`, which is the binary representation of 30.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,8,16]

**Output:** 1296

**Explanation:**

Concatenate the numbers in the order `[2, 8, 16]` to get the result `"10100010000"`, which is the binary representation of 1296.

</div>
### Constraints

- $\text{nums.length} = 3$

- $1 \le \text{nums}[i] \le 127$