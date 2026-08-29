## General

**Turn the road into three tiny dynamic-programming states.** The frog moves through many points, but there are always exactly three lanes. That fixed lane count is the key simplification. After processing a point, the algorithm does not need to remember the complete route used to get there. It only needs three numbers:

- `f[0]` is the minimum number of side jumps needed to stand in lane 1 at the current point.
- `f[1]` is the corresponding minimum for lane 2.
- `f[2]` is the corresponding minimum for lane 3.

Each entry describes the best valid route ending in that lane, not one particular route. Keeping only the cheapest cost is safe because two routes that reach the same lane at the same point have exactly the same choices from then onward. The more expensive one can never become better later.

**Why the initial state is `[1, 0, 1]`.** At point 0, the frog starts in lane 2, so reaching lane 2 costs zero side jumps. It can also make one immediate side jump at point 0 to lane 1 or lane 3. The statement guarantees that point 0 has no obstacle, so both moves are legal. Consequently, the three best costs at the starting point are one, zero, and one.

**Process one road point at a time.** The loop visits `obstacles[1:]`, which represents points 1 through `n`. Let `v` be the obstacle value at the new point. A zero means all lanes are open; a value from one to three identifies the one blocked lane.

The first inner loop finds that blocked lane. If `v == j + 1`, lane `j + 1` cannot be occupied at this point, so the code sets `f[j]` to `inf`. Infinity is a useful impossible-state marker: it ensures that this lane cannot be selected as a cheapest valid source. The loop then breaks because the problem permits at most one obstacle at a point. When `v` is zero, no equality is found and all three old costs remain available.

This invalidation must happen before considering side jumps. A route that was cheap at the preceding point is irrelevant if moving straight into the current point would hit an obstacle. Setting its cost to infinity precisely removes that illegal continuation.

**The cheapest side jump at the current point.** After the blocked lane has been removed, the code computes

`x = min(f) + 1`.

The minimum is the cheapest cost among lanes that can legally reach this point. Adding one represents making one side jump at this same point. A side jump may go directly to either other lane; the destination does not have to be adjacent. Therefore every open destination lane can be reached with cost `x` from a cheapest open source lane.

There is a small but important reason that one shared value `x` works for all destinations. Suppose the lane attaining `min(f)` is also the destination currently being updated. Staying there costs `f[j]`, and `min(f) + 1` is merely one more, so taking the minimum keeps the cheaper stay-put cost. For either other open lane, `x` represents a genuine side jump from the cheapest lane. Thus the update

`f[j] = min(f[j], x)`

simultaneously chooses between continuing straight in lane `j + 1` and arriving there with one side jump. The code skips the blocked lane, so its infinity marker survives until the next point.

**Why no repeated relaxation is necessary.** One might wonder whether reaching one lane by a side jump and then using that newly improved value to jump again could help another lane. It cannot. Two side jumps at the same point cost two, whereas the frog can jump directly between any two lanes for a cost of one. The best source is already represented by `min(f)` before the destination updates begin. Computing `x` once also prevents update order from changing the result.

**A concrete trace.** For `obstacles = [0, 1, 2, 3, 0]`, the state starts as `[1, 0, 1]`.

- At point 1, lane 1 is blocked. Its state becomes infinity. The minimum open cost is zero, so the open states remain zero for lane 2 and one for lane 3.
- At point 2, lane 2 is blocked. The cheapest surviving cost is one in lane 3, so lane 1 can be reached with cost two. The useful finite states are now two in lane 1 and one in lane 3.
- At point 3, lane 3 is blocked. Lane 1 remains available with cost two, and lane 2 can be reached from it with one extra jump, although that extra move is not needed to achieve the final minimum.
- At point 4, no lane is blocked. The smallest state is still two, so the answer is two.

The state records costs rather than drawing the route, but it captures exactly the same decisions as the arrows in the example.

**Why returning `min(f)` is correct.** The required destination is point `n` in any lane. After the final loop iteration, each finite state is the minimum side-jump count for its particular final lane. Taking their minimum therefore chooses the cheapest permitted ending lane. Point `n` is guaranteed obstacle-free, so at least one state is finite.

The reasoning can be summarized inductively. Before an iteration, every state is the cheapest valid cost at the preceding point. Invalidation removes exactly the straight continuation blocked at the new point. For each open lane, the update then compares the only two useful ways to occupy it: stay in that lane, or make one direct side jump from the cheapest open lane. The resulting three states are therefore optimal at the new point. Since the initialization is optimal at point 0, the property remains true through point `n`.

## Complexity detail

Let `n = obstacles.length - 1` be the road length. The outer loop processes exactly `n` points. Each point runs two loops of at most three iterations, and `min(f)` also examines only three entries. Because three is a fixed constant rather than an input-dependent lane count, the dynamic-programming work is `O(n)` time.

The state array always contains exactly three costs, so the algorithmic dynamic-programming state is `O(1)` space. However, the exact Python expression `obstacles[1:]` creates a new list containing `n` elements before iteration. Consequently, this exact implementation has `O(n)` peak auxiliary space in Python even though the underlying rolling-state method needs only `O(1)`. Iterating by index or with an iterator over the suffix would preserve the same recurrence while avoiding that copy. The infinity value is only a sentinel and does not grow with the input.

## Alternatives and edge cases

- **Two-dimensional dynamic programming:** A table storing the best cost for every point and lane uses the same recurrence and is often easier to derive initially, but it consumes `O(n)` state even though only the previous point is needed.
- **Zero-one breadth-first search:** Treating each point-lane pair as a graph node, forward moves as weight zero, and side jumps as weight one also finds the optimum. It is substantially heavier than three rolling states for this fixed-width road.
- **Greedy reaction without lane costs:** Jumping only when the current lane becomes blocked is intuitive, but choosing the new lane based solely on the next obstacle can miss longer-range consequences. The three costs retain all relevant possibilities without guessing.
- **No obstacles:** Lane 2 keeps cost zero throughout, so the returned minimum is zero.
- **Obstacle in the currently cheapest lane:** That state becomes infinity before `min(f)` is computed, forcing the transition to use a genuinely reachable lane.
- **Obstacle value zero:** No state is invalidated; each open lane keeps its old cost unless one side jump from the cheapest lane is better.
- **Blocked destination during a side-jump update:** The condition `v != j + 1` prevents the algorithm from replacing the blocked lane’s infinity with a finite value.
- **Side jumps over nonadjacent lanes:** The single `min(f) + 1` transition is valid specifically because a side jump can go directly to any other lane.
- **First and last points:** The source guarantees no obstacle at either endpoint, which justifies the initial costs and guarantees a valid finite final state.
- **Python slicing detail:** The recurrence itself is constant-space, but `obstacles[1:]` copies the suffix. Replacing the slice with indexed iteration changes memory usage, not the algorithm or answer.
