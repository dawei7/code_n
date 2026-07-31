## General

The smallest valid solution never needs a digit greater than `n + 1`: using the consecutive digits from `1` through `n + 1` gives the smallest possible pool. An `'I'` can keep those digits in their natural order, while a run of `'D'` requires reversing the corresponding consecutive block.

**Delay digits inside a decreasing run.** Generate digits in increasing order and push each one onto a stack. When the current pattern symbol is `'D'`, leave the pending digits untouched because more digits may belong to the same decreasing run. At an `'I'`, pop the whole stack into the answer. Popping reverses exactly the pending block and makes all comparisons in that completed run decrease.

**Flush after the final digit.** The last decreasing run has no following `'I'`, so push digit `n + 1` and flush unconditionally at the end. Every generated digit is pushed and popped exactly once.

Before each flush, the algorithm has chosen the smallest not-yet-used consecutive digits. Reversing the shortest block forced by the current `'D'` run is necessary to satisfy those comparisons. Any smaller prefix would either use a smaller digit already committed earlier or violate a required decrease. Processing runs from left to right therefore produces the lexicographically smallest valid string.

## Complexity detail

Let $n = \lvert\texttt{pattern}\rvert$. Each of the $n+1$ digits is pushed and popped once, so the time is $O(n)$. The pending stack and constructed output use $O(n)$ space.

## Alternatives and edge cases

- **Lexicographic backtracking:** Trying unused digits from smallest to largest eventually finds the same answer, but the search can examine factorially many arrangements.
- **Reverse runs in a prepared array:** Start with digits `1..n+1` and reverse each maximal interval covered by consecutive `'D'` symbols; this is equivalent to the stack.
- **All increasing:** No reversal is needed, so the answer is `123...`.
- **All decreasing:** The entire digit sequence is one reversed block.
- **Final decreasing run:** It must be flushed after the loop even though no `'I'` follows it.
- **Distinct digits:** Reusing a digit can satisfy comparisons but violates the construction contract.
