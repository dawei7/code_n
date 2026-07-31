## General

**Index order is handled by processing order.** Scan `nums` from left to right.
Any dynamic-programming state already stored was created by an earlier array
position, so extending it automatically preserves subsequence order.

**Index states by ending value.** Let the state at value $v$ be the longest
valid subsequence seen so far whose final value is exactly $v$. For a current
value $x$, strict increase and the maximum jump together require the previous
value to lie in the inclusive interval $[\max(1,x-k),x-1]$.

**Query a range maximum.** A segment tree over value coordinates returns the
largest state in that predecessor interval. Add one for `x`, then point-update
coordinate `x` with the larger of its existing state and the new length.
Using a half-open tree query `[max(1, x-k), x)` excludes `x` itself and
therefore enforces strict increase.

For every processed occurrence of $x$, the range query examines exactly all
legal endpoint values belonging to earlier positions. Extending the best one
produces the optimal subsequence ending at this occurrence. Keeping the
maximum state for each value loses no useful history because future
transitions depend only on endpoint value and length. Induction over the scan
proves all states and the final maximum are optimal.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $M=\max(\texttt{nums})$. Each element
performs one segment-tree range query and one point update, each
$O(\log M)$, for total time $O(n\log M)$. The power-of-two segment tree has
$O(M)$ entries and therefore uses $O(M)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Compare each position with every earlier
  position and test both value conditions; this is simple but takes $O(n^2)$
  time.
- **Coordinate-compressed segment tree:** Compress the distinct values and use
  binary searches to locate `[x-k,x-1]`; this retains
  $O(n\log n)$ time and reduces storage to $O(n)$.
- **Ordinary LIS tails:** The usual patience-sorting array tracks the smallest
  tail by length but cannot directly enforce a bounded adjacent value jump.
- **Duplicate values:** Equal values cannot extend one another because the
  query excludes coordinate `x`; repeated occurrences may still improve the
  state stored at `x`.
- **Lower query boundary:** Values below 1 do not occur, so clamp `x-k` to 1.
- **Gap exactly `k`:** The lower endpoint is inclusive and is a legal
  predecessor.
- **Strict increase:** A negative, zero, or equal-value transition is never
  allowed, regardless of its absolute difference.
