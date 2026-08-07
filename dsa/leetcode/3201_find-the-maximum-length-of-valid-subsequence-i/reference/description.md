## Description

You are given an integer array `nums`.
A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

- $(\text{sub}[0] + \text{sub}[1]) \% 2 = (\text{sub}[1] + \text{sub}[2]) \% 2 = ... = (sub[x - 2] + sub[x - 1]) \% 2.$

Return the length of the **longest** **valid** subsequence of `nums`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** 4

**Explanation:**

The longest valid subsequence is `[1, 2, 3, 4]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,1,1,2,1,2]

**Output:** 6

**Explanation:**

The longest valid subsequence is `[1, 2, 1, 2, 1, 2]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,3]

**Output:** 2

**Explanation:**

The longest valid subsequence is `[1, 3]`.

</div>
### Constraints

- $2 \le \text{nums.length} \le 2 * 10^{5}$

- $1 \le \text{nums}[i] \le 10^{7}$