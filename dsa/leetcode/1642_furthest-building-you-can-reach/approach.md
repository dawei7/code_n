## General

**Spend ladders on the most expensive climbs**

Only positive height differences consume resources. A descent or equal-height move is free. Among the positive climbs needed to reach a fixed prefix, ladders should cover the largest ones and bricks should cover the smaller ones.

The exchange argument is simple. Suppose an allocation uses a ladder on a climb of size $x$ but bricks on a larger climb of size $y>x$. Swapping the ladder to $y$ and paying $x$ bricks instead saves $y-x$ bricks without using another ladder. Therefore an optimal allocation can always place ladders on the largest climbs encountered.

The source maintains exactly that allocation online with a min-heap `h`.

**Temporarily give every new climb a ladder**

The loop examines each edge from building `i` to `i+1`. It computes `d = b - a`. When `d <= 0`, the move is free and no heap or resource value changes.

For a positive `d`, the source pushes it into `h`. Conceptually, every climb in the heap currently receives a ladder.

If the heap size is no greater than `ladders`, all heap climbs can indeed be covered by available ladders, so no bricks are spent.

If pushing creates more heap entries than ladders, one climb must switch to bricks. `heappop(h)` removes the smallest climb among those tentatively assigned ladders, and that amount is subtracted from `bricks`.

After this pop, the heap contains the largest at most `ladders` climbs seen so far. Every other positive climb in the processed prefix has been paid with bricks.

**Why the heap may revise an earlier decision**

Suppose one ladder was used on an earlier climb of 3 and the current climb is 8. Pushing 8 creates heap `[3,8]`. If only one ladder exists, popping 3 means retroactively paying 3 bricks and moving the ladder to 8.

If the current climb were 2 instead, pushing gives `[2,3]` and popping 2 means paying bricks for the current climb while leaving the ladder on 3.

The same code handles both cases. No explicit “is the current climb larger?” branch is needed because the min-heap chooses the cheapest climb to remove from ladder coverage.

**Detect the first impossible edge**

After paying the newly determined smallest non-ladder climb, the source checks whether `bricks < 0`. If so, the available bricks cannot cover all climbs not assigned ladders in the prefix through edge `i`.

At this point the heap already represents the brick-minimizing placement of every available ladder. Any other ladder allocation would require at least as many bricks by the exchange argument. Therefore no resource rearrangement can cross from building `i` to `i+1`, and the furthest reachable building is `i`.

Returning immediately is valid because travel is sequential. A later building cannot be reached without crossing this failed edge first.

If every edge is processed without making bricks negative, every required climb has a valid ladder-or-brick assignment, so the final building index `len(heights) - 1` is reachable.

**Trace the first example**

For heights `[4,2,7,6,9,14,12]`, five bricks, and one ladder:

- Difference $2-4$ is negative, so building 1 is free.
- Climb $7-2=5$ enters the heap. One ladder can cover it.
- Difference $6-7$ is negative.
- Climb $9-6=3$ enters the heap. There are now two climbs for one ladder, so pop 3 and spend three bricks. The ladder remains on 5.
- Climb $14-9=5$ enters the heap. Pop one of the 5s and attempt to spend five more bricks. Only two remain, so bricks become negative and the algorithm returns index 4.

One could instead put the ladder on the later size-5 climb, but the earlier size-5 climb would still cost five bricks. The tie does not alter reachability.

**The maintained invariant**

After each successfully crossed edge:

- `h` contains the largest $\min(\ell,c)$ positive climbs seen so far, where $\ell$ is the ladder count and $c$ is the number of climbs;
- those heap climbs are assigned ladders;
- `initial_bricks - bricks` is the sum of all remaining positive climbs.

Pushing a new climb and popping the minimum when necessary preserves exactly the largest-$\ell$ set. Since using ladders on that set minimizes brick cost for the prefix, non-negative remaining bricks prove the prefix reachable, while negative bricks prove it unreachable.

This invariant establishes the returned furthest index.

## Complexity detail

Let $n$ be the number of buildings and $\ell$ the number of ladders. The loop considers $n-1$ edges. Each positive climb is pushed once. Whenever heap size exceeds $\ell$, one item is popped. The heap contains at most $\ell$ items after an iteration and at most $\ell+1$ momentarily, so each heap operation costs $O(\log(\ell+1))$.

Total time is $O(n\log(\ell+1))$. This notation also handles $\ell=0$ cleanly: the heap temporarily holds one item and operations are constant time.

The intended heap storage is $O(\ell)$. However, the exact source iterates over `heights[:-1]`, and Python slicing constructs a new list of $n-1$ height references. Consequently, this checked-in implementation's actual peak auxiliary space is $O(n+\ell)=O(n)$, not only the manifest's `O(\ell)`. Replacing the slice with `range(len(heights)-1)` or `pairwise(heights)` would restore the heap-dominated $O(\ell)$ bound.

The heap stores integer climb sizes, and the algorithm does not store which particular edge received each ladder because only sizes affect resource feasibility.

## Alternatives and edge cases

- **Max-heap of brick-paid climbs:** Initially pay every climb with bricks. When bricks become negative, replace the largest brick payment with a ladder. This is the symmetric greedy solution with similar complexity.
- **Binary search the reachable building:** For a candidate prefix, select its largest ladder-covered climbs and test brick cost. Repeating prefix checks adds complexity and usually more total work.
- **Sort all climbs for every prefix:** It can identify optimal allocation but repeatedly sorting produces excessive time. The heap updates the allocation incrementally.
- **No ladders:** Every positive climb is immediately popped and paid with bricks; the heap remains empty after each iteration.
- **No bricks:** The journey succeeds through at most the climbs covered by ladders. The first required brick payment makes the count negative.
- **More ladders than positive climbs:** Every climb remains in the heap and no bricks are spent.
- **Descending or equal buildings:** Non-positive differences are free and never enter the heap.
- **Equal climb sizes:** Either equal climb can receive the ladder; only total brick cost matters.
- **Failure on edge `i`:** Building `i` is reachable but `i+1` is not, so returning `i` is the correct zero-based index.
- **Single building:** The sliced loop is empty and the only building, index 0, is returned.
- **Python slice storage:** `heights[:-1]` is an avoidable $O(n)$ copy that makes the exact space usage larger than the abstract heap algorithm.
