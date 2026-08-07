## Description

You are given an array of integers `nums` of length `n` and a *positive* integer `k`.

The **power** of an array is defined as:

- Its **maximum** element if *all* of its elements are **consecutive** and **sorted** in **ascending** order.

- -1 otherwise.

You need to find the **power** of all subarrays of `nums` of size `k`.

Return an integer array `results` of size $n - k + 1$, where $\text{results}[i]$ is the *power* of $nums[i..(i + k - 1)]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,3,2,5], k = 3

**Output:** [3,4,-1,-1,-1]

**Explanation:**

There are 5 subarrays of `nums` of size 3:

- `[1, 2, 3]` with the maximum element 3.

- `[2, 3, 4]` with the maximum element 4.

- `[3, 4, 3]` whose elements are **not** consecutive.

- `[4, 3, 2]` whose elements are **not** sorted.

- `[3, 2, 5]` whose elements are **not** consecutive.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,2,2,2,2], k = 4

**Output:** [-1,-1]

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,2,3,2,3,2], k = 2

**Output:** [-1,3,-1,3,-1]

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 500$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le n$