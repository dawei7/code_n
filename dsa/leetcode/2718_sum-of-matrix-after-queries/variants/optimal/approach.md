## General

A cell's final value comes from the last query that touches either its row or its column. Processing queries forward would require revising earlier contributions when later lines overwrite intersections. Reverse processing exposes final assignments first and avoids that dependency.

Maintain the sets of rows and columns already encountered while scanning from the last query to the first. When an unseen row query with value `value` is reached, every column not already seen still has its final cell in that row determined by this query. It therefore contributes

$$
\texttt{value}\,(n-\lvert\texttt{seen_columns}\rvert).
$$

The symmetric rule for an unseen column uses the number of unseen rows. Repeated queries for a line already seen contribute nothing because a later query has fixed every cell that the earlier assignment could control.

Each matrix cell is counted exactly once: whichever of its row or column queries appears later in forward order is encountered first in reverse order. At that moment, the opposite line is unseen precisely when this query owns the cell. Untouched cells remain zero and need no contribution. Summing these disjoint final assignments yields the matrix total.

## Complexity detail

Let $q$ be the number of queries. The reverse scan performs expected $O(1)$ set operations per query, taking $O(q)$ expected time. At most $n$ row indices and $n$ column indices are stored, so auxiliary space is $O(n)$. The benchmark uses `size` as $q$ with $n=q$.

## Alternatives and edge cases

- **Materialize the matrix:** Writing every cell of each queried row or column is correct but takes $O(qn)$ time and $O(n^2)$ space.
- **Maintain the running sum forward:** This requires knowing the previous values at every overwritten intersection, which recreates matrix-sized state or more complicated bookkeeping.
- **Track only the last query per line:** Row and column timestamps still must be reconciled at every intersection, potentially taking $O(n^2)$ work.
- Repeated assignments to the same row or column count only the last one.
- A value of zero can erase earlier positive contributions.
- Rows and columns never mentioned by a query remain all zero.
- For $n=1$, the final cell is determined by the last query of either type.

