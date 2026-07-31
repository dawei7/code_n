## General

Track the best attainable sum for every selected-element count and remainder. Let `best[c][r]` be the largest sum formed from exactly `c` processed values whose remainder modulo three is `r`. Initialize only `best[0][0]` to zero; use `-1` for every unreachable state because all input values are positive.

For each value, process `c` from two down to zero. If `best[c][r]` is reachable, adding the value proposes a sum for `best[c + 1][(r + value % 3) % 3]`. Descending count order is essential: it prevents the current value from being selected more than once during the same iteration.

After all values are processed, `best[3][0]` is the largest sum made from exactly three positions and divisible by three. Return it when reachable, and otherwise return `0`.

Inductively, each state stores the greatest sum among all selections with its exact count and remainder: skipping the current value preserves the old state, while every selection using it arises from exactly one predecessor state. The final state therefore covers every legal triplet and retains the greatest one.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each input value updates a bucket of at most three retained elements, so the running time is $O(N)$. The three constant-size buckets use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Largest values by residue:** Retain the three greatest values in each remainder class, then evaluate `(0,0,0)`, `(1,1,1)`, `(2,2,2)`, and `(0,1,2)`. This is also $O(N)$ time and $O(1)$ space, but encodes the four valid residue patterns separately.
- **Fully sorted remainder buckets:** Sorting or incrementally inserting every value in its bucket is correct but requires more than linear time or space than retaining only three maxima.
- **Exactly three:** A divisible sum formed by fewer elements is irrelevant; every candidate must use three distinct positions.
- **Repeated values:** Equal values remain separate selectable elements when they occupy separate indices.
- **No residue pattern available:** Return `0`, even though all input values are positive.
- **Only one possible triplet:** When $N=3$, return its sum if divisible by three and otherwise return `0`.
