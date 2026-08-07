## Description

You are given an integer array `nums` and an integer digit `x`.

A **subarray** `nums[l..r]` is considered **valid** if the sum of its elements satisfies both of the following conditions:

- The first digit of the sum is equal to `x`.

- The last digit of the sum is equal to `x`.

Return the number of valid subarrays.
### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers.
- `x`: A digit from `1` through `9` that must match both boundary digits of a qualifying subarray sum.

Let $n = \lvert\texttt{nums}\rvert$ and

$$
S = \sum_{v \in \texttt{nums}} v.
$$

For $0 \le l \le r < n$, `nums[l..r]` is the contiguous nonempty interval from index `l` through index `r`. Positivity guarantees that every such sum has a well-defined leading digit and that prefix sums are strictly increasing.

**Return value**

Return the number of pairs $(l,r)$ for which the decimal representation of $\sum_{i=l}^{r}\texttt{nums[i]}$ starts with `x` and ends with `x`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,100,1], x = 1

**Output:** 4

**Explanation:**

The valid subarrays are:

- `nums[0..0]`: $sum = 1$

- `nums[0..1]`: $sum = 1 + 100 = 101$

- `nums[1..2]`: $sum = 100 + 1 = 101$

- `nums[2..2]`: $sum = 1$

Thus, the answer is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1], x = 2

**Output:** 0

**Explanation:**

The only subarray is `nums[0..0]` with a sum of 1, which does not satisfy the conditions.

Thus, the answer is 0.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le x \le 9$