## Description

You are given an integer array `nums`.

- The **low** score of `nums` is the **minimum** absolute difference between any two integers.

- The **high** score of `nums` is the **maximum** absolute difference between any two integers.

- The **score** of `nums` is the sum of the **high** and **low** scores.

Return the **minimum score** after **changing two elements** of `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,4,7,8,5]

**Output:** 3

**Explanation:**

- Change $\text{nums}[0]$ and $\text{nums}[1]$ to be 6 so that `nums` becomes [6,6,7,8,5].

- The low score is the minimum absolute difference: |6 - 6| = 0.

- The high score is the maximum absolute difference: |8 - 5| = 3.

- The sum of high and low score is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,4,3]

**Output:** 0

**Explanation:**

- Change $\text{nums}[1]$ and $\text{nums}[2]$ to 1 so that `nums` becomes [1,1,1].

- The sum of maximum absolute difference and minimum absolute difference is 0.

</div>
### Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$