## Description

Given an array of integers `nums`, you are allowed to perform the following operation any number of times:

- Remove a **strictly increasing** subsequence from the array.

Your task is to find the **minimum** number of operations required to make the array **empty**.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [5,3,1,4,2]

**Output:** 3

**Explanation:**

We remove subsequences `[1, 2]`, `[3, 4]`, `[5]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4,5]

**Output:** 1

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,4,3,2,1]

**Output:** 5

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$