## General

**Translate each painted value into matrix coordinates**

The paint sequence contains values, but completion is defined by row and column positions. Searching the whole matrix for every `arr[k]` would repeat work.

The solution first builds reverse map `idx`:

$$
\texttt{idx[value]}=(\texttt{row},\texttt{column}).
$$

Every matrix value is unique, so each key maps to exactly one cell.

After this preprocessing, locating the next painted cell is an expected constant-time dictionary lookup.

**Maintain painted counts**

Array `row` has one entry per matrix row; `row[i]` is the number of painted cells currently in row $i$.

Array `col` similarly stores painted cells per column.

When `arr[k]` maps to $(i,j)$, exactly one new cell in row $i$ and column $j$ is painted. The code increments:

`row[i] += 1`

and:

`col[j] += 1`.

All other row and column counts remain unchanged.

**Recognize completion immediately**

Each row contains $n$ cells. It becomes complete exactly when:

$$
\texttt{row[i]}=n.
$$

Each column contains $m$ cells and becomes complete exactly when:

$$
\texttt{col[j]}=m.
$$

Only the row and column incident to the newly painted cell can change status. Testing those two counters is sufficient; rescanning other lines is unnecessary.

If either equality holds, the function returns current paint index `k`.

**Why the first returned index is minimal**

The paint loop processes `arr` from index zero upward.

Before iteration $k$, no row or column was complete; otherwise the function would already have returned at the earlier iteration that completed it.

After painting at $k$, the two updated counters determine whether completion first occurs now. Therefore, the first successful test is automatically the smallest valid index.

No search over possible answers or postprocessing is needed.

**Why counts never overcount**

Both `arr` and `mat` contain each integer from one through $mn$ exactly once.

Thus:

- each paint value identifies one cell;
- no cell is painted twice;
- a row count increases once for each distinct painted cell in that row;
- a column count behaves likewise.

Without uniqueness, repeated paint values would require a separate painted-state check before incrementing.

**Trace the first example**

For:

`mat = [[1,4],[2,3]]`,

the reverse map includes:

- one at $(0,0)$;
- three at $(1,1)$;
- four at $(0,1)$;
- two at $(1,0)$.

Painting one gives row-zero count one and column-zero count one.

Painting three gives row-one count one and column-one count one.

Painting four makes row zero contain two painted cells, equal to its width. At index two the method returns two. Column one also becomes complete at the same step, but the requested answer is the index, so one condition is enough.


After processing paint indices zero through $k$:

- `row[i]` equals the number of values from that prefix located in matrix row $i$;
- `col[j]` equals the number located in column $j$.

The reverse mapping makes each update target exactly the current cell, so induction proves the invariant.

Under it, equality with row width or column height is equivalent to every cell in that line having appeared. The increasing scan and immediate return prove the result is the earliest completion index.

**Why a completion always occurs**

The full `arr` sequence paints every matrix cell. By its final index, every row and every column is complete.

The exact Python function has no explicit return after the loop, but valid constraints guarantee some iteration executes the return branch. It cannot fall through for a valid input.

**Memory tradeoff**

The coordinate dictionary duplicates one pair of indices per matrix value. This is the price for avoiding repeated searches.

Since total cells are at most $10^5$, linear mapping storage is appropriate.

**Input preservation**

The matrix and paint order are only read. Painted state is represented by counters rather than by overwriting cells.

## Complexity detail

Building `idx` visits all $mn$ cells in $O(mn)$ time. The paint loop processes at most $mn$ values, each with expected $O(1)$ lookup and updates. Total time is $O(mn)$.

The coordinate map stores $mn$ entries. Row and column counters use $O(m+n)$ space. Total auxiliary space is $O(mn)$.

## Alternatives and edge cases

- **Search the matrix for every paint value:** Can take $O((mn)^2)$ time and repeats coordinate work.
- **Store row and column directly by value in arrays:** Since values are from one through $mn$, two indexed arrays can replace the dictionary.
- **Mark cells and rescan lines:** Correct but adds unnecessary row or column scans per query.
- **One-row matrix:** The row completes only after all cells, while a column completes on its single cell; the first paint returns index zero.
- **One-column matrix:** Symmetric behavior also returns zero.
- **Row and column complete together:** Return the same current index once.
- **Uniqueness:** It guarantees no duplicate painting or counter overcount.
- **Earliest index:** Immediate return during increasing scan enforces minimality.
- **Full sequence:** Guarantees the function eventually returns.
- **Input preservation:** No matrix cell is altered.
