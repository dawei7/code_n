## Description

You are given an integer array `nums`.

An array is called **beautiful** if for every index `i > 0`, the value at $\text{nums}[i]$ is **divisible** by $nums[i - 1]$.

In one operation, you may **increment** any element $\text{nums}[i]$ (with `i > 0`) by `1`.

Return the **minimum number of operations** required to make the array beautiful.
### Function Contract

**Inputs**

- `nums`: The positive integer array to make beautiful. Its first element is fixed; every later element may only be increased.

**Return value**

Return the minimum total number of single-unit increments that can make every element after the first divisible by its predecessor.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,7,9]

**Output:** 2

**Explanation:**

Applying the operation twice on $\text{nums}[1]$ makes the array beautiful: `[3,9,9]`

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,1]

**Output:** 0

**Explanation:**

The given array is already beautiful.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [4]

**Output:** 0

**Explanation:**

The array has only one element, so it's already beautiful.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 50​​​$