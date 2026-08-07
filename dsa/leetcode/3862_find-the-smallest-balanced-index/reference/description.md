## Description

You are given an integer array `nums`.

An index `i` is **balanced** if the sum of elements **strictly** to the left of `i` equals the product of elements **strictly** to the right of `i`.

If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.

Return an integer denoting the **smallest** balanced index. If no balanced index exists, return -1.
### Function Contract

**Inputs**

- `nums`: A nonempty integer array whose indices are zero-based.

Let $N = \lvert\texttt{nums}\rvert$. For an index `i`, define its left sum as

$$
L_i = \sum_{j=0}^{i-1} \texttt{nums[j]},
$$

where $L_0 = 0$. Define its right product as

$$
R_i = \prod_{j=i+1}^{N-1} \texttt{nums[j]},
$$

where $R_{N-1} = 1$. Index `i` is balanced exactly when $L_i = R_i$.

**Return value**

Return the smallest balanced index. Return `-1` when no index satisfies the
equality.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,1,2]

**Output:** 1

**Explanation:**

For index $i = 1$:

- Left sum = $\text{nums}[0] = 2$

- Right product = $\text{nums}[2] = 2$

- Since the left sum equals the right product, index 1 is balanced.

No smaller index satisfies the condition, so the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,8,2,2,5]

**Output:** 2

**Explanation:**

For index $i = 2$:

- Left sum = $2 + 8 = 10$

- Right product = $2 * 5 = 10$

- Since the left sum equals the right product, index 2 is balanced.

No smaller index satisfies the condition, so the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** -1

For index $i = 0$:

- The left side is empty, so the left sum is 0.

- The right side is empty, so the right product is 1.

- Since the left sum does not equal the right product, index 0 is not balanced.

Therefore, no balanced index exists and the answer is -1.</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$