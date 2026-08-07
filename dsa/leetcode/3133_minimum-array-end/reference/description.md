## Description

You are given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every $0 \le i < n - 1$, $nums[i + 1]$ is **greater than** $\text{nums}[i]$, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

Return the **minimum** possible value of $nums[n - 1]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, x = 4

**Output:** 6

**Explanation:**

`nums` can be `[4,5,6]` and its last element is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2, x = 7

**Output:** 15

**Explanation:**

`nums` can be `[7,15]` and its last element is 15.

</div>
### Constraints

- $1 \le n, x \le 10^{8}$