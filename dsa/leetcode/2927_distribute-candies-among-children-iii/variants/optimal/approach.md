## General

**Count without the upper bounds first.** For a non-negative total $s$, the
stars-and-bars count of ordered triples satisfying $x+y+z=s$ is

$$
F(s)=\binom{s+2}{2}=\frac{(s+1)(s+2)}{2}.
$$

Define $F(s)=0$ when $s<0$. This convention lets the same expression handle
every relationship between `n` and `limit`.

**Remove violations with inclusion-exclusion.** A child violates the bound
when receiving at least `limit + 1` candies. For any chosen set of $k$
violating children, reserve `limit + 1` candies for each of them. The remaining
unrestricted total is $n-k(\texttt{limit}+1)$, and there are $\binom{3}{k}$
ways to choose those children. Inclusion-exclusion therefore gives

$$
\sum_{k=0}^{3}(-1)^k\binom{3}{k}
F\bigl(n-k(\texttt{limit}+1)\bigr).
$$

The alternating signs first subtract every distribution violating any one
bound, restore those counted twice for two violations, and remove the ones
counted once too many across all three. Thus each valid distribution remains
exactly once and every invalid distribution contributes zero. Evaluating the
four terms directly produces the answer without iterating over candy counts.

## Complexity detail

The formula evaluates four fixed arithmetic terms, so it takes $O(1)$ time and
$O(1)$ auxiliary space, independent of `n` and `limit`.

## Alternatives and edge cases

- **Enumerate one child's count:** For each possible first count, intersect the legal interval for the second count; this is correct but takes $O(\texttt{limit})$ time.
- **Enumerate all triples:** Three nested choices are unnecessary and can take $O(\texttt{limit}^3)$ time.
- **Insufficient capacity:** If $n>3\cdot\texttt{limit}$, no distribution exists and inclusion-exclusion evaluates to zero.
- **Inactive upper bound:** If `limit >= n`, no child can violate the cap and the result is the unrestricted stars-and-bars count.
- **Inclusive cap:** A child may receive exactly `limit`; violations begin at `limit + 1`.
- **Wide counts:** Intermediate products can exceed 32-bit signed range, so fixed-width implementations need 64-bit arithmetic.
