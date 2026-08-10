## General

**Turn the geometric wording into a numerical operation.** Every row stores one integer coordinate on the x-axis. For two coordinates `a` and `b`, their distance is $\lvert a-b\rvert$. The task therefore has two parts: consider every valid pair of different points, and keep the smallest distance produced by any pair. The exact query expresses both parts inside one aggregate query.

**Why the self-join is needed.** A row contains only one point, whereas a distance needs two points. Giving the table two aliases, `p1` and `p2`, lets one output row represent a pair. A completely unrestricted self-join would also pair every point with itself. Such a pair has distance zero, which would always become the minimum and would be invalid because the problem asks for two distinct points. It would also produce both orientations of every genuine pair: `(a, b)` and `(b, a)`.

The join condition `p1.x < p2.x` solves all three concerns at once:

1. A coordinate cannot be less than itself, so self-pairs disappear.
2. For two distinct coordinates, exactly one orientation satisfies the condition: the smaller coordinate is `p1.x` and the larger one is `p2.x`.
3. Because `p2.x` is now guaranteed to be larger, `p2.x - p1.x` is already the nonnegative distance. There is no need to call `ABS`.

The primary-key guarantee matters here. It says that two different rows cannot have the same `x`. Consequently, every unordered pair of distinct stored points appears exactly once after the join.

**How the aggregate finishes the query.** Each joined pair conceptually produces the expression `p2.x - p1.x`. `MIN(...)` examines those values and returns the smallest one under the output name `shortest`. The aggregate has no `GROUP BY`, so it reduces the complete joined relation to exactly one result row.

For the sample coordinates `-1`, `0`, and `2`, the condition creates these pairs:

| `p1.x` | `p2.x` | difference |
|---:|---:|---:|
| -1 | 0 | 1 |
| -1 | 2 | 3 |
| 0 | 2 | 2 |

The aggregate returns `1`. Notice that the query never creates `(0, -1)`, and it never creates `(-1, -1)`. That is why subtraction is safe and zero is not introduced accidentally.

**Why the answer is correct.** Take any two distinct input points with coordinates `a` and `b`. Exactly one of $a<b$ or $b<a$ is true. If $a<b$, the join includes the row with `p1.x = a` and `p2.x = b`; otherwise it includes the reversed assignment. Thus every legal unordered pair contributes exactly one value, and that value is its true absolute distance. Since `MIN` is applied to all and only those legal distances, the selected value must be the shortest distance in the table.

The statement guarantees at least two rows. Together with unique coordinates, that guarantees at least one joined pair. Without that promise, the join could be empty and `MIN` would return `NULL`.

**An important distinction between the exact query and the nominal bound.** The variant manifest states an $O(P\log P)$ target, where $P$ is the number of points. That is the natural bound for sorting the coordinates and comparing adjacent values. The exact SQL source shown here does not explicitly implement that plan: it joins every smaller coordinate with every larger coordinate. Its logical intermediate relation therefore contains

$$
\binom{P}{2}=\frac{P(P-1)}{2}
$$

pairs. This does not affect correctness, but it does affect the honest worst-case cost of this particular text. An optimizer may use indexes or aggregation shortcuts, but an explanation cannot assume that every SQL engine will transform a quadratic all-pairs join into an adjacent-neighbor scan.

## Complexity detail

Let $P$ be the number of rows in `Point`.

The exact self-join has one result for every unordered pair, so it produces $P(P-1)/2$ candidate distances. Evaluating the subtraction and updating a running minimum are constant-time operations per candidate. The logical worst-case time complexity of the exact query is therefore $O(P^2)$, not $O(P\log P)$.

The `MIN` aggregate itself needs only one running value, so a streaming execution can use $O(1)$ additional aggregate memory. A database engine may still allocate memory for join processing, temporary pages, or an execution plan; those physical details are engine-dependent. The manifest's $O(P)$ space allowance safely covers linear auxiliary structures, while a particularly materialized all-pairs plan could use more temporary storage.

The advertised $O(P\log P)$ time and $O(P)$ space describe the standard sort-then-scan strategy: sort all coordinates, subtract each adjacent pair, and take the minimum. If the input can truly be read in ascending coordinate order, the follow-up reduces the scan after ordering to $O(P)$ time and $O(1)$ extra working space. Those bounds should not be attributed to the literal all-pairs join without evidence that the database performs an equivalent optimization.

## Alternatives and edge cases

- **Sort and compare adjacent points:** After coordinates are ordered, the globally closest pair must be adjacent; any coordinate between two nonadjacent endpoints would create an equal or smaller neighboring gap. This gives the manifest's intended $O(P\log P)$ bound and is the preferable large-input algorithm.
- **Already ordered input:** If ascending order is guaranteed by an index scan or another explicit ordering contract, use a previous-row operation such as `LAG(x)` and minimize `x - previous_x`. The scan is linear after the ordered access.
- **Unrestricted self-join plus `ABS`:** Joining on `p1.x != p2.x` is correct, but it emits both orientations of every pair. The strict `<` condition performs half as much pair work and removes the need for `ABS`.
- **Self-pairs:** Omitting the inequality condition makes every row pair with itself, forcing the minimum to zero. The primary key does not prevent that mistake because the two aliases may refer to the same row.
- **Negative coordinates:** They require no special case. Once `p1.x < p2.x`, the subtraction `p2.x - p1.x` is positive even when one or both coordinates are negative.
- **Exactly two rows:** The join produces one candidate, so that sole distance is returned.
- **Fewer than two rows:** The official contract excludes this case. If it occurred, the aggregate would still return one row, but its `shortest` value would be `NULL`.
- **Duplicate coordinates:** The primary key forbids them. If duplicates were allowed, two distinct rows at the same coordinate would have distance zero, but the strict `<` condition would omit that valid pair; the query relies on uniqueness.
