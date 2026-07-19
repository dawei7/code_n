## General
**One extreme is insufficient.** A positive cell preserves product order, but a negative cell reverses it: the smallest negative product entering that cell can become the largest positive product leaving it. Therefore each cell needs both the minimum and maximum complete product of any path reaching it. A zero naturally makes both candidate extremes zero and needs no special transition.

**Combine the only possible predecessors.** Cell `(i, j)` can be entered only from `(i - 1, j)` or `(i, j - 1)`. Multiply the current value by both stored extremes from every predecessor that exists, then retain the smallest and largest results. Initialize both extremes at `(0, 0)` to its own value. Processing cells in row-major order guarantees that the required predecessor states are ready.

Every path into a cell ends at one of those predecessors, and multiplying an interval of possible incoming products by one fixed value places its new extremes at the incoming extremes (possibly swapping their order). Thus the transition retains the extremes of all and only valid paths to that cell. Inductively, the maximum stored at the bottom-right is the true greatest path product. Return `-1` when it is negative; otherwise apply the modulus only once to that already-selected value.

## Complexity detail
Each of the $mn$ cells combines at most four candidate products, so the running time is $O(mn)$. Two $m \times n$ tables store the minimum and maximum reachable products, using $O(mn)$ auxiliary space. Rolling rows can reduce this to $O(n)$ without changing the recurrence.

## Alternatives and edge cases
- **Enumerate every path:** Depth-first search is correct, but it explores $\binom{m+n-2}{m-1}$ paths in the worst case instead of sharing work between paths that reach the same cell.
- **Store only the maximum:** This loses a large-magnitude negative value that a later negative cell could turn into the optimum.
- **Reduce products modulo $10^9+7$ during the DP:** This is incorrect because residues do not preserve either numerical order or sign; reduce only the final non-negative maximum.
- A single-cell matrix has one path, whose product is that cell itself.
- A reachable zero makes `0` a valid answer and must beat the `-1` result used when every product is negative.
- Rows or columns of length one have exactly one path and are handled by the same predecessor rules.
