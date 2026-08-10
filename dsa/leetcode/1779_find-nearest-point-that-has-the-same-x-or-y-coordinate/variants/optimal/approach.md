## General

**Filter by the validity rule before comparing distance**

A point `(a, b)` is valid when it lies on the same vertical line or horizontal line as `(x, y)`. The exact condition is:

`a == x or b == y`.

Only valid points compete for the answer. An invalid point may be geometrically close, but it must be ignored completely.

The exact solution scans points in original index order and keeps the best valid distance found so far.

**Compute Manhattan distance**

For each valid point, the source calculates:

`abs(a - x) + abs(b - y)`.

This is the stated Manhattan distance. Because a valid point shares at least one coordinate, one term is zero, but using the full formula is clear and works even when both coordinates match.

A point at the exact current location has distance zero and is valid through both equalities. Zero is the smallest possible distance.

**Maintain the best index and distance**

`ans` begins at minus one, meaning no valid point has been seen. `mi` begins at positive infinity, so the first valid finite distance is always accepted.

For each valid point at index `i`, the source updates only when:

`mi > d`.

The strict inequality means a genuinely smaller distance replaces the current best. It assigns both `ans = i` and `mi = d` together.

If the new distance equals `mi`, no update occurs. Since indices are visited from zero upward, the stored point is already the smallest index among all points at that distance. This implements the tie rule without an explicit index comparison.

**Trace the first example**

At location `(3,4)`:

- Point `(1,2)` shares neither coordinate and is ignored.
- Point `(3,1)` is valid with distance three, so it becomes the first best.
- Point `(2,4)` is valid with distance one and replaces it at index two.
- Point `(2,3)` is invalid.
- Point `(4,4)` is valid with distance one, tied with the current best.

The strict update keeps index two instead of later index four, producing the required answer.

**Why scan order solves ties**

Suppose several valid points share the minimum distance. The earliest one is encountered first and sets `ans` when that distance becomes the best.

Every later tied point fails `mi > d` because `mi == d`. Therefore the earliest index remains. If an even smaller distance appears later, it correctly replaces the previous result, and the same tie behavior begins for that new minimum.

This technique works because enumeration order is exactly increasing original index order.

**Why no sorting is needed**

Sorting points by distance and index could also identify the answer, but it would require storing keys or rearranging references and cost $O(n\log n)$.

A single running minimum contains all information needed: best distance and earliest index at that distance. The problem asks for only one point, not a sorted ranking.


After processing points through index `r`:

- `mi` is the smallest Manhattan distance among valid points in that prefix.
- `ans` is the smallest index in that prefix attaining `mi`.

Initially the statement holds vacuously with no point and infinity. An invalid point changes nothing. A valid point with smaller distance replaces both values, while one with equal or greater distance leaves the earlier correct best unchanged.

By induction, after the full scan the stored index is exactly the nearest valid point with the required tie-breaking. If no valid point exists, `ans` remains minus one.

## Complexity detail

Let $n$ be the number of points. The loop visits each point once and performs a constant number of integer comparisons, subtractions, absolute values, and assignments. Total time is $O(n)$.

Only `ans`, `mi`, the current index, coordinates, and distance are stored. Auxiliary space is $O(1)$, matching the manifest.

The input point list is read without sorting or modification. Coordinate bounds keep arithmetic modest, though Python integers would handle larger values as well.

## Alternatives and edge cases

- **Sort valid candidates:** Sorting by `(distance, index)` is correct but costs $O(n\log n)$ time and extra storage.
- **Build a filtered list:** It makes validity explicit but uses $O(n)$ space that a streaming minimum avoids.
- **Check same x only:** It would miss valid points sharing y.
- **Check same y only:** It would miss valid points sharing x.
- **Use AND instead of OR:** It would accept only the identical location, which is too restrictive.
- **No valid points:** `ans` never changes and minus one is returned.
- **Exact same location:** Distance zero is valid and cannot be beaten.
- **Several zero-distance duplicates:** The earliest index remains because updates are strict.
- **Equal nearest distances:** Scan order plus strict comparison keeps the smallest index.
- **Later smaller distance:** It replaces the earlier farther point even though its index is larger.
- **Valid vertical point:** `a == x` and distance reduces to `abs(b-y)`.
- **Valid horizontal point:** `b == y` and distance reduces to `abs(a-x)`.
- **Point sharing both coordinates:** Both validity clauses are true, but it is still processed once.
- **Positive coordinate bounds:** They are irrelevant to the logic; only differences matter.
- **Input preservation:** Enumeration reads points in their original order, which is essential for implicit tie handling.
