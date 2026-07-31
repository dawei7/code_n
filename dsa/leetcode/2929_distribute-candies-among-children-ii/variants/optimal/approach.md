## General

**Represent distributions as bounded solutions.** Let the children's candy
counts be $x$, $y$, and $z$. Without the individual caps, stars and bars gives
the number of non-negative solutions to $x+y+z=s$:

$$
U(s)=\binom{s+2}{2}=\frac{(s+1)(s+2)}{2}.
$$

Treat $U(s)$ as zero for $s<0$, since a negative remaining candy total has no
solutions.

**Correct the unrestricted count.** A child exceeds the allowed range upon
receiving at least `limit + 1` candies. Choose $k$ children that violate the
cap and first give each of them that many candies. The residual unrestricted
total is $n-k(\texttt{limit}+1)$, and the violating set can be selected in
$\binom{3}{k}$ ways. Inclusion-exclusion gives

$$
\sum_{k=0}^{3}(-1)^k\binom{3}{k}
U\bigl(n-k(\texttt{limit}+1)\bigr).
$$

The one-child terms remove all cap violations. The two-child terms restore
assignments subtracted twice, and the three-child term removes the final
overlap excess. Thus legal triples retain coefficient one while illegal
triples cancel. Because the number of children is fixed at three, evaluating
this expression uses a fixed amount of work even when `n` and `limit` are
large.

## Complexity detail

The four inclusion-exclusion terms require $O(1)$ time and $O(1)$ auxiliary
space. Neither bound depends on `n` or `limit`.

## Alternatives and edge cases

- **One-child enumeration:** Iterate one child's legal count and derive the interval of possible counts for a second child; this is correct but takes $O(\min(n,\texttt{limit}))$ time.
- **Two-child enumeration:** Directly trying both first counts takes $O(\min(n,\texttt{limit})^2)$ time and is unnecessary.
- **Combined capacity too small:** If $n>3\cdot\texttt{limit}$, the answer is zero.
- **Upper bound inactive:** When `limit >= n`, every unrestricted triple is legal and the answer is $\binom{n+2}{2}$.
- **Inclusive boundary:** Receiving exactly `limit` is legal; shifted violations begin at `limit + 1`.
- **Large result:** The count can exceed 32-bit range, so fixed-width languages need 64-bit arithmetic.
