## Description

You are given an integer `n`.

An integer `x` is considered **good** if there exist **at least** two **distinct** pairs `(a, b)` such that:

- `a` and `b` are positive integers.

- $a \le b$

- $x = a^{3} + b^{3}$

Return an array containing all good integers **less than or equal to** `n`, sorted in ascending order.
### Function Contract

**Inputs**

- `n`: The inclusive positive upper bound for candidate good integers.

Let $B$ be the largest positive integer for which $1+B^3 \le n$; when no such integer exists, take $B=0$. Let $G$ be the number of good integers in the returned array.

Only positive cube bases are permitted. Each representation must use its non-decreasing orientation $a \le b$, including pairs with $a=b$ when legal.

**Return value**

Return all integers at most `n` that have at least two distinct canonical cube-sum representations, sorted in strictly increasing order. Return an empty array if none exist.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 4104

**Output:** [1729,4104]

**Explanation:**

Among integers less than or equal to 4104, the good integers are:

- 1729: $1^{3} + 12^{3} = 1729$ and $9^{3} + 10^{3} = 1729$.

- 4104: $2^{3} + 16^{3} = 4104$ and $9^{3} + 15^{3} = 4104$.

Thus, the answer is `[1729, 4104]`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 578

**Output:** []

**Explanation:**

There are no good integers less than or equal to 578, so the answer is an empty array.

</div>
### Constraints

- $1 \le n \le 10^{9}$