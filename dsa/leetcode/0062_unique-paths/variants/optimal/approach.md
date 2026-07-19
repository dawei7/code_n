## General
**A path is completely determined by the positions of one move type**

Every path contains exactly $m - 1$ downward moves and $n - 1$ rightward moves, in some order. Once the positions of all downward moves are chosen, every remaining position must be a right move, so the movement sequence is determined. The answer is a binomial coefficient over $m + n - 2$ total positions.

**Choose the smaller move group to minimize arithmetic steps**

Let $N=m+n-2$ be the total number of moves. Use symmetry $\binom{N}{r} = \binom{N}{N-r}$ and let $r = \min(m - 1, n - 1)$. Compute the coefficient incrementally rather than constructing two factorials. At step `i`, multiply by `total - r + i` and divide by `i`.

The chosen recurrence yields an integer after every complete step, so arbitrary-precision implementations remain exact. Fixed-width implementations should use a sufficiently wide intermediate type or divide common factors safely before multiplication.

**Every intermediate value is a smaller binomial coefficient**

After iteration $i$, the running result equals $\binom{N-r+i}{i}$. Multiplying by `total - r + i` and dividing by `i` applies the standard neighboring-binomial recurrence, preserving integrality.

**Trace a rectangular grid**

For a 3-by-7 grid there are 8 moves, including 2 downward moves. Choosing their positions gives $\binom{8}{2} = 8 \cdot 7 / 2 = 28$ paths.

**Paths are in bijection with move-position choices**

Every valid route contains exactly $m - 1$ downward moves and $n - 1$ rightward moves. Recording which positions in the complete move sequence are downward uniquely determines every remaining position as rightward, so it reconstructs one path.

Conversely, any choice of that many positions yields a legal monotone route ending at the destination. The mapping is one-to-one, making the path count the corresponding binomial coefficient; the incremental product evaluates that coefficient exactly.

## Complexity detail
The loop uses the smaller of the two move counts, taking $O(\min(m,n))$ arithmetic steps and $O(1)$ auxiliary variables.

## Alternatives and edge cases
- **Grid dynamic programming:** is straightforward and takes $O(mn)$ time, reducible to $O(\min(m,n))$ storage.
- **Unmemoized recursion:** follows the movement definition directly but recomputes overlapping states exponentially.
- **Factorials:** express the formula compactly but create larger intermediate values and may overflow fixed-width types sooner.
- If either dimension is one, $r = 0$, the loop performs no work, and the single straight path is returned.
- This combinatorial shortcut depends on every cell being available. Obstacles destroy the equal move-order counting and require dynamic programming as in problem 63.
