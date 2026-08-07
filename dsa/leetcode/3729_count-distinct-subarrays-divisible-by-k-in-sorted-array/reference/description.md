## Description

You are given an integer array `nums` **sorted** in **non-descending** order and a positive integer `k`.

A **subarray** of `nums` is **good** if the sum of its elements is **divisible** by `k`.

Return an integer denoting the number of **distinct** **good** subarrays of `nums`.

Subarrays are **distinct** if their sequences of values are. For example, there are 3 **distinct** subarrays in `[1, 1, 1]`, namely `[1]`, `[1, 1]`, and `[1, 1, 1]`.
### Function Contract

**Inputs**

- `nums`: An integer array already sorted in non-descending order.
- `k`: The positive divisor used to test each subarray sum.

A subarray is a nonempty contiguous sequence. Two occurrences with identical value sequences represent the same distinct subarray even when they use different indices.

**Return value**

Return the integer number of different subarray value sequences whose element sum is congruent to $0$ modulo `k`.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3], k = 3

**Output:** 3

**Explanation:**

The good subarrays are `[1, 2]`, `[3]`, and `[1, 2, 3]`. For example, `[1, 2, 3]` is good because the sum of its elements is $1 + 2 + 3 = 6$, and $6 \% k = 6 \% 3 = 0$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,2,2,2,2,2], k = 6

**Output:** 2

**Explanation:**

The good subarrays are `[2, 2, 2]` and `[2, 2, 2, 2, 2, 2]`. For example, `[2, 2, 2]` is good because the sum of its elements is $2 + 2 + 2 = 6$, and $6 \% k = 6 \% 6 = 0$.

Note that `[2, 2, 2]` is counted only once.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- `nums` is sorted in non-descending order.

- $1 \le k \le 10^{9}$