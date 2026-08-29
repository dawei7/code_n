## General

**The last assignment determines every cell**

Each query overwrites an entire row or column. For a particular cell $(r,c)$, its final value comes from whichever is later: the last assignment to row $r$ or the last assignment to column $c$. Earlier values written to that cell are irrelevant.

A forward simulation struggles with these overwrites. Updating $n$ cells per query costs $O(qn)$, and maintaining only row or column totals is awkward because a later perpendicular assignment replaces parts of earlier work.

Processing the queries in reverse turns “which write is last?” into “which write is encountered first?” Once a row or column is seen in reverse, its final assignment is known and every earlier query to that same line can be ignored.

**Track lines whose final write is already fixed**

The set `row` contains row indices already encountered while walking backward. Likewise, `col` contains finalized column indices.

For a reversed row query `[0, i, v]`:

- if `i` is already in `row`, a later forward-time query overwrote this row, so the current query contributes nothing;
- otherwise, this is the last forward-time assignment to row `i`.

The symmetric reasoning applies to a column query.

**Count only cells not already claimed by a perpendicular line**

Suppose a new final row assignment with value `v` is found. Some columns have already been finalized in reverse. Those column queries occurred later in forward time, so their values win at intersections with this row. There are `len(col)` such columns.

The remaining $n-\lvert\texttt{col}\rvert$ cells receive `v` in the final matrix. Their total contribution is:

$$
v\left(n-\lvert\texttt{col}\rvert\right).
$$

After adding it, row `i` is inserted into `row`.

For a newly finalized column, exactly $n-\lvert\texttt{row}\rvert$ cells have not already been claimed by later row assignments, so its contribution is:

$$
v\left(n-\lvert\texttt{row}\rvert\right).
$$

**Why every cell is counted at most once**

Imagine assigning ownership of each final cell to its last forward-time query. During reverse traversal, that owner is encountered before every older query that also touches the cell.

When the owner is a row query, the cell's column has not yet been marked by any later column owner, so the cell is included among the unclaimed columns. Afterward, the row is marked and older column queries will exclude that cell through `len(row)`. The same argument works with row and column exchanged.

Thus no cell can contribute twice. A cell whose row and column are never queried remains zero and contributes nothing, so it need not be counted at all.

**Trace the first example**

Take $n=3$ and queries `[[0,0,1],[1,2,2],[0,2,3],[1,0,4]]`. Read them backward.

The column-zero query with value four is the first final column. No row is fixed, so it contributes $4(3-0)=12$.

The row-two query with value three is new. Column zero is already owned by a later query, leaving two cells, so it contributes $3(3-1)=6$.

The column-two query with value two is new. Row two is already owned by a later query, leaving two cells, so it contributes $2(3-1)=4$.

Finally, row zero with value one is new. Two columns are already finalized, leaving one cell, so it contributes $1(3-2)=1$. The sum is $12+6+4+1=23$.

Notice that the algorithm never constructs the matrix, yet this accounting assigns exactly the same final value to every nonzero cell.

**Repeated line assignments**

If a row appears many times, only its first occurrence in reverse matters. The membership check discards all older assignments. This is essential: adding them would count values that are overwritten in the final state.

Values may be zero. A final zero assignment contributes zero numerically, but the row or column must still be marked. It overwrites older nonzero assignments just as decisively as any other value.

**A concise correctness argument**

For every cell, the final value is supplied by its latest touching query. Reverse traversal visits that query before all competing older queries. When visited, the algorithm counts the cell because no later perpendicular owner has excluded it. It then marks the query's line, ensuring all older competing queries exclude the cell. Therefore every cell with a final assigned value is counted exactly once with that value, while untouched cells contribute zero. The accumulated `ans` is the final matrix sum.

## Complexity detail

Let $q$ be the number of queries. Reversing through `queries[::-1]` visits each query once. Expected set lookup and insertion are $O(1)$, so expected time is $O(q)$.

The slice `queries[::-1]` creates a reversed list containing $q$ references in Python, so the exact implementation uses $O(q)$ temporary space in addition to the sets. The `row` and `col` sets together hold at most $2n$ indices, or $O(n)$ space. Consequently the implementation's total auxiliary space is $O(q+n)$, even though the manifest's $O(n)$ summary describes the algorithmic tracking sets and a reverse-iterator implementation could avoid the slice. Replacing the slice with `reversed(queries)` would realize $O(n)$ auxiliary space without changing the logic.

The accumulated sum can be large, but Python integers expand as needed. No modulo is requested.

## Alternatives and edge cases

- **Build the full matrix:** Straightforward but costs $O(n^2+qn)$ time in a literal row/column update and $O(n^2)$ storage.
- **Forward overwrite bookkeeping:** Possible with more complicated correction terms, while reverse processing makes final ownership direct.
- **Use boolean arrays:** Two length-$n$ arrays can replace the sets and give deterministic $O(1)$ membership with the same asymptotic storage.
- **Use `reversed(queries)`:** Avoids the $O(q)$ list copy created by `queries[::-1]` and matches the manifest's $O(n)$ auxiliary bound.
- **Repeated row or column:** Only the last forward assignment matters; older ones are skipped.
- **Zero-valued query:** It adds zero but must still mark its line to suppress older writes.
- **No query for a cell:** The cell remains at its initial zero and needs no contribution.
- **All rows finalized:** Later reversed column discoveries contribute only cells in any rows not yet finalized, possibly zero.
- **All columns finalized:** The symmetric zero-contribution situation is handled by `n - len(col)`.
- **Single-cell matrix:** The first reversed query touching its only row or column determines the answer; every older query is excluded.
