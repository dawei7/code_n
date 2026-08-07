## Description

You are given an integer array `nums` of length `n`, where `nums` is a **permutation** of the numbers in the range `[0..n - 1]`.

You may swap elements at indices `i` and `j` **only if** $\text{nums}[i] AND \text{nums}[j] = k$, where `AND` denotes the bitwise AND operation and `k` is a **non-negative** integer.

Return the **maximum** value of `k` such that the array can be sorted in **non-decreasing** order using any number of such swaps. If `nums` is already sorted, return 0.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [0,3,2,1]

**Output:** 1

**Explanation:**

Choose $k = 1$. Swapping $\text{nums}[1] = 3$ and $\text{nums}[3] = 1$ is allowed since $\text{nums}[1] AND \text{nums}[3] = 1$, resulting in a sorted permutation: `[0, 1, 2, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,1,3,2]

**Output:** 2

**Explanation:**

Choose $k = 2$. Swapping $\text{nums}[2] = 3$ and $\text{nums}[3] = 2$ is allowed since $\text{nums}[2] AND \text{nums}[3] = 2$, resulting in a sorted permutation: `[0, 1, 2, 3]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,2,1,0]

**Output:** 0

**Explanation:**

Only $k = 0$ allows sorting since no greater `k` allows the required swaps where $\text{nums}[i] AND \text{nums}[j] = k$.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le n - 1$

- `nums` is a permutation of integers from `0` to $n - 1$.