## General

To guarantee the shortest pair without assumptions about point arrangement, the query compares every distinct point with every other distinct point. It uses a self-join to generate pairs, computes Euclidean distance, orders distances from smallest to largest, and returns the first one.

**Generating distinct-point pairs**

`Point2D AS p1` and `Point2D AS p2` are two logical copies of the same table. The join condition is:

```sql
p1.x != p2.x OR p1.y != p2.y
```

It excludes a row paired with itself because identical points have equal $x$ and equal $y$, making both inequalities false. For two distinct coordinate pairs, at least one coordinate differs, so the OR is true.

The composite primary key guarantees coordinates are unique. Therefore, coordinate inequality is equivalent to distinct rows.

Every unordered pair appears twice: once as $(p_1,p_2)$ and once as $(p_2,p_1)$. Their distances are equal. This doubles constant work but does not change the minimum.

**Computing distance**

For each joined pair, the source evaluates:

$$
\sqrt{(p_1.x-p_2.x)^2+(p_1.y-p_2.y)^2}.
$$

`POW(..., 2)` squares each coordinate difference, `SQRT` converts squared distance to Euclidean distance, and `ROUND(..., 2)` produces the required two-decimal value.

The query could compare squared distances and apply one square root after finding the minimum because square root is increasing. The exact source computes full distance for every pair, which is simpler to read but does more numeric work.

**Ordering and limiting**

The computed column is the first selected expression and is aliased `shortest`. `ORDER BY 1` sorts by that rounded distance ascending. `LIMIT 1` returns one row containing the smallest rounded value.

Rounding occurs before ordering. Rounding to a fixed number of decimal places is monotone nondecreasing: if $a<b$, then rounded $a$ cannot become greater than rounded $b$ under ordinary SQL rounding. Two nearby distances may tie after rounding, but either tied row displays the same rounded value. Therefore, minimum of the rounded distances equals the rounded global minimum, and the returned numeric result remains correct.

Computing `MIN` on exact squared distances and rounding afterward would express the mathematical sequence more directly and avoid depending on this monotonicity observation.

**Tracing the sample**

The three points generate six oriented distinct pairs. Distances between `(-1,-1)` and `(0,0)` are $\sqrt2$, between `(-1,-1)` and `(-1,-2)` are 1, and between `(0,0)` and `(-1,-2)` are $\sqrt5$. Each appears in both orientations. Rounded ascending order starts with 1.00, so the query returns it.

The description’s explanatory coordinate `(-1,2)` appears to be a typo relative to the table; the actual nearest pair uses `(-1,-2)`. The query follows table coordinates.

**Why the query is correct**

The self-join produces every ordered pair of distinct points, so for every unordered pair relevant to the problem, at least one—and in fact two—joined rows exist. The distance expression computes that pair’s exact Euclidean distance before presentation rounding.

Ordering places a minimum rounded distance first, and monotonic rounding ensures this value equals the global minimum distance rounded to two decimals. `LIMIT 1` returns exactly one row with the required alias.

No pair involving the same point survives, so zero self-distances cannot incorrectly dominate. Unique coordinates also prevent two different rows from representing a genuine zero distance.

## Complexity detail

Let $P$ be the number of points. The self-join produces $P(P-1)=\Theta(P^2)$ oriented pairs, and distance calculation is constant work per pair. Pair generation and evaluation therefore take $O(P^2)$ time.

With a top-one/priority optimization, the engine can track the smallest value while scanning pairs, supporting the manifest’s $O(P^2)$ time and $O(1)$ aggregate state beyond join iteration. However, the exact SQL requests `ORDER BY ... LIMIT 1`. An engine that materializes and fully sorts all pair rows could use $O(P^2\log P)$ time and $O(P^2)$ temporary space. The manifest’s $O(1)$ space assumes streaming/top-one execution and is not guaranteed by the declarative text alone.

The output itself is one scalar row. SQL optimizer, indexes, and join strategy determine physical resources.

## Alternatives and edge cases

- **Aggregate minimum squared distance:** `ROUND(SQRT(MIN(dx*dx+dy*dy)),2)` avoids sorting and computes square root once. It more directly supports $O(1)$ aggregate state.
- **Generate unordered pairs only:** Use a lexicographic condition such as `p1.x < p2.x OR (p1.x = p2.x AND p1.y < p2.y)` to halve pair rows.
- **Closest-pair divide and conquer:** In procedural code, sorting by coordinate and merging strips achieves $O(P\log P)$ time, but is much more complex than portable SQL.
- **Self-pairs:** Must be excluded or distance zero always wins.
- **Same $x$, different $y$:** OR condition keeps the pair because the $y$ inequality is true.
- **Same $y$, different $x$:** Symmetrically retained.
- **Duplicate coordinates:** Forbidden by the composite primary key; otherwise distinct rows at distance zero would be a legitimate minimum.
- **Only one point:** The join has no rows, so this exact query returns no row. The intended problem domain must provide at least two points for a shortest pair to exist.
- **Rounding ties:** Any tied pair produces the same displayed result, so `LIMIT 1` remains sufficient.
- **Round after minimum:** Preferable for mathematical clarity even though fixed-precision rounding is monotone.
- **Ordered-pair duplication:** Doubles constant work but not asymptotic complexity or result.
- **Physical-plan caveat:** `ORDER BY LIMIT 1` may be optimized as top-one, but a full materialized sort would violate the manifest’s constant-space assumption.
- **Any coordinate signs:** Squared differences handle negative coordinates correctly.
