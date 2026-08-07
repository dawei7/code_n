## Description

You are given an integer array `nums`.

Return the **smallest absent positive** integer in `nums` such that it is **strictly greater** than the **average** of all elements in `nums`.

The **average** of an array is defined as the sum of all its elements divided by the number of elements.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [3,5]

**Output:** 6

**Explanation:**

- The average of `nums` is $(3 + 5) / 2 = 8 / 2 = 4$.

- The smallest absent positive integer greater than 4 is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,1,2]

**Output:** 3

**Explanation:**

- ​​​​​​​The average of `nums` is $(-1 + 1 + 2) / 3 = 2 / 3 = 0.667$.

- The smallest absent positive integer greater than 0.667 is 3.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4,-1]

**Output:** 2

**Explanation:**

- The average of `nums` is $(4 + (-1)) / 2 = 3 / 2 = 1.50$.

- The smallest absent positive integer greater than 1.50 is 2.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$​​​​​​​