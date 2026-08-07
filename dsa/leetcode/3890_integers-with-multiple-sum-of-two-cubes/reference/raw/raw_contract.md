## Function Contract

**Inputs**

- `n`: The inclusive positive upper bound for candidate good integers.

Let $B$ be the largest positive integer for which $1+B^3 \le n$; when no such integer exists, take $B=0$. Let $G$ be the number of good integers in the returned array.

Only positive cube bases are permitted. Each representation must use its non-decreasing orientation $a \le b$, including pairs with $a=b$ when legal.

**Return value**

Return all integers at most `n` that have at least two distinct canonical cube-sum representations, sorted in strictly increasing order. Return an empty array if none exist.
