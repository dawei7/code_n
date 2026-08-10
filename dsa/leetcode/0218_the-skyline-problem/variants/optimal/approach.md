## General

**A skyline can change only at a building boundary**

Between two consecutive building edges, the set of rectangles covering the
ground does not change. Therefore the visible maximum height is constant on
that open horizontal interval. A key point can occur only at some building's
left edge, where a rectangle begins, or right edge, where one stops
contributing.

The exact solution collects both coordinates from every building in `lines`
and sorts that list. It deliberately keeps duplicate coordinates. Processing a
coordinate more than once is harmless because the output logic suppresses an
unchanged height; retaining duplicates avoids a separate set construction.
There are only $2n$ entries for $n$ buildings.

The input guarantee that `buildings` is already sorted by non-decreasing left
coordinate is essential to the `city` pointer. As the sweep visits boundary
coordinates from left to right, `city` identifies the first building not yet
inserted into the active priority queue.

**What it means for a building to be active**

A building `[left, right, height]` contributes at coordinate $x$ exactly when

$$
\texttt{left} \le x < \texttt{right}.
$$

The left edge counts, so every building whose left coordinate is at most the
current `line` must be inserted before measuring the height there. The right
edge does not count, so a building whose right coordinate is at most `line`
must be ignored before measuring.

The loop
`while city < n and buildings[city][0] <= line` inserts all newly started
buildings. Since the building list is left-sorted, once the first not-yet-added
building starts after `line`, every later one does too, and the loop can stop.
Each building is inserted exactly once, and `city` never moves backward.

**Use a min-priority queue as a max-height structure**

Python's `PriorityQueue` returns the lexicographically smallest stored entry.
The source stores each building as
`[-height, left, right]`. A taller positive height has a more negative first
field, so the smallest entry corresponds to the greatest height. Thus
`-pq.queue[0][0]` is the current visible height once expired entries at the top
have been removed.

The `left` and `right` fields break ties between equal heights. Their exact tie
order does not affect the visible maximum; the right coordinate is also needed
to decide whether the top building has ended. The source peeks through
`pq.queue[0]`, the internal list used by `PriorityQueue`, rather than calling a
public peek method because that class does not expose one.

If no active building remains, the visible height is ground level 0.

**Lazy deletion is sufficient**

A normal heap efficiently removes only its top entry. When a shorter building
ends while a taller building still covers the sweep position, the ended
building may be buried inside the heap and cannot be removed cheaply. The
solution leaves it there temporarily.

This stale entry cannot corrupt the skyline while it is buried: some entry
above it has at least as much height and is the one determining the visible
contour. Before reading the maximum at every coordinate, the source repeatedly
checks the top building's right edge. While `pq.queue[0][2] <= line`, that top
entry no longer covers the current coordinate and `pq.get()` removes it. If
another expired entry becomes the new top, the loop removes that one too.

The loop ends only when the heap is empty or its tallest entry is still live.
Therefore the remaining top is exactly the tallest active building, even if
irrelevant expired entries remain deeper in the heap. Every stale item is
eventually removed if it rises to the top, or remains permanently harmless
under an equal-or-taller live item until a later sweep position.

**Order at a shared coordinate handles starts and ends correctly**

Several buildings may start or end at the same x-coordinate. At the first
iteration for that coordinate, the insertion loop adds every building with
`left <= line`, including all buildings beginning exactly there. The expiration
loop then removes top entries with `right <= line`, including all ended
buildings as they reach the top. The height is measured only after both kinds
of update.

This ordering matches the half-open interval rule. A building that ends at
`x` is absent at `x`, while one that begins there is present. It also prevents
an unnecessary ground-level point between two touching buildings. For
`[[0,2,3],[2,5,3]]`, the second height-3 building is inserted and the first is
expired at coordinate 2; the measured height remains 3, so no point `[2,3]` is
added. The skyline changes to 0 only at coordinate 5.

Because `lines` contains duplicates, the same `line` may be processed again.
No new building then satisfies the insertion pointer, and the top has already
been cleaned for that coordinate. The computed height repeats and the output
check skips it.

**Append a key point only when the visible height changes**

After cleaning the heap, `high` is either the negative of the top entry's
stored negative height or 0 for an empty queue. If the last point in `skys` has
that same height, the horizontal skyline segment simply continues, so the
method executes `continue`. Otherwise it appends `[line, high]`.

This rule guarantees there are no consecutive segments with equal height. It
also means multiple boundary events at the same x-coordinate yield at most one
meaningful key point: after the first fully processed occurrence, later copies
see no height change.

