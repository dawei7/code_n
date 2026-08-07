## Description

You are given an integer array `nums` and two integers, `k` and `m`.

Return the **maximum** sum of `k` non-overlapping subarrays of `nums`, where each subarray has a length of **at least** `m`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,-1,3,3,4], k = 2, m = 2

**Output:** 13

**Explanation:**

The optimal choice is:

- Subarray `nums[3..5]` with sum $3 + 3 + 4 = 10$ (length is $3 \ge m$).

- Subarray `nums[0..1]` with sum $1 + 2 = 3$ (length is $2 \ge m$).

The total sum is $10 + 3 = 13$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-10,3,-1,-2], k = 4, m = 1

**Output:** -10

**Explanation:**

The optimal choice is choosing each element as a subarray. The output is $(-10) + 3 + (-1) + (-2) = -10$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 2000$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- $1 \le k \le floor(\text{nums.length} / m)$

- $1 \le m \le 3$