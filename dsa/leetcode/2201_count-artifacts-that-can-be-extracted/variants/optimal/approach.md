## General

An artifact can be extracted exactly when every grid cell in its rectangular footprint appears in `dig`.

The exact solution puts all excavated coordinates into a hash set, enumerates each artifact's at-most-four cells, and checks membership for all of them.

**Hash excavated coordinates**

The set comprehension

`{(i, j) for i, j in dig}`

stores every dug row-column pair as a tuple.

Tuple equality compares both coordinates, so `(0,1)` and `(1,0)` remain distinct cells. Hash-set membership is expected $O(1)$.

The contract says dig entries are unique, but the set would safely deduplicate them even without that guarantee.

**Unpack one artifact rectangle**

Helper `check(a)` assigns `x1, y1, x2, y2` from the artifact description.

Rows in the footprint run from `x1` through `x2` inclusive. Columns run from `y1` through `y2` inclusive.

Both range stops add one because Python excludes the stop endpoint.

**Enumerate the rectangle's Cartesian product**

The nested generator chooses every row `x` in the row interval and every column `y` in the column interval. This produces exactly all coordinates of the rectangular artifact.

For a one-cell artifact, both ranges contain one value. For a horizontal artifact, the row range has one value and columns vary. Vertical and two-dimensional rectangles follow the same code.

The constraint that an artifact covers at most four cells means this enumeration is constant-sized for each artifact.

**Require every cell to be excavated**

For each coordinate, predicate `(x, y) in s` checks whether that cell was dug.

`all(...)` returns true only if every footprint coordinate is present. It stops immediately at the first missing cell, because one covered part is enough to prevent extraction.

If it reaches the end without failure, the complete artifact is uncovered.

**Count extractable artifacts with booleans**

The outer expression `sum(check(a) for a in artifacts)` calls the helper once for every artifact.

Python treats true as one and false as zero in summation, so each fully uncovered rectangle contributes one and every partial rectangle contributes zero.

Artifacts are counted independently. The no-overlap guarantee makes their physical regions disjoint, but the algorithm would still test each description correctly even if regions shared dug cells.

**Why the returned count is exact**

If `check` returns true, every coordinate generated from the artifact's inclusive bounds is in the dug set. Those coordinates are its entire footprint, so all parts are uncovered and it can be extracted.

If any part remains covered, its coordinate is absent from the set. The generator reaches it and `all` returns false, so the artifact is not counted.

The outer generator visits every artifact exactly once. Therefore the boolean sum equals the number of extractable artifacts.

For the first example, the single-cell artifact's only coordinate is present and passes. The vertical artifact includes `(1,1)`, which is absent, so short-circuit failure leaves the total at one.

**Why `n` is not used**

All supplied coordinates are guaranteed to lie within the `n x n` grid. The algorithm never needs to allocate the whole grid or clip ranges.

Using only mentioned dig cells avoids $O(n^2)$ memory when the grid is large but excavation is sparse.

## Complexity detail

Let $d$ be the number of dug cells, $a$ the number of artifacts, and let each artifact cover at most $q=4$ cells.

Building the hash set takes expected $O(d)$ time. Checking all artifacts takes $O(aq)=O(a)$ expected time because $q$ is constant. Total time is $O(a+d)$.

The dug set stores $d$ coordinate tuples, giving $O(d)$ auxiliary space. Generators and helper variables use constant additional space. The manifest bounds match the exact implementation.

## Alternatives and edge cases

- **Boolean grid:** Mark an `n x n` matrix and inspect artifacts. Membership is constant time but space grows as $O(n^2)$ instead of only dug cells.
- **Prefix-sum grid:** A two-dimensional prefix sum can query dug counts in rectangles quickly, useful for large artifacts but excessive when each covers at most four cells.
- **Map each cell to an artifact:** Count dug parts per artifact. The no-overlap guarantee makes this possible, but it requires indexing every artifact cell first.
- **Single-cell artifact:** It is extractable exactly when its one coordinate is in the set.
- **Partially dug artifact:** One absent coordinate makes `all` false.
- **All cells dug:** Every artifact check succeeds.
- **Extra dug cells:** Coordinates outside artifacts remain in the set but affect no check.
- **Unique dig entries:** No duplicate-count correction is needed; the set would handle duplicates anyway.
- **No artifact overlap:** One dug cell cannot represent parts of two artifacts under the contract.
- **Inclusive bottom-right corner:** Both ranges use endpoint plus one, ensuring it is tested.
- **At most four cells:** Per-artifact enumeration is constant bounded.
- **Short-circuit failure:** `all` may stop before checking later cells once extraction is impossible.
- **Grid size unused:** Valid-coordinate guarantees remove the need for a full-grid allocation.
- **Input preservation:** Artifact and dig arrays are only read.
