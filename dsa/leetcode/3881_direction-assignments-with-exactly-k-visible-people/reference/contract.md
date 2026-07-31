## Function Contract

**Inputs**

- `n`: The number of people in the indexed line.
- `pos`: The index of the fixed observer.
- `k`: The exact number of other people who must be visible to that observer.

Every person chooses one of the two directions independently. The observer's own direction does not change whom that observer sees.

Let $m=n-1$ be the number of people other than the observer, and let $P=10^9+7$.

**Return value**

Return the number of complete `L`/`R` assignments that make exactly `k` of those $m$ people visible, reduced modulo $P$.
