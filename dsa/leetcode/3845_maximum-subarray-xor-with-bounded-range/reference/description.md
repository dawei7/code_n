## Description

You are given a non-negative integer array `nums` and an integer `k`.

You must select a **subarray** of `nums` such that the **difference** between its **maximum** and **minimum** elements is at most `k`. The **value** of this subarray is the bitwise XOR of all elements in the subarray.

Return an integer denoting the **maximum** possible **value** of the selected subarray.
### Function Contract

**Inputs**

- `nums`: The non-negative integer array from which a nonempty contiguous subarray is selected.
- `k`: The inclusive upper bound on the selected subarray's maximum-minus-minimum difference.

For boundaries $0\le l\le r<N$, where $N=\lvert\texttt{nums}\rvert$, the selected subarray is `nums[l:r + 1]`. It is valid when

$$
\max_{l\le i\le r}\texttt{nums}[i]
-
\min_{l\le i\le r}\texttt{nums}[i]
\le \texttt{k}.
$$

Its value is

$$
\texttt{nums}[l]\mathbin{\mathrm{XOR}}\texttt{nums}[l+1]
\mathbin{\mathrm{XOR}}\cdots\mathbin{\mathrm{XOR}}\texttt{nums}[r].
$$

Let $V=2^{15}$ denote the exclusive upper bound on every input value and on every prefix XOR.

**Return value**

Return the maximum XOR value over all valid pairs of boundaries $(l,r)$. A length-one subarray is always valid because its maximum and minimum are equal.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [5,4,5,6], k = 2

**Output:** 7

**Explanation:**

- Select the subarray `[5, <u>**4, 5, 6**</u>]`.

- The difference between its maximum and minimum elements is $6 - 4 = 2 \le k$.

- The value is $4 XOR 5 XOR 6 = 7$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,4,5,6], k = 1

**Output:** 6

**Explanation:**

- Select the subarray `[5, 4, 5, <u>**6**</u>]`.

- The difference between its maximum and minimum elements is $6 - 6 = 0 \le k$.

- The value is 6.

</div>
### Constraints

- $1 \le \text{nums.length} \le 4 * 10^{4}$

- $0 \le \text{nums}[i] < 2^{15}$

- $0 \le k < 2^{15}$