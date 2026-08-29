## General

**Store point multiplicities by x-coordinate**

`self.cnt[x][y]` is the number of times point $(x,y)$ has been added. The outer `defaultdict` groups points by vertical column, and each inner `Counter` maps y-coordinates to occurrence counts.

`add` increments rather than sets the count because duplicate points are distinct choices. This multiplicity directly affects how many squares can be formed.

**Choose the opposite x-column**

For query point $(x_1,y_1)$, any axis-aligned square has another horizontal corner $(x_2,y_1)$ with $x_2\ne x_1$.

The count method loops through every stored x-column `x2`. Difference

`d = x2 - x1`

is the signed horizontal displacement. The square side length is $\lvert d\rvert$, and positive area is guaranteed by skipping `x2 == x1`.

**Check both vertical directions**

For a chosen opposite column, one square uses vertical coordinate `y1 + d`. Its three stored corners are:

- $(x_2,y_1)$;
- $(x_1,y_1+d)$;
- $(x_2,y_1+d)$.

The other uses `y1 - d` and the analogous two vertical corners.

Even when `d` is negative because `x2` lies left of the query, these two formulas still cover the squares on the two sides of the horizontal line. Their roles simply swap between visually above and below.

The signed formulas also guarantee equal side lengths without calling `abs`. The horizontal difference from `x1` to `x2` is `d`. The vertical difference to `y1+d` is the same signed amount, and to `y1-d` is its negation; both have magnitude $\lvert d\rvert$. The fourth corner combines the selected opposite x and y coordinates, so all edges are axis-aligned and equal.

**Multiply occurrence counts**

For one geometric square, choosing one stored occurrence at each of its three required coordinates gives independent choices. If their counts are $a$, $b$, and $c$, the number of triples is $abc$.

The query point itself is supplied externally and is not selected from storage, so its stored multiplicity is irrelevant.

The source adds the two products for every `x2`.

**Why a missing query column returns zero**

Every square needs a vertical corner $(x_1,y_1\pm d)$ in the same x-column as the query. If `x1` is not an outer dictionary key, no stored point has that x-coordinate, so no square is possible.

The early return avoids scanning unrelated columns.

**Trace the duplicate example**

With stored points $(3,10)$ once, $(3,2)$ once, and $(11,2)$ twice, query $(11,10)$ chooses opposite column three and $d=-8$.

The relevant vertical level is two. Multiplicities are one at $(3,10)$, one at $(3,2)$, and two at $(11,2)$. Their product is two, corresponding to the two distinguishable copies of $(11,2)$.

**Why every square is counted exactly once**

Any valid square with the query has one unique other x-coordinate `x2` and one unique other y-coordinate. The outer loop reaches that column, and exactly one of `y1+d` or `y1-d` equals the square's other row, so its multiplicity product is added.

Conversely, every nonzero product names three coordinates at equal nonzero horizontal and vertical distance, forming an axis-aligned square. No geometric square appears under another `x2`.

The two vertical formulas cannot describe the same positive-area square because `d\ne0` makes `y1+d` and `y1-d` different. Thus adding both products does not double-count a single row choice.

Every contribution consequently has one unique geometric orientation.

**Counter lookups for missing corners**

An inner `Counter` returns zero for an absent y-coordinate. The product becomes zero naturally, eliminating explicit membership tests. Counter's missing-value behavior does not create a positive occurrence.

## Complexity detail

Let $H$ be the number of distinct stored x-coordinates and $P$ the number of distinct stored points. `add` takes expected $O(1)$ time.

`count` scans $H$ columns and performs constant expected-time counter lookups per column, so it takes $O(H)$ time. Stored counters use $O(P)$ space; duplicate additions increase numeric counts without adding keys.

## Alternatives and edge cases

- **Store one global pair counter:** Query could enumerate y-levels or columns, but the nested column structure matches the square geometry directly.
- **Enumerate all stored point triples:** Cubic and ignores axis alignment until late.
- **Precompute every square on add:** Makes additions expensive and requires updating many query answers.
- **Duplicate points:** Multiply the number of distinct selection triples.
- **Query point not stored:** It can still form squares; only the other three points must be stored.
- **No points in query x-column:** Immediate zero because the vertical partner is missing.
- **Same x-column candidate:** Skipped to enforce positive side length.
- **Coordinates outside 0 through 1000 after adding `d`:** Counter lookup returns zero safely.
- **Opposite column left or right:** Signed `d` formulas cover both.
- **Squares above and below:** Both are counted separately.
- **Repeated count calls:** Do not change stored multiplicities.
- **Add complexity:** One nested counter increment is expected constant time.
- **Environment imports:** The exact source assumes `defaultdict` and `Counter` are available.
- **Query-time dimension:** `count` loops over distinct stored x-coordinates, not every added point. Repeated additions change multiplicities but do not lengthen this outer scan.
