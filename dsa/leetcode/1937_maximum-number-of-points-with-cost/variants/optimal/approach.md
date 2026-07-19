## General
**Define the row dynamic program**

Let `previous[c]` be the best score after the processed rows when the most
recent selection is column $c$. For a new row and destination column $j$, the
direct transition is

$$
\text{current}[j]
= \text{points}[r][j]
+ \max_k\left(\text{previous}[k]-\lvert k-j\rvert\right).
$$

Trying every $k$ for every $j$ would be quadratic in the column count for each
row.

**Separate transitions from the left and right**

For $k \le j$, the transition term is
`previous[k] + k - j`. Scan left to right while retaining the best value that
can reach the current column; moving one column right decreases that retained
value by one. This produces `left[j]`.

For $k \ge j$, the term is `previous[k] - k + j`. A symmetric right-to-left
scan produces `right[j]`. The better of `left[j]` and `right[j]` is exactly the
maximum over every possible previous column, so add the current cell's points
to that value.

**Advance one row at a time**

Initialize the dynamic program with the first row because it has no movement
cost. Replace `previous` with the newly computed row scores until every row is
processed, then return the largest final-column score. The two directional
scans cover all previous columns and use the exact absolute-distance penalty,
so every transition and the resulting maximum are correct.

## Complexity detail
Each of the $M$ rows performs a constant number of length-$N$ passes, giving
$O(MN)$ time. The previous scores, two directional arrays, and current scores
each contain $N$ values, so the auxiliary space is $O(N)$.

## Alternatives and edge cases
- **All-pairs row transition:** Test every previous column for every current
  column. This directly implements the recurrence but takes $O(MN^2)$ time.
- **Priority queues by distance:** Maintaining candidates while distance
  changes is more complicated than the two monotone directional passes and
  does not improve their linear row cost.
- A one-row matrix has no movement penalty; return its largest cell.
- A one-column matrix forces every choice, so the answer is the sum of that
  column.
- Staying in the same column costs zero.
- Moving may still be optimal when a larger cell value exceeds the distance
  penalty.
- Zero-valued cells remain valid selections, and the maximum score is
  non-negative under the given constraints.
