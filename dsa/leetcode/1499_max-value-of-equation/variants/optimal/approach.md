## General

**Removing the absolute value**

Points arrive in strictly increasing x-coordinate order. When an earlier point `i` is paired with the current point `j`, $x_i < x_j$, so

$$
\lvert x_i-x_j\rvert = x_j-x_i.
$$

The equation can be rearranged as

$$
y_i+y_j+x_j-x_i
=
(y_i-x_i)+(x_j+y_j).
$$

For a fixed current point, `x + y` is constant. The best eligible earlier point is therefore the one maximizing `y_i - x_i`, subject to `x - x_i <= k`.

The stored source represents the negative of that score in a min-heap. Each entry is `(x_i - y_i, x_i)`. The smallest first component corresponds to the largest `y_i - x_i`.

**Maintaining eligibility**

Before using the heap for current coordinates `x, y`, the loop checks its top entry. If `x - pq[0][1] > k`, that point is too far left and cannot form a valid pair now or with any later point. It is removed.

The while loop repeats because several expired points may rise to the top one after another. Once the heap is empty or its top point is within distance `k`, evaluation can proceed.

Expired entries that are not at the top may remain in the heap. This lazy deletion is safe. Only the top entry can influence the maximum calculation. If the top is valid, it already has the best score among every stored entry, so lower-priority expired entries are irrelevant. If an expired entry later becomes the top, the while loop removes it before use.

**Computing the current best pair**

When the heap is nonempty after expiration, its top supplies the minimum `x_i - y_i`. The source computes

`x + y - pq[0][0]`,

which equals

$$
x_j+y_j-(x_i-y_i)
=
y_i+y_j+x_j-x_i.
$$

That is precisely the original equation for this ordered pair. The value updates `ans` if it is the largest seen across all current points.

Only after evaluating pairs ending at the current point does the code push `(x - y, x)`. This order ensures that a point cannot pair with itself. It becomes a candidate only for later points, as required by $i<j$.

**Why the heap top gives the best eligible earlier point**

After the expiration loop, the top entry is valid. A min-heap guarantees that no stored entry has a smaller `x_i-y_i`. Negating this relationship means no stored point has a larger `y_i-x_i`. Thus the top maximizes the only earlier-point term in the rearranged expression.

Any valid pair has some later endpoint. When that endpoint is processed, its earlier point has already been pushed. If that earlier point is the best candidate, it is used; if another valid point has a better score, that alternative produces an equation value at least as large. Taking the maximum over all later endpoints therefore finds the global optimum.

Strictly increasing x-coordinates also make expiration permanent. Once `x_j-x_i>k`, every later x-coordinate is even farther from `x_i`, so removing it cannot discard a candidate needed later.

**The role of the guarantee**

`ans` starts at negative infinity because coordinates and equation values may be negative. The problem guarantees at least one eligible pair, so at some iteration the heap remains nonempty after expiration and `ans` receives a finite value. Without that guarantee, the method would return negative infinity rather than a problem-defined sentinel.

The names `heappush`, `heappop`, and `inf` must be available in the module environment, normally through imports from `heapq` and `math`.

## Complexity detail

Let $N$ be the number of points. Every point is pushed into the binary heap once. An entry is popped at most once. Each push or pop costs $O(\log N)$, and top inspection is constant time. Total time is therefore $O(N \log N)$.

The heap can hold $O(N)$ points when many remain within the distance window, so auxiliary space is $O(N)$.

The manifest states $O(N)$ time and $O(N)$ space. The space bound matches, but the time bound does not match the exact heap operations. A monotonic deque can maintain candidate scores in linear total time. Lazy expiration avoids unnecessary heap removals but does not make heap insertion constant time.

## Alternatives and edge cases

- **Monotonic deque:** Keep eligible points in decreasing order of `y_i-x_i` and increasing x order. Each point enters and leaves once, achieving the manifest's $O(N)$ time and $O(N)$ space.
- **Brute-force pairs:** Testing all earlier points for every current point costs $O(N^2)$ and ignores the rearranged separability.
- **Balanced search structure:** It can maintain scores with logarithmic operations like the heap, but usually adds implementation complexity.
- **Negative y-values:** Initializing with negative infinity is necessary because every valid equation value may be negative.
- **Distance exactly k:** The expiration test uses greater than k, so equality remains valid.
- **k equals zero:** Strictly increasing x-values allow no pair at distance zero; the existence guarantee therefore excludes such an effective test instance.
- **Several equal scores:** Any heap top with the minimum `x-y` gives the same optimal contribution.
- **Expired non-top entries:** They may remain temporarily but cannot affect the answer until reaching the top, when they are removed.
- **Self-pairing:** Pushing the current point after evaluation prevents using the same point twice.
- **Sorted input requirement:** Permanent expiration and the sign simplification rely on strictly increasing x-coordinates.
- **Missing imports:** A standalone file must provide `heappush`, `heappop`, and `inf`.
