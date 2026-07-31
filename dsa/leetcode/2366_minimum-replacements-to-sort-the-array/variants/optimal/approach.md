## General

**Work from the fixed suffix.** Process `nums` from right to left, maintaining
`limit`, the largest value that the current element's rightmost piece may have
without exceeding the already valid suffix. The last element starts as its own
limit.

**Use the fewest feasible pieces.** A value $x$ needs

$$
k=\left\lceil\frac{x}{\textit{limit}}\right\rceil
$$

pieces so that none exceeds `limit`. Producing $k$ pieces costs $k-1$
operations. Fewer pieces are impossible by the pigeonhole principle.

For the best future boundary, distribute $x$ as evenly as possible. Its
smallest piece is $\lfloor x/k\rfloor$; set this as the new `limit` for the
element to the left. Balanced pieces maximize that smallest value, so they
never impose a tighter left boundary than another feasible $k$-piece split.
This locally minimal split is therefore globally optimal by right-to-left
induction.

## Complexity detail

Each of $n$ values uses constant-time integer arithmetic, giving $O(n)$ time
and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Increment pieces until feasible:** This finds the same split but can take
  up to $O(\texttt{nums[i]})$ work per element.
- **Explicit splitting:** Materializing all pieces can make the intermediate
  array enormous and is unnecessary.
- **Already valid value:** When $x\le\textit{limit}$, use one piece and add no
  operation.
- **Ceiling division:** Compute `k = (x + limit - 1) // limit` exactly.
- **Large result:** The accumulated operation count may exceed 32-bit range.
