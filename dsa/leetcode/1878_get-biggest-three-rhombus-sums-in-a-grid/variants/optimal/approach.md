## General

**Describe every rhombus by a center and radius.** The source uses one-based coordinates `(i, j)` for a rhombus's center and a radius `k`. For `k > 0`, its four corners are top `(i - k, j)`, right `(i, j + k)`, bottom `(i + k, j)`, and left `(i, j - k)`. Radius zero is the area-zero rhombus consisting only of the center cell. This representation enumerates every valid rotated square exactly once because the four corners uniquely determine their center and equal vertical and horizontal radius.

**Bound the radius before enumeration.** For a center `(i, j)`, the distance to the four grid boundaries is `i - 1` upward, `m - i` downward, `j - 1` leftward, and `n - j` rightward. The largest valid radius is their minimum:

`l = min(i - 1, m - i, j - 1, n - j)`.

Every `k` from `1` through `l` keeps all four corners in the grid. Any larger radius crosses at least one boundary. The code separately inserts the center value `x` for radius zero, then loops through all positive radii, so narrow grids and single rows need no exceptional geometry branch.

**Precompute the two diagonal directions.** A rhombus border consists of diagonals, not horizontal or vertical segments. Array `s1` stores down-right diagonal prefix sums:

`s1[i][j] = s1[i - 1][j - 1] + grid[i - 1][j - 1]`.

Array `s2` stores down-left diagonal prefix sums:

`s2[i][j] = s2[i - 1][j + 1] + grid[i - 1][j - 1]`.

Both arrays use an extra row and two extra columns filled with zeros. That padding lets the recurrences and later endpoint subtractions access positions just outside the original columns without separate boundary tests. The source fills both tables in top-to-bottom order, so each referenced previous-row prefix is already known.

**Extract four edges in constant time.** For a positive radius, the code computes `a`, `b`, `c`, and `d`:

- `a = s1[i + k][j] - s1[i][j - k]` follows the down-right diagonal from the left corner toward the bottom, excluding left and including bottom.
- `b = s1[i][j + k] - s1[i - k][j]` follows the down-right diagonal from the top corner toward the right, excluding top and including right.
- `c = s2[i][j - k] - s2[i - k][j]` follows the down-left diagonal from the top corner toward the left, excluding top and including left.
- `d = s2[i + k][j] - s2[i][j + k]` follows the down-left diagonal from the right corner toward the bottom, excluding right and including bottom.

Each subtraction removes the diagonal prefix before the desired segment, leaving all cells on that edge with the stated endpoint convention. Interior cells of each edge appear exactly once.

**Correct the corner multiplicities.** Adding `a + b + c + d` includes the left and right corners once each, excludes the top corner from both upper edges, and includes the bottom corner in both lower edges. The final expression subtracts `grid[i + k - 1][j - 1]`, the bottom cell in zero-based grid coordinates, and adds `grid[i - k - 1][j - 1]`, the top cell. After this correction all four corners and every non-corner border cell appear exactly once. No interior cell is included because each prefix difference lies strictly on a border diagonal.

**Keep values distinct while retaining only the largest three.** `ss` is a `SortedSet`, so inserting an already-seen sum does not create a duplicate. It stores values in ascending order, making `ss[0]` the smallest. After processing all radii for one center, the loop repeatedly removes that smallest value while more than three distinct sums remain. Removing anything below the current top three is permanently safe: future candidates can only displace another small value, never make a discarded smaller value re-enter the final top three. At the end, `list(ss)[::-1]` converts the ascending set to a list and reverses it into the required descending order.

The trimming occurs after an entire center rather than immediately after each insertion. Correctness is unchanged because the set temporarily holds every distinct sum produced at that center, then discards all but the global largest three seen so far. This placement does, however, matter to the exact complexity analysis.

**Trace a radius-one rhombus.** With center `(i, j)` and `k = 1`, every edge contains only its destination corner under the prefix conventions. The four raw segments contribute bottom, right, left, and bottom. Subtracting bottom and adding top leaves top + right + bottom + left, exactly the four-cell border shown in the examples. This smallest positive case is a useful check on both the one-based prefix indices and the asymmetric-looking correction.

**Why enumeration is complete and sums are accurate.** Every valid rhombus has some grid-centered top and bottom alignment and a nonnegative integer radius, so the nested center and radius loops reach it. The boundary minimum accepts exactly the radii whose corners fit. Radius zero contributes its one cell directly. For a positive radius, the four prefix differences partition the border except for the known top/bottom multiplicity discrepancy, which the explicit correction fixes. Thus every candidate sum is computed once. The maintained set then applies only distinctness and order filtering, so the returned list contains precisely the largest three distinct candidate values, or all values if fewer than three exist.

## Complexity detail

Let $m$ and $n$ be the grid dimensions, and let $q=\min(m,n)$. Building `s1` and `s2` takes $O(mn)$ time and $O(mn)$ space. Across all centers, the number of enumerated radii is $O(mnq)$; each geometric sum uses a constant number of prefix lookups and arithmetic operations.

The variant manifest states $O(mnq)$ time, which describes the geometry when top-three maintenance is constant time, as in a fixed three-value structure or a set trimmed after every insertion. The exact source uses a general `SortedSet` and delays trimming until the end of each center. During one center it may temporarily contain $O(q)$ new distinct values, so an insertion or removal can cost $O(\log q)$. A strict bound for the checked-in implementation is therefore $O(mnq\log q)$ time, though $q\le 50$ under the stated constraints and the logarithmic factor is small. If the library treats the bounded problem domain as a constant, this collapses operationally to the manifest's form, but asymptotically the distinction should be visible.

The two prefix tables dominate auxiliary storage at $O(mn)$. The temporary sorted set holds at most the previous three values plus all sums for the current center before trimming, which is $O(q)$ and therefore dominated by $O(mn)$. The final list has at most three elements.

Grid values are positive and at most $10^5$. A border has at most $2m+2n$ scale in the broadest estimate, so sums remain modest for the given 50-by-50 bound. Python integers eliminate overflow concerns; fixed-width implementations should still calculate the maximum legal border sum before choosing a type.

## Alternatives and edge cases

- **Fixed top-three structure:** Track at most three distinct values with direct comparisons after every candidate. This restores constant-time answer maintenance and gives the manifest's clean $O(mn\min(m,n))$ time without relying on a balanced sorted container.
- **Enumerating every border cell:** Walking all four edges for every center and radius avoids prefix tables but adds another factor proportional to the radius, producing a substantially slower worst case.
- **Horizontal and vertical prefix sums:** They do not align with a 45-degree rhombus border. Two diagonal prefix directions are the natural structures that make each edge a difference of two stored values.
- **Area-zero rhombi:** Every individual cell is a valid candidate. The explicit `ss.add(x)` is essential because the positive-radius loop starts at one and cannot discover them.
- **Single row or single column:** Every boundary minimum is zero, so only cell values are inserted. Distinctness and top-three selection still work normally.
- **Repeated sums from different rhombi:** `SortedSet` stores a numeric sum once, as required. The task asks for distinct values, not distinct shapes.
- **Fewer than three distinct sums:** The set is never padded. Reversing it returns exactly one or two values when that is all the grid provides.
- **Corner double counting:** Simply adding four inclusive diagonal segments counts every corner twice. The exact endpoint conventions here instead omit top and duplicate bottom, so the specific subtract-bottom/add-top correction must be understood rather than replaced mechanically.
- **Dependency on `SortedSet`:** This is not Python's built-in `set`; it relies on an ordered-set implementation supplied by the execution environment. A portable solution can use an ordinary set plus fixed top-three comparisons because only three final values are needed.
