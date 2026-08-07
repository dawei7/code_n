## Description

You are given an integer array `nums`, and an integer `k`.

For any subarray `nums[l..r]`, define its **cost** as:

$cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1)$.

Return an integer denoting the number of subarrays of `nums` whose cost is **less than or equal** to `k`.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The inclusive upper bound allowed for a subarray's cost.

Let $N=\lvert\texttt{nums}\rvert$. For $0\le l\le r<N$, define

$$
\operatorname{cost}(l,r)
=
\left(
\max(\texttt{nums}[l..r])
-
\min(\texttt{nums}[l..r])
\right)(r-l+1).
$$

**Return value**

Return the number of index pairs $(l,r)$ for which $\operatorname{cost}(l,r)\le\texttt{k}$.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2], k = 4

**Output:** 5

**Explanation:**

We consider all subarrays of `nums`:

- `nums[0..0]`: $cost = (1 - 1) * 1 = 0$

- `nums[0..1]`: $cost = (3 - 1) * 2 = 4$

- `nums[0..2]`: $cost = (3 - 1) * 3 = 6$

- `nums[1..1]`: $cost = (3 - 3) * 1 = 0$

- `nums[1..2]`: $cost = (3 - 2) * 2 = 2$

- `nums[2..2]`: $cost = (2 - 2) * 1 = 0$

There are 5 subarrays whose cost is less than or equal to 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,5,5], k = 0

**Output:** 10

**Explanation:**

For any subarray of `nums`, the maximum and minimum values are the same, so the cost is always 0.

As a result, every subarray of `nums` has cost less than or equal to 0.

For an array of length 4, the total number of subarrays is $(4 * 5) / 2 = 10$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3], k = 0

**Output:** 3

**Explanation:**

The only subarrays of `nums` with cost 0 are the single-element subarrays, and there are 3 of them.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $0 \le k \le 10^{15}$