### 1. Description

You are given an integer array `nums` of length `n`.

An integer `k` is called **sortable** if `k` **divides** `n` and you can sort `nums` in **non-decreasing** order by sequentially performing the following operations:

- Partition `nums` into **consecutive subarrays** of length `k`.

- **Cyclically rotate each subarray independently** any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers `k`.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array whose fixed consecutive blocks may be cyclically rotated.

Let $n = \lvert\texttt{nums}\rvert$, and let $D$ be the number of positive divisors of $n$.

For a candidate $k$, the partition consists of `nums[0:k]`, `nums[k:2*k]`, and so on. Each block may be rotated independently, but its values cannot move to another block.

**Return value**

Return the sum of all positive divisors $k$ of $n$ for which the permitted block rotations can make `nums` non-decreasing.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,1,2]

**Output:** 3

**Explanation:**​​​​​​​

- For $n = 3$, possible divisors are 1 and 3.

- For $k = 1$: each subarray has one element. No rotation can sort the array.

- For $k = 3$: the single subarray `[3, 1, 2]` can be rotated once to produce `[1, 2, 3]`, which is sorted.

- Only $k = 3$ is sortable. Hence, the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [7,6,5]

**Output:** 0

**Explanation:**

- For $n = 3$, possible divisors are 1 and 3.

- For $k = 1$: each subarray has one element. No rotation can sort the array.

- For $k = 3$: the single subarray `[7, 6, 5]` cannot be rotated into non-decreasing order.

- No `k` is sortable. Hence, the answer is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,8]

**Output:** 3

**Explanation:**​​​​​​​

- For $n = 2$, possible divisors are 1 and 2.

- Since `[5, 8]` is already sorted, every divisor is sortable. Hence, the answer is $1 + 2 = 3$.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$