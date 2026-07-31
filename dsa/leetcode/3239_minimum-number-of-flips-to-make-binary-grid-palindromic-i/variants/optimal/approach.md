## General

For one row to be palindromic, each cell at column $c$ must equal the cell at column $n-1-c$. Consider only one representative from each mirrored pair. If the two bits already match, the pair costs zero; if they differ, flipping either one makes them equal, so the pair costs exactly one. Different mirrored pairs share no cells, and their minimum costs add independently.

Sum these mismatches across every row to obtain the exact cost of the all-rows alternative. Apply the same reasoning vertically: compare rows $r$ and $m-1-r$ in every column and sum the mismatches for the all-columns alternative.

The problem permits either complete orientation, so return the smaller total. Center cells in odd-length rows or columns have no partner and never need a flip.

## Complexity detail

The row comparisons and column comparisons each inspect $O(mn)$ cells in total, giving $O(mn)$ time. Only two counters and loop indices are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Construct reversed rows or columns repeatedly:** This can compute the same mismatches but may introduce superlinear copying work.
- **Flip greedily while scanning:** Mutation is unnecessary; each pair's minimum cost depends only on whether its original bits differ.
- A one-row grid always satisfies the all-columns alternative because each column has one cell.
- A one-column grid always satisfies the all-rows alternative.
- Odd-length centers never contribute a mismatch.
- Matching `00` and `11` pairs both cost zero.
- A mismatched `01` or `10` pair costs exactly one, regardless of which bit is flipped.
- The cheaper orientation may be zero even when the other orientation requires many flips.
- The input grid need not be square.