At the rightmost building edge, every building has been inserted and every
remaining entry has `right <= line`. Repeated top removal empties the queue,
`high` becomes 0, and the final drop `[rightmost, 0]` is appended unless it was
already represented. Because the input contains at least one positive-height
building, the final drop is present as required.

**Why the resulting contour is exact**

At each processed boundary `line`, all buildings starting at or before it have
entered the heap, and no future-starting building has entered. Lazy cleanup
ensures the top among these entries has right edge greater than `line`.
Consequently `high` is the maximum height among exactly the buildings covering
that coordinate.

No coverage set changes between this boundary and the next distinct boundary,
so that maximum remains the skyline height throughout the interval. Appending
only when this maximum differs from the preceding value records precisely the
left endpoint of each new horizontal segment and no redundant point. Since all
possible change coordinates are in `lines`, no key point can be missed.

**Trace the beginning of the main example**

At coordinate 2, building `[2,9,10]` is inserted. It is live, so the first key
point is `[2,10]`. At coordinate 3, `[3,7,15]` enters. Its stored height `-15`
outranks `-10`, raising the visible height and adding `[3,15]`.

At coordinate 5, the height-12 building starts, but height 15 remains taller,
so no point is appended. At coordinate 7, the height-15 top has ended and is
removed. The height-12 building is now the tallest live one, producing
`[7,12]`. At coordinate 9, the ended height-10 building may still exist below
the active height-12 entry, but it cannot influence the top and needs no
immediate arbitrary-position deletion. At coordinate 12, expired entries are
removed as they reach the top, the heap becomes empty, and `[12,0]` is emitted.

The source imports `PriorityQueue` directly but expects `List` to be available
from the surrounding execution environment.

## Complexity detail

Let $n$ be the number of buildings. Collecting `lines` takes $O(n)$ time and
sorting its $2n$ entries takes $O(n\log n)$ time. The sweep has $2n$
iterations. Each building is inserted once and removed at most once; each
priority-queue operation costs $O(\log n)$. All other sweep work is constant
per boundary occurrence, so total time is $O(n\log n)$.

The coordinate list contains $2n$ values, and the priority queue can contain
$O(n)$ live or lazily retained entries. The answer has at most $O(n)$ key
points. Excluding returned output, auxiliary space is $O(n)$; including it does
not change the bound.

## Alternatives and edge cases

- **`heapq` instead of `PriorityQueue`:** A plain heap list provides the same negative-height lazy-deletion algorithm with less synchronization overhead. `PriorityQueue` is thread-safe but the exact source peeks into its internal `.queue` list, so it already relies on implementation details.
- **Explicit start/end events with a multiset:** Add a height at every left edge and remove it at every right edge, then read the maximum. A balanced multiset supports arbitrary deletion but Python's standard library lacks a direct built-in version.
- **Divide and conquer:** Recursively compute skylines for building halves and merge two contour lists by x-coordinate while tracking both current heights. It also achieves $O(n\log n)$ time but requires careful equal-coordinate and redundant-height handling.
- **Coordinate compression with direct range updates:** Evaluate height on intervals between unique edges. A naive update touches many intervals per building and can degrade to $O(n^2)$ unless paired with a more advanced structure.
- **Several starts at one coordinate:** All are inserted before height measurement, so only their maximum can create the key point.
- **Several ends at one coordinate:** Expired top entries are repeatedly removed. A shorter expired entry may stay buried, but it cannot affect the current maximum and will be removed if it later surfaces.
- **A start and an end at the same coordinate:** The ending building is excluded and the starting building is included at that x, matching `[left, right)` coverage and avoiding a false intermediate gap.
- **One building:** Its left edge produces `[left,height]`; its right edge expires the only heap entry and produces `[right,0]`.
- **Nested buildings:** A shorter nested building never changes the contour while covered by a taller one. Lazy retention handles it without unnecessary output.
- **Equal-height touching or overlapping buildings:** The height-change check merges them into one continuous horizontal segment, as the note requires.
- **Gaps between groups:** When the previous active heap empties, a zero key point begins the ground segment. A later left edge raises the height again and creates another point.
- **Large coordinates and heights:** The algorithm compares Python integers and negates heights without overflow. It never allocates memory proportional to coordinate magnitude.
- **Input ordering:** The `city` pointer is correct because the reference guarantees non-decreasing left edges. With unsorted buildings, the method would need to sort them by left coordinate first.
