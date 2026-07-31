## General

**Begin with unrestricted triples.** Stars and bars counts the non-negative
ordered triples with sum $s$ as

$$
F(s)=\binom{s+2}{2}=\frac{(s+1)(s+2)}{2}.
$$

Set $F(s)=0$ for negative $s$ so impossible residual totals contribute
nothing without separate case analysis.

**Impose all three caps together.** A child first violates the inclusive cap
at `limit + 1`. If a chosen set of $k$ children violates it, reserve
`limit + 1` candies for each; their remaining counts and the third child's
count form an unrestricted triple with total $n-k(\texttt{limit}+1)$. There
are $\binom{3}{k}$ choices of the violating children. Inclusion-exclusion
therefore yields

$$
F(n)-3F(n-L)+3F(n-2L)-F(n-3L),
\qquad L=\texttt{limit}+1.
$$

The first subtraction removes distributions violating each individual cap.
The next term restores distributions removed once for each of two violations,
and the final term removes the remaining triple-overlap excess. Consequently,
every legal ordered distribution contributes exactly once and every illegal
one cancels. Only four formula evaluations are needed.

## Complexity detail

The fixed inclusion-exclusion expression takes $O(1)$ time and $O(1)$
auxiliary space, independent of the input values.

## Alternatives and edge cases

- **Enumerate the first child:** For each legal first count, derive the interval of second counts that leaves a legal third count; this takes $O(\min(n,\texttt{limit}))$ time.
- **Enumerate two children:** Testing every first and second count is straightforward but takes quadratic time in the cap.
- **Total exceeds capacity:** When $n>3\cdot\texttt{limit}$, no valid triple exists and the formula returns zero.
- **Cap at least the total:** No distribution can violate the cap, leaving the unrestricted value $\binom{n+2}{2}$.
- **Zero allocations:** Children may receive zero candies; the counts are non-negative rather than positive.
- **Ordered assignments:** Permuting unequal child counts creates distinct distributions because the children are distinct.
