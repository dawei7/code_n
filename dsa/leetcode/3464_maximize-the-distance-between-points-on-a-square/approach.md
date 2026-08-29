## General

**Turn the square boundary into a circular number line.** Let the square perimeter be $P=4\cdot side$. The protected source maps every boundary point to the clockwise distance from the bottom-left corner:

- on the left edge, $(0,y)$ maps to $y$;
- on the top edge, $(x,side)$ maps to $side+x$;
- on the right edge, $(side,y)$ maps to $3\cdot side-y$;
- on the bottom edge, $(x,0)$ maps to $4\cdot side-x$.

The `if`/`elif` order assigns each corner only once, while both adjacent formulas would give the same circular position there anyway. After sorting these coordinates into `nums`, moving forward in the array means walking clockwise around the boundary.

This reduction works because the answer is never larger than `side` when $k\ge4$. With more than four selected points, two must share an edge; with exactly four, either the four corners give minimum distance `side` or some same-edge/adjacent-edge pair gives no more. Points on opposite edges have Manhattan distance at least `side`, so for a tested distance $d\le side$ they can never be the violating pair. For points on the same or adjacent edges, the shorter relevant boundary separation equals their Manhattan distance. Consequently, requiring every cyclic gap between consecutive selected perimeter coordinates to be at least $d$ is sufficient and necessary for all selected pairs to have Manhattan distance at least $d$.

**Binary-search a candidate minimum distance.** If it is possible to select $k$ points with every pair at least $d$ apart, the same selection also works for every smaller distance. Feasibility is monotone, so the source binary-searches the largest feasible integer in $[1,side]$. It uses the upper midpoint

`mid = (l + r + 1) >> 1`

so that a feasible midpoint can safely assign `l = mid` without stalling. An infeasible midpoint assigns `r = mid - 1`. When both bounds meet, their common value is the maximum feasible distance.

The lower bound one is safe. Boundary points have unique integer coordinates, so their perimeter positions are distinct integers. Since at least $k$ points exist, any $k$ distinct positions have pairwise Manhattan distance at least one. Thus zero never needs to be represented.

**Test one distance while respecting the circular closing gap.** For a candidate `lo`, `check` tries every point as the first selected coordinate `start`. If the final selected coordinate is `last`, the clockwise wrap-around gap back to `start` is

$$
P-(last-start).
$$

It must be at least `lo`, which rearranges to

$$
last\le start+P-lo.
$$

The code stores that upper limit as `end = start + side * 4 - lo`.

Starting with `cur = start`, it selects the remaining $k-1$ points greedily. `bisect_left(nums, cur + lo)` finds the earliest available perimeter coordinate at least `lo` after `cur`. If no such coordinate exists, or if it lies beyond `end`, this start fails. Otherwise, that coordinate becomes the next `cur`.

There is no need to explicitly duplicate the coordinate array with values shifted by one perimeter. For a fixed original `start`, selection only moves to larger coordinates already present in `nums`. The `end` test encodes the one circular gap that crosses coordinate zero. Trying every possible original point as `start` covers every cyclic selection after rotating its order so that its smallest stored coordinate is first.

**Why choosing the earliest next point is optimal for a fixed start.** Suppose a feasible selection chooses some next coordinate $q$ at least `lo` after `cur`. The greedy choice $g$ is the first coordinate meeting that threshold, so $g\le q$. Replacing $q$ with $g$ cannot harm the gap from `cur`, and it leaves at least as much coordinate space for every later choice and for the final `end` limit. Applying this exchange after each selected point shows that if any sequence works from `start`, the greedy sequence works. Therefore, a greedy failure proves that no selection with that same start can work.

For a simple square of side two whose available boundary coordinates are `[0,1,2,3,4,5,6]`, testing `lo = 1` can choose any five successive distinct coordinates while leaving a wrap gap of at least one. Testing `lo = 2` cannot choose five points around a perimeter of eight because five required cyclic gaps would total at least ten. The feasibility check detects this through either a missing successor or the `end` bound.

**Why checking adjacent cyclic gaps is enough.** Order the selected points around the perimeter. Any nonadjacent pair has a boundary separation that contains at least one adjacent gap and therefore is no smaller than that gap along the relevant direction. Same-edge and adjacent-edge pairs have their Manhattan distance represented by the corresponding boundary separation. Opposite-edge pairs already have distance at least `side`, and every tested `lo` is at most `side`. Hence no untested nonadjacent pair can invalidate a selection whose cyclic adjacent gaps all pass.

The combined argument proves correctness: the perimeter mapping preserves every distance comparison that can limit the answer, `check` recognizes exactly whether $k$ suitably separated cyclic points exist for a fixed distance, and monotone binary search returns the greatest feasible distance.

**The protected checker differs from the manifest summary.** The manifest describes two-pointer successor construction plus binary lifting. This exact source does not build successor tables. It tries every start and performs one library binary search for each of the next $k-1$ points. That implementation is still practical because $k\le25$, but its exact time and space bounds must be stated from the code rather than from the different advertised technique.

## Complexity detail

Let $n$ be the number of given points. Mapping costs $O(n)$ and sorting `nums` costs $O(n\log n)$. One call to `check` tries all $n$ starts. For each start it performs at most $k-1$ calls to `bisect_left`, each costing $O(\log n)$, so one feasibility test costs $O(nk\log n)$.

Binary search performs $O(\log side)$ feasibility tests. The exact total time is

$$
O(n\log n+nk\log n\log side).
$$

This is not the manifest's $O(n\log n+n\log k\log side)$ bound, because no binary-lifting structure appears in the protected source.

The mapped coordinate array stores $n$ integers. Apart from it, the checker and binary search use scalar variables, so auxiliary space is $O(n)$, not the manifest's $O(n\log k)$. Python's sorting implementation may use linear temporary memory, which remains within $O(n)$.

## Alternatives and edge cases

- **Check every selected pair directly:** Pairwise distance evaluation makes a candidate subset expensive and does not solve the combinatorial selection problem.
- **Greedy without trying every start:** A line has a natural first point, but a circle does not; fixing the wrong start can violate only the closing gap and miss a feasible rotation.
- **Ignore the wrap-around gap:** Large separations between consecutive stored coordinates are insufficient if the last and first selected points are too close across the perimeter boundary.
- **Duplicate the perimeter array:** Appending every coordinate plus $P$ is a valid way to linearize circular windows, but the protected code instead uses `end` and original starts.
- **Two-pointer successors plus binary lifting:** This can accelerate repeated jumps and matches the manifest summary, but it is not the algorithm implemented in the protected source.
- **Opposite edges:** Their Manhattan distance is at least `side`, so they cannot violate any candidate distance in the searched range.
- **Corner points:** Branch precedence maps each corner consistently; adjacent edge formulas agree at the shared endpoint.
- **Exactly four corner points:** All four are selected and the minimum Manhattan distance is `side`, the search's upper bound.
- **Candidate distance one:** Unique integer boundary coordinates guarantee feasibility whenever at least $k$ points exist.
- **Repeated coordinates:** The input guarantees unique points, so the sorted perimeter coordinates are distinct despite corner branch choices.
- **Large side length:** The algorithm searches the numeric answer logarithmically rather than iterating through all distances up to $10^9$.
- **Small \(k\) bound:** Although the exact checker has a factor of $k$, the constraint $k\le25$ keeps that factor controlled.
