## General

The process grows a set of points over a sequence of generations. At generation zero, the available points are exactly the points in `points`. To form the next generation, choose two distinct available coordinate triples and take their coordinate-wise midpoint, rounding each coordinate down:

$$
\left(
\left\lfloor \frac{x_1+x_2}{2} \right\rfloor,
\left\lfloor \frac{y_1+y_2}{2} \right\rfloor,
\left\lfloor \frac{z_1+z_2}{2} \right\rfloor
\right).
$$

The important timing rule is that a generation is simultaneous. A point first made in generation $g$ may participate only when generation $g+1$ is formed. It must not be used immediately to make another point in generation $g$. The source preserves that rule by keeping newly produced points in a separate set until the whole generation has been examined.

**Representing a point as an immutable value**

Python lists cannot be members of a set, so the source converts each three-coordinate list to a tuple. It creates:

- `known`, containing every distinct point available through the last completed generation;
- `frontier`, containing only the points first discovered in that last generation; and
- `produced`, containing new points being accumulated for the generation currently under construction.

The target is converted to a tuple for the same reason. The first test checks whether it is already in `known`. If so, its earliest generation is zero, and returning immediately is essential: rediscovering the same coordinates later would not change their first appearance.

**Why only pairs touching the frontier are needed**

A literal simulation could reconsider every pair in `known` during every generation. That would be correct, but most of its work would be repeated. Suppose a pair consists of two points that were both known before the current `frontier` was added. That exact pair was already available in an earlier generation. Its midpoint was therefore already considered. The midpoint either was already known or was added in an earlier generation; the same old pair cannot suddenly create a genuinely new point now.

Consequently, every point that can be new in the current generation comes from a pair containing at least one point in `frontier`. The outer loop therefore chooses `a` only from `frontier`. The inner loop chooses `b` from `available`, which is a tuple snapshot of all points in `known`. This examines every relevant pair while avoiding all pairs whose endpoints are both older than the frontier.

The snapshot also makes the generation boundary explicit. `available` is created before `produced` is merged into `known`, so a midpoint found during this pass cannot become an endpoint later in the same pass.

**Examining every relevant unordered pair exactly once**

There are two small conditions inside the nested loops:

1. If `a == b`, the pair is rejected because the operation requires two distinct coordinate triples.
2. If both `a` and `b` belong to `frontier`, the loops would otherwise see both orientations, $(a,b)$ and $(b,a)$. Tuple comparison gives a stable ordering. The condition `b in frontier and b < a` skips one orientation and retains the other.

When `a` is in the frontier and `b` is an older point, no symmetric duplicate exists: the older point can never be selected by the outer loop. Thus the ordering condition is applied only when `b` is also in `frontier`. Every useful unordered pair is considered once, and no useful pair is omitted.

For each retained pair, the code computes the three floored averages with integer division. It adds the result to `produced` only if that result is not already in `known`. Because `produced` is itself a set, several different pairs producing the same new point still create just one frontier entry.

**Returning the earliest possible generation**

The variable `generation` starts at one, matching the generation currently being built from the initial points. After all relevant pairs have been processed, the source tests whether the target is in `produced`. If it is, this is the first generation in which the target appears: it was not in `known` at the beginning of the pass, and generations are examined in increasing order. The algorithm can therefore return `generation` immediately.

If `produced` is empty, the closure has stabilized. Every pair of currently known points has already been considered, and none can add another point. Repeating the process would leave `known` unchanged forever, so an absent target is unreachable and the correct result is `-1`.

Otherwise, `produced` is merged into `known`, becomes the next `frontier`, and the generation counter advances. This maintains the exact meanings of both sets for the next pass.

Termination is guaranteed by the coordinate bounds. Every input coordinate lies from $0$ through $6$, and a floored average of two values in that interval remains in the same interval. There are therefore at most

$$
U \le 7^3 = 343
$$

possible coordinate triples. Every nonterminal pass adds at least one previously unknown triple, so the loop cannot continue indefinitely.

## Complexity detail

Let $n$ be the number of input points and let $U$ be the number of distinct points that are eventually known. Here $U\le 343$, although it is still useful to describe how work grows with $U$.

Building the initial set costs $O(n)$. Across the complete run, each relevant unordered pair is processed only when at least one of its endpoints has just entered the frontier. A pair of eventual points is never processed again in a later generation. There are at most $\binom{U}{2}$ such pairs, so midpoint computation and membership checks total $O(U^2)$ expected time with Python hash sets.

Creating an `available` tuple once per generation also copies known references. There can be at most $U$ productive generations and at most $U$ known points, so even its loose worst-case total is $O(U^2)$ and does not change the bound. Set updates and target checks add at most linear work per accumulated point. The complete time complexity is therefore $O(n+U^2)$.

The sets `known`, `frontier`, and `produced` collectively hold only points from the finite closure. `available` holds at most $U$ references. Although a point may temporarily occur in more than one of these containers, the number of stored entries remains $O(U)$. Thus the auxiliary space complexity is $O(U)$, aside from the input.

## Alternatives and edge cases

- **Recompute every pair after every generation:** This mirrors the definition directly and is a useful conceptual oracle, but it repeatedly examines old-old pairs. With as many as $U$ generations and $O(U^2)$ pairs per generation, a loose bound is $O(U^3)$ instead of the source's $O(U^2)$ total pair work.
- **Use newly found points immediately:** Updating `known` while iterating and allowing those points to participate in the same pass changes the meaning of a generation. It can report a target too early, so the separate `produced` set is not merely an implementation convenience.
- **Track derivation trees for every point:** Remembering every pair that can produce every midpoint is unnecessary when the requested output is only the earliest generation. The frontier level already records all timing information needed.
- **Target initially present:** The answer is `0` even if the target could also be generated later. The source handles this before initializing generation one.
- **Several pairs produce the same midpoint:** `produced` deduplicates the coordinate triple, so it is added once and receives one earliest generation.
- **Two equal endpoint values:** Even if duplicate input rows were supplied, converting to a set leaves one coordinate triple. The check `a == b` prevents using a point with itself, matching the requirement that the two triples be distinct.
- **Odd coordinate sums:** Python's `// 2` performs the required floor. Because all allowed coordinates are nonnegative, there is no negative-number rounding subtlety.
- **No point is produced:** An empty `produced` proves that the finite closure is complete. Returning `-1` is conclusive rather than an early guess.
- **Target appears alongside other new points:** Membership is checked after the full generation has been formed. The algorithm returns that generation without needing to merge the other new points, because only the target's earliest generation is requested.
