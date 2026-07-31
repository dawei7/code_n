## General

Sort all values. The only relevant difference within a triple is its maximum
minus its minimum, so take consecutive groups of three in sorted order. Reject
immediately if `ordered[start + 2] - ordered[start] > k`; otherwise append that
triple.

To see why a failing consecutive triple proves impossibility, consider the
smallest value not assigned before its start. Any group containing it must also
choose two values from the remaining sorted suffix. Its third member cannot be
smaller than `ordered[start + 2]`, so even the narrowest possible group exceeds
`k`. Conversely, when every consecutive triple passes, those triples use every
input occurrence exactly once and directly satisfy the condition. The method
therefore returns a valid division exactly when one exists.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting takes $O(N\log N)$ time, and the
grouping scan takes $O(N)$ time. The sorted copy and returned groups use $O(N)$
space.

## Alternatives and edge cases

- **Selection sort before grouping:** It produces the same canonical triples but takes $O(N^2)$ time.
- **Backtracking over triples:** Trying arbitrary group assignments is unnecessary and grows combinatorially.
- **Duplicate values:** Occurrences remain separate elements and may fill one or several triples.
- **Exactly one group:** The three values form the answer precisely when their maximum-minus-minimum is at most `k`.
- **Failure in any group:** One oversized consecutive triple is a proof that no rearrangement can succeed.
- **Multiple valid answers:** Returning sorted consecutive triples is sufficient even when other groupings also work.
