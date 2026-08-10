## General

**What symmetry means for ordinary and diagonal pairs**

A row `(X,Y)` has a symmetric partner when another row `(Y,X)` exists. For unequal coordinates, one row in each direction is sufficient. The output keeps only the orientation satisfying `X <= Y`, so `(20,21)` is returned while `(21,20)` is not.

Diagonal coordinates require special care. A row `(20,20)` reverses to the same values, but the problem’s pair interpretation requires two coordinate rows. One physical row must not partner with itself. Therefore, `(x,x)` qualifies only when it occurs at least twice.

**Give duplicate rows temporary identities**

The CTE `P` selects every input row and assigns `ROW_NUMBER() OVER () AS id`. The order of these IDs is irrelevant. Their only purpose is to distinguish physical occurrences that have identical `x` and `y` values.

The query joins `P AS p1` to `P AS p2` under four effective conditions:

- `p1.x = p2.y`;
- `p1.y = p2.x`;
- `p1.x <= p1.y`; and
- `p1.id != p2.id`.

The first two conditions enforce reversal. The third keeps the canonical lower-or-equal orientation. The fourth requires two distinct source rows.

For an off-diagonal pair such as `(20,21)` and `(21,20)`, their IDs are naturally different. For two copies of `(20,20)`, each can join the other. For only one copy, the equal-ID candidate is rejected and no result is produced.

**Why `DISTINCT` is still required**

The table may contain duplicates. If there are three copies of `(20,21)` and four copies of `(21,20)`, the self-join creates twelve matching row pairs. The requested output contains the unique coordinate only once. `SELECT DISTINCT p1.x, p1.y` collapses all those physical matches into one logical result.

Diagonal duplicates also create multiple ordered ID pairs, and `DISTINCT` similarly reduces them to one output row.

**Ordering the final relation**

`ORDER BY 1, 2` refers to the first and second selected columns, `x` and `y`. Both directions default to ascending, exactly matching the requested lexicographic order: smaller `x` first, and for equal `x`, smaller `y` first.

**Why the logical result is correct**

Any returned row comes from two different IDs whose coordinates reverse one another. It is therefore backed by two distinct symmetric rows. Its orientation satisfies `x <= y`, and `DISTINCT` guarantees uniqueness.

Conversely, take any qualifying symmetric coordinate pair. Its two physical rows appear in `P` with different IDs, satisfy the reversal join, and one orientation satisfies `x <= y`. That orientation reaches the selection. If it is diagonal, the existence of two rows supplies the required different IDs. Thus no valid output is missed.

**The exact query does not use the manifest’s aggregation method**

The manifest summary says duplicate coordinates are aggregated before a reversed-pair join. The protected SQL does something different: it preserves every physical row, assigns IDs, and joins those rows directly.

This distinction affects complexity substantially. With $R/2$ copies of `(1,2)` and $R/2$ copies of `(2,1)`, the logical join can produce $\Theta(R^2)$ matching pairs before `DISTINCT` reduces them to one coordinate. An aggregated solution would compress these to two counted rows and avoid that explosion.

Database optimizers may use hashing, indexes, or distinct-pushdown to reduce practical work, so SQL runtime is plan-dependent. Nevertheless, the relational intermediate of this exact formulation has quadratic worst-case cardinality. It is inaccurate to claim the manifest’s $O(R + D\log D)$ bound for the executable query without assuming a powerful optimizer rewrite.

## Complexity detail

Let $R$ be the number of input rows and $D$ the number of distinct qualifying output coordinates. Assigning IDs and scanning rows is at least $O(R)$. The self-join can produce $\Theta(R^2)$ matches under heavy duplicate reversal, and duplicate elimination must process that logical result unless optimized away. Final ordering costs $O(D\log D)$.

A safe query-level worst-case description is $O(R^2 + D\log D)$ time and potentially $O(R^2)$ intermediate work or storage, though an actual MySQL plan may stream or optimize portions. The materialized CTE itself is $O(R)$; the final distinct result is $O(D)$. These bounds differ from the aggregated algorithm named in the manifest.

## Alternatives and edge cases

- **Aggregate by `x,y` first:** Store `COUNT(*)` for each coordinate, join one distinct row to its reverse, and require count at least two for diagonals. This avoids duplicate cross products and matches the manifest summary.
- **Use `EXISTS`:** A correlated existence test can stop after finding one partner, but it still needs a distinct output and an explicit different-row mechanism for diagonal values.
- **Omit row IDs:** Then a single `(x,x)` row can join itself and be incorrectly reported.
- **Omit `x <= y`:** Both `(x,y)` and `(y,x)` would appear for off-diagonal pairs.
- **Omit `DISTINCT`:** Duplicate input rows can generate many repeated output coordinates.
- **One diagonal row:** It is not enough; `id != id` rejects self-pairing.
- **Two or more diagonal rows:** At least one different-ID pairing exists, and the coordinate appears exactly once after `DISTINCT`.
- **Heavy duplicates:** The result remains correct, but the exact row-level join may have quadratic intermediate cardinality.
- **Unordered `ROW_NUMBER`:** Deterministic numbering is unnecessary because only ID inequality matters.
