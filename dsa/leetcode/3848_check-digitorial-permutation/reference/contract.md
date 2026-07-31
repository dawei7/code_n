## Function Contract

**Inputs**

- `n`: A positive integer whose complete multiset of decimal digits may be rearranged.

For a decimal integer $x$ with digit multiset $D(x)$, define its digit-factorial sum as

$$
F(x)=\sum_{d\in D(x)} d!.
$$

A candidate must use every digit of `n` exactly once and must have no leading zero. It is digitorial precisely when its numeric value $x$ satisfies $F(x)=x$.

Let $D$ be the number of decimal digits in `n`.

**Return value**

Return `true` if some valid digit permutation $x$ satisfies $F(x)=x$; otherwise, return `false`.
