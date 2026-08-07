## Description

You are given an integer array `nums` and a **positive** integer `k`.
A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

- $(\text{sub}[0] + \text{sub}[1]) \% k = (\text{sub}[1] + \text{sub}[2]) \% k = ... = (sub[x - 2] + sub[x - 1]) \% k.$

Return the length of the **longest** **valid** subsequence of `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,5], k = 2

**Output:** 5

**Explanation:**

The longest valid subsequence is `[1, 2, 3, 4, 5]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,4,2,3,1,4], k = 3

**Output:** 4

**Explanation:**

The longest valid subsequence is `[1, 4, 1, 4]`.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{3}$

- $1 \le \text{nums}[i] \le 10^{7}$

- $1 \le k \le 10^{3}$