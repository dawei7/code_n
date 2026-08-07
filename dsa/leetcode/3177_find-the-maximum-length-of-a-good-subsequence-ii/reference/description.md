## Description

You are given an integer array `nums` and a **non-negative** integer `k`. A sequence of integers `seq` is called **good** if there are **at most** `k` indices `i` in the range `[0, seq.length - 2]` such that $\text{seq}[i] \neq seq[i + 1]$.

Return the **maximum** possible length of a **good** subsequence of `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,1,3], k = 2

**Output:** 4

**Explanation:**

The maximum length subsequence is `[<u>1</u>,<u>2</u>,<u>1</u>,<u>1</u>,3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,4,5,1], k = 0

**Output:** 2

**Explanation:**

The maximum length subsequence is `[<u>1</u>,2,3,4,5,<u>1</u>]`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 5 * 10^{3}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le min(50, \text{nums.length})$