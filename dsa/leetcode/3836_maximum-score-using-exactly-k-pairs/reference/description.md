## Description

You are given two integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively, and an integer `k`.

You must choose **exactly** `k` pairs of indices $(i_{1}, j_{1}), (i_{2}, j_{2}), ..., (i_{k}, j_{k})$ such that:

- $0 \le i_{1} < i_{2} < ... < i_{k} < n$

- $0 \le j_{1} < j_{2} < ... < j_{k} < m$

For each chosen pair `(i, j)`, you gain a score of $\text{nums1}[i] * \text{nums2}[j]$.

The total **score** is the **sum** of the products of all selected pairs.

Return an integer representing the **maximum** achievable total score.
### Function Contract

**Inputs**

- `nums1`: The first integer array.
- `nums2`: The second integer array.
- `k`: The exact number of ordered index pairs to select.

Let $N=\lvert\texttt{nums1}\rvert$, $M=\lvert\texttt{nums2}\rvert$, and $K=\texttt{k}$. A legal selection consists of index chains

$0\le i_1<i_2<\cdots<i_K<N$

and

$0\le j_1<j_2<\cdots<j_K<M.$

Its score is

$\sum_{t=1}^{K}\texttt{nums1}[i_t]\texttt{nums2}[j_t].$

**Return value**

Return the largest score among all legal selections of exactly $K$ pairs.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [1,3,2], nums2 = [4,5,1], k = 2

**Output:** 22

**Explanation:**

One optimal choice of index pairs is:

- $(i_{1}, j_{1}) = (1, 0)$ which scores $3 * 4 = 12$

- $(i_{2}, j_{2}) = (2, 1)$ which scores $2 * 5 = 10$

This gives a total score of $12 + 10 = 22$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [-2,0,5], nums2 = [-3,4,-1,2], k = 2

**Output:** 26

**Explanation:**

One optimal choice of index pairs is:

- $(i_{1}, j_{1}) = (0, 0)$ which scores $-2 * -3 = 6$

- $(i_{2}, j_{2}) = (2, 1)$ which scores $5 * 4 = 20$

The total score is $6 + 20 = 26$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums1 = [-3,-2], nums2 = [1,2], k = 2

**Output:** -7

**Explanation:**

The optimal choice of index pairs is:

- $(i_{1}, j_{1}) = (0, 0)$ which scores $-3 * 1 = -3$

- $(i_{2}, j_{2}) = (1, 1)$ which scores $-2 * 2 = -4$

The total score is $-3 + (-4) = -7$.

</div>
### Constraints

- $1 \le n = \text{nums1.length} \le 100$

- $1 \le m = \text{nums2.length} \le 100$

- $-10^{6} \le \text{nums1}[i], \text{nums2}[i] \le 10^{6}$

- $1 \le k \le min(n, m)$