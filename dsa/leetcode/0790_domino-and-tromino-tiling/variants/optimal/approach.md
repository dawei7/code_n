## General
**Track complete and one-cell-gap states**

Let `full[i]` count complete tilings of width `i`. A tromino can create an intermediate board whose final column is missing its top or bottom cell; the two orientations have equal counts, represented by one `gap[i]` state. Extending a complete board uses a vertical domino, two horizontal dominoes, or one of the two gap orientations closed by a tromino. Thus `full[i] = full[i - 1] + full[i - 2] + 2 * gap[i - 1]`, while `gap[i] = gap[i - 1] + full[i - 2]`.

**Collapse the states to three full counts**

Substituting the gap transition into consecutive full transitions gives `full[i] = 2 * full[i - 1] + full[i - 3]`. The bases include the empty prefix: `full[0] = 1`, `full[1] = 1`, and `full[2] = 2`. Keep only these three rolling values and apply the modulus after every update.

The complete and gap transitions classify a tiling by the pieces touching its right boundary, so their cases are exhaustive and disjoint. The collapsed recurrence is algebraically equivalent to those states; induction from the three base widths therefore counts every tiling exactly once.

## Complexity detail
The recurrence performs constant work for each width from `3` through `n`, taking $O(n)$ time. Three rolling counts use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Explicit full and gap DP:** Retain both state recurrences directly; this is also $O(n)$ time and can use $O(1)$ rolling space.
- **Matrix exponentiation:** Encode the order-three recurrence in a transition matrix to obtain $O(\log n)$ time, with more implementation overhead.
- **Top-down recursion with memoization:** This preserves $O(n)$ work but uses $O(n)$ cache and call-stack space.
- **Recompute every prefix:** Solving the recurrence from the bases separately for each width repeats work and takes $O(n^2)$ time.
- **Width one:** Only the vertical domino fits.
- **Modulo arithmetic:** Reduce during each recurrence step so large exact counts never need to be retained.
- **Empty-prefix base:** `full[0] = 1` is a recurrence device representing one way to tile no columns.
