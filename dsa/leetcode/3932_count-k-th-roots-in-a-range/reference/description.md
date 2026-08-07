## Description

You are given three integers `l`, `r`, and `k`.

An integer `y` is said to be a **perfect $k^{\text{th}}$ power** if there exists an integer `x` such that $y = x^k$.

Return the number of integers `y` in the range `[l, r]` (inclusive) that are **perfect $k^{\text{th}}$ powers**.
### Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the nonnegative integer range.
- `r`: The inclusive upper endpoint of the range, with `r >= l`.
- `k`: The positive integer exponent in the relation $y=x^k$.

For the complexity bounds, define $R=\max(2,\texttt{r}+1)$ and $K=\max(2,\texttt{k})$. A value is counted once if there exists any integer base that produces it. Both endpoints belong to the range, so a perfect power equal to `l` or `r` is included.

**Return value**

Return the number of distinct integers `y` in `[l, r]` for which some integer `x` satisfies $y=x^k$.

### Examples
#### Example 1

<div class="example-block">
**Input:** l = 1, r = 9, k = 3

**Output:** 2

**Explanation:**

The perfect cubes in the range `[1, 9]` are:

- $1 = 1^{3}$

- $8 = 2^{3}$

Hence, the answer is 2.</div>
#### Example 2

<div class="example-block">
**Input:** l = 8, r = 30, k = 2

**Output:** 3

**Explanation:**

The perfect squares in the range `[8, 30]` are:

- $9 = 3^{2}$

- $16 = 4^{2}$

- $25 = 5^{2}$

Hence, the answer is 3.</div>
### Constraints

- $0 \le l \le r \le 10^{9}$

- $1 \le k \le 30$