## General

**Maintain the answer instead of recounting it**

The array begins uncolored, represented by zeros. Each query assigns a positive color `c` to one index `i` and asks for the number of adjacent pairs whose two elements have the same nonzero color.

A direct implementation could apply a query and scan all $n-1$ neighboring pairs again. That would repeat almost the same work after every update.

Only one array position changes. Therefore only pairs touching that position can possibly change:

- the left pair between indices $i-1$ and $i$, when $i>0$;
- the right pair between indices $i$ and $i+1$, when $i<n-1$.

Every other pair has exactly the same two endpoint colors before and after the query. The solution keeps `x` as the current total and adjusts only these at most two local contributions.

**What counts as a contributing pair**

A pair contributes one precisely when:

1. both positions are colored, and
2. their colors are equal.

Since all assigned colors are positive and zero means uncolored, checking that the current color is nonzero distinguishes a real equal-colored pair from two uncolored zeros.

The solution stores current colors in `nums`. Before a query, `nums[i]` is the old color at the updated position and may be zero.

**First remove the old local contributions**

Before installing color `c`, the algorithm asks whether the old position currently forms a counted pair with each neighbor.

For the left side it checks:

`i > 0 and nums[i] and nums[i - 1] == nums[i]`.

The boundary test ensures the neighbor exists. `nums[i]` ensures the updated position was colored. Equality then proves the old left pair contributed one, so `x` is decremented.

The right-side condition is symmetric. After these two checks, `x` represents the total number of valid pairs that do not rely on the old color at index `i`.

This removal step must happen while `nums[i]` still contains the old color.

**Then add the new local contributions**

The algorithm next compares each existing neighbor directly with the new positive color `c`:

- if `i > 0` and `nums[i - 1] == c`, add one;
- if `i < n - 1` and `nums[i + 1] == c`, add one.

There is no separate nonzero test for `c` because the contract guarantees every query color is positive. If a neighbor equals `c`, that neighbor is therefore colored too.

At this point `x` already equals the answer after the recoloring, even though the physical assignment to `nums[i]` occurs a few lines later. The code records `ans[k] = x` and then executes `nums[i] = c` so future queries see the new state.

**Why recording before assignment is correct**

It can initially look backwards to store the result before writing the color. However, `x` is updated using the old value for removals and the explicit new value `c` for additions. The arithmetic has already simulated the state transition completely.

The assignment is necessary for later queries, not for the current result. No code between storing `ans[k]` and assigning `nums[i]` examines adjacency again, so this order is safe.

**Trace creation and destruction of pairs**

Suppose part of the color array is `[2, 0, 2]` and a query colors the middle position with 2.

The old middle value is zero, so neither old pair is removed. Both neighbors equal the new color, so the left and right pairs are added. `x` increases by two.

If a later query changes the middle position to 3, both old pairs satisfy the removal checks and `x` decreases by two. Neither neighbor equals 3, so nothing is added. Two local pairs disappear without inspecting any distant element.

**Recoloring to the same color still works**

Suppose `nums[i]` already equals `c`. Every matching old neighboring pair is first removed. The exact same neighboring pair is then added back because that neighbor also equals `c`.

The net change is zero. This uniform remove-then-add procedure avoids a special branch for “color did not change” while still preserving the correct total.

**The running invariant**

Before each query, `x` equals the number of indices $j$ such that positions $j$ and $j+1$ both have the same nonzero color in `nums`.

Removing the old contributions eliminates exactly the counted pairs whose truth value might be invalidated by changing position $i$. Adding the new contributions restores exactly the pairs that are true with color `c`. All unaffected pairs remain included exactly as before.

After `nums[i] = c`, the invariant holds for the new stored array. By induction over the query sequence, every appended answer is correct.

**Why there can be at most two changes**

Adjacency is a local relationship. Position $i$ is an endpoint only of pair $i-1$ on its left and pair $i$ on its right.

Even if the new color matches a long run of equal colors, the query does not suddenly create every pair in that run. Those pairs between unchanged positions were already counted. It creates only the links from the updated position to its immediate neighbors.

**Why this is optimal**

The algorithm must read each query and produce one output, so $\Omega(q)$ total work is unavoidable for $q$ queries.

Maintaining the running total uses constant work per query after an $O(n)$ color-array initialization. No method can asymptotically improve on processing each required query result.

## Complexity detail

Creating the length-$n$ color array takes $O(n)$ time. For each of $q$ queries, the algorithm performs at most four neighbor comparisons, a constant number of additions or subtractions, one output write, and one color assignment. Total time is $O(n+q)$.

The current color array uses $O(n)$ space and the required answer array uses $O(q)$ space. All counters and loop variables use $O(1)$ additional space, so total storage including output is $O(n+q)$.

## Alternatives and edge cases

- **Rescan every adjacent pair after each query:** Simple but costs $O(nq)$ time.
- **Store a Boolean for every edge:** This can also update two edges per query, but the single total `x` is sufficient and needs less state.
- **Segment tree:** It can maintain richer interval information, but it is unnecessary because the requested statistic changes locally and constant-time updates are possible.
- **First color at an index:** No old pair is removed because `nums[i]` is zero.
- **Recolor to the same color:** Old contributions are removed and identically restored, giving no net change.
- **Change the middle of a run:** Up to two equal pairs may disappear and up to two different pairs may appear.
- **Left endpoint:** Only the right pair exists.
- **Right endpoint:** Only the left pair exists.
- **Array of length one:** No adjacent pair exists, so every answer is zero.
- **Two uncolored neighbors:** Equal zeros never count because a contributing pair must be colored.
- **Positive color guarantee:** It makes direct neighbor comparison with `c` sufficient when adding new pairs.
- **Repeated queries at one index:** The stored assignment ensures every later query removes contributions of the latest color, not an older one.
