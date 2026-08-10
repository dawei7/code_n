## General

A boomerang `(i, j, k)` is organized around its first point `i`. Once that pivot is fixed, the only requirement is that endpoints `j` and `k` lie at the same distance from it. This suggests handling one pivot at a time and grouping every possible endpoint by its distance from that pivot.

The order of the tuple matters. If two endpoints `A` and `B` are equally distant from pivot `P`, then `(P, A, B)` and `(P, B, A)` are two different boomerangs. The exact solution first counts each unordered endpoint pair once and doubles the total at the end.

**One distance counter for one pivot**

For each point `p1`, create a fresh `Counter` named `cnt`. Its key is a distance from `p1`, and its value is the number of points already seen at exactly that distance. Then scan every point `p2` and compute `d = dist(p1, p2)`.

Before inserting `p2`, suppose `cnt[d] = t`. There are exactly `t` earlier endpoints at the same distance from `p1`. Pairing the new `p2` with each one creates `t` new unordered endpoint pairs centered at `p1`. The code adds `t` to `ans`, then increments `cnt[d]` so that `p2` is available to pair with later endpoints.

This incremental rule is another way to compute a combination. If a distance group eventually contains $m$ points, its successive contributions are

$$
0+1+2+\cdots+(m-1)=\binom{m}{2}.
$$

That is the number of unordered ways to select two endpoints from the group. The scan avoids a separate second pass over all counter values because it adds each new pair at the moment its later endpoint is encountered.

**Why doubling gives ordered tuples**

Every unordered pair `{j, k}` around a fixed pivot corresponds to exactly two ordered tuples: `(i, j, k)` and `(i, k, j)`. No other ordering keeps the same pivot first. Therefore the number of ordered boomerangs is exactly twice the accumulated number of unordered endpoint pairs.

The expression `ans << 1` shifts the binary representation of the nonnegative integer `ans` one place left. For integers, this is exactly multiplication by two, so it converts the unordered-pair count into the required ordered-tuple count.

An equivalent direct formula for a distance group of size $m$ is $m(m-1)$: choose the second tuple position in $m$ ways and the third in $m-1$ ways. The implementation's incremental count obtains $\binom{m}{2}$ first and applies the factor of two only once at the end.

**A concrete trace**

Consider points `[[0,0], [1,0], [2,0]]`. Use `[1,0]` as the pivot.

- The pivot itself has distance `0`; no earlier point has that distance, so it adds nothing and makes `cnt[0] = 1`.
- `[0,0]` has distance `1`; it is the first endpoint in that group, so it adds nothing and makes `cnt[1] = 1`.
- `[2,0]` also has distance `1`. There is already one point in that group, so it adds one unordered pair and makes `cnt[1] = 2`.

The other two pivots have no distance group containing two non-pivot points. Thus `ans` is `1`, and shifting it left gives `2`: `([1,0], [0,0], [2,0])` and `([1,0], [2,0], [0,0])`.

The iteration order of `points` does not affect the result. Within a group of size $m$, whichever point is seen second contributes one, whichever is seen third contributes two, and so on. Their sum is always $\binom{m}{2}$.

**Why every boomerang is counted exactly once**

Take any valid tuple `(i, j, k)`. During the outer iteration for pivot `i`, endpoints `j` and `k` fall into the same distance group. Whichever endpoint appears later in the inner scan finds the earlier one in `cnt`, so their unordered pair contributes exactly once to `ans`. The final doubling accounts for both possible endpoint orders, including the original tuple.

The pair cannot be counted under another pivot because the outer loop's `p1` fixes the first tuple position. It cannot be counted twice for the same pivot because only the later endpoint creates that unordered pair. Conversely, the algorithm adds a pair only when both endpoints have the same distance key from the current pivot, so every counted pair really does generate two valid boomerangs.

**The pivot appears in its own inner scan**

The inner loop includes `p2 == p1`, whose distance is zero. This does not create an invalid tuple. All points are distinct, so the pivot is the only point at distance zero from itself. Its distance group has size one and contributes $\binom{1}{2}=0$. Avoiding a special conditional keeps the loop simple without changing the result.

The exact implementation uses `dist`, which computes Euclidean distance. Only equality between distances from the same pivot matters; their numerical magnitudes are never otherwise used. With the fixed two-dimensional integer inputs, equal geometric distances are grouped by their computed distance keys. A common variant uses squared distance `dx * dx + dy * dy`, which avoids square roots and keeps all keys integral, but the counting logic is identical.

## Complexity detail

Let $n$ be the number of points. The outer loop selects each of the $n$ pivots, and for every pivot the inner loop examines all $n$ points. Distance computation in two dimensions, counter lookup, addition, and counter update are constant-time operations. Total expected time is therefore $O(n^2)$, where “expected” reflects the usual expected $O(1)$ behavior of hash-table operations.

The counter is recreated for each pivot and can hold at most $n$ distinct distance keys. It is discarded before the next pivot's counter is built, so counters do not accumulate across outer iterations. Auxiliary space is $O(n)$.

The algorithm never stores triples or endpoint pairs. The integer `ans` and loop references use constant space in addition to the current counter. The output itself is a single integer.

## Alternatives and edge cases

- **Check every ordered triple:** Trying all distinct `(i, j, k)` tuples takes $O(n^3)$ time. Grouping endpoints by distance counts all choices for a pivot collectively and reduces this to $O(n^2)$.
- **Count full groups after the inner scan:** For each distance frequency $m$, adding $m(m-1)$ directly is equally valid. The exact solution instead accumulates unordered pairs online and doubles once at the end.
- **Use squared Euclidean distance:** The key `(x1 - x2) ** 2 + (y1 - y2) ** 2` avoids square roots and floating-point keys. It is often preferred in fixed-width languages, using a sufficiently wide integer type. The present solution uses `dist` but relies on the same grouping principle.
- **Use Manhattan distance:** This would change the problem. A boomerang is based on Euclidean distance, so points equal under Manhattan distance may not be geometrically equidistant.
- **One point:** Every distance group has size one, no endpoint pair exists, and the method returns zero.
- **Two points:** Each pivot has only one other endpoint, so no group can supply two distinct endpoints. The answer is again zero.
- **The pivot itself:** Its zero-distance group contains only itself because all input points are unique, so it never contributes a pair.
- **Several points on one circle around a pivot:** If $m$ points share that radius, they contribute $m(m-1)$ ordered boomerangs for that pivot, even if their coordinates or directions differ.
- **Same endpoint coordinates:** The contract forbids duplicate points. That guarantee ensures `j` and `k` are genuinely different points when two separate entries are selected and keeps the pivot's zero-distance group harmless.
