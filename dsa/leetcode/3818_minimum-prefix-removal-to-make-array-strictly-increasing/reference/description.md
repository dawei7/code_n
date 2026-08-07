## Description

You are given an integer array `nums`.

You need to remove **exactly** one prefix (possibly empty) from nums.

Return an integer denoting the **minimum** length of the removed prefix such that the remaining array is **strictly increasing**.
### Function Contract

**Inputs**

- `nums`: A non-empty array of integers.

Let $N=\lvert\texttt{nums}\rvert$. Removing a prefix of length $k$ leaves `nums[k:]`; $k=0$ denotes the empty prefix. A remaining array is strictly increasing exactly when every adjacent pair satisfies $\text{nums}[j] < nums[j + 1]$ within that suffix. Equal neighbors do not satisfy the condition.

A solution always exists: removing the first $N-1$ elements leaves one element, which is strictly increasing. Therefore the minimum answer lies between $0$ and $N-1$ inclusive.

**Return value**

Return the smallest prefix length whose removal leaves a strictly increasing array.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,-1,2,3,3,4,5]

**Output:** 4

**Explanation:**

Removing the $prefix = [1, -1, 2, 3]$ leaves the remaining array `[3, 4, 5]` which is strictly increasing.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,3,-2,-5]

**Output:** 3

**Explanation:**

Removing the $prefix = [4, 3, -2]$ leaves the remaining array `[-5]` which is strictly increasing.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** 0

**Explanation:**

The array `nums = [1, 2, 3, 4]` is already strictly increasing so removing an empty prefix is sufficient.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}​​​​​​​$