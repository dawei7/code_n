## General

**There are at most two useful jumps from one index**

For the first jump rule, `nums[i] \le nums[j]` and every intermediate value must be strictly below `nums[i]`. Therefore, `j` must be the first index to the right whose value is at least `nums[i]`. If a nearer such index existed, it would be an intermediate value violating the strict-below condition.

For the second rule, `nums[i] > nums[j]` and every intermediate value must be at least `nums[i]`. Thus, `j` must be the first index to the right whose value is strictly smaller than `nums[i]`.

So the complete outgoing jump set has at most two edges: the next greater-or-equal boundary and the next strictly-smaller boundary.

**Find the next greater-or-equal boundary**

The first right-to-left monotonic-stack pass pops while

`nums[stk[-1]] < nums[i]`.

Those smaller values are permitted intermediates for the first rule, so they are skipped. When popping stops, the stack top, if present, is the nearest rightward value at least as large as `nums[i]`. The code appends that index to `g[i]`.

Any popped index cannot be the first-rule destination for `i` because its value is too small. Any farther qualifying destination is blocked by the nearer retained boundary.

**Find the next strictly-smaller boundary**

The second pass pops while

`nums[stk[-1]] >= nums[i]`.

These greater-or-equal values are permitted intermediates for the second rule. The first remaining stack top is strictly smaller and becomes the second possible edge.

Again, a farther smaller destination would have this nearer smaller value as an intermediate, violating the requirement that all intermediates be at least `nums[i]`.

**Why equality differs between the stacks**

For the first rule, equality is allowed at the destination, so equal values must remain and can be selected. That pass pops only strictly smaller values.

For the second rule, the destination must be strictly smaller, while equal values are allowed only as intermediates. That pass pops greater-or-equal values.

These exact inequalities mirror the two source conditions and prevent losing or inventing jumps around duplicate values.

**Build a forward acyclic graph**

Every stored edge goes from `i` to a strictly larger index `j`. The dictionary `g` therefore represents a directed acyclic graph already ordered by index.

There is always at least an adjacent jump when another index exists: for two adjacent values, either the first is no greater than the second or it is greater, and there are no intermediate positions to violate the chosen rule.

Thus, the destination is reachable and forward dynamic programming can process indices from zero upward.

**Define minimum landing cost**

`f[i]` is the minimum cost required to reach index `i`. The start has `f[0]=0` because no jump lands there. Other entries begin at infinity.

For every edge `i\to j`, landing at `j` costs `costs[j]`, so relaxation is

`f[j] = min(f[j], f[i] + costs[j])`.

The departure index's cost is not charged. If several routes reach `j`, the minimum keeps the cheapest.

**Why one forward pass is sufficient**

Every predecessor of `j` has a smaller index. By the time the outer loop reaches `j`, all incoming edges have already been relaxed from their processed origins.

There is no need for repeated relaxation, a priority queue, or topological sorting: numerical index order is already a topological order.

**Trace the first example structurally**

From value three at index zero, the next greater-or-equal boundary is value four at index two, creating the jump costing six. The next strictly-smaller boundary is value two at index one, creating the alternative costing seven.

Subsequent boundary edges allow index two to reach index four at added cost two, for total eight. The DP compares this with paths through the other generated edges and retains eight.

**Why the graph is complete and the DP is correct**

The boundary arguments prove every legal jump destination must be one of the two stack-discovered indices, and each discovered index satisfies its rule because all skipped intermediates have the required relation. Therefore, `g` contains exactly all useful legal edges.

On this forward DAG, the recurrence considers every path into each vertex and adds precisely the landing costs. Induction over index order proves `f[i]` is optimal, so `f[n-1]` is the requested minimum.

## Complexity detail

Each index is pushed and popped at most once in each monotonic-stack pass. Graph construction is `O(n)` time and stores at most two edges per index.

The DP scans those `O(n)` edges once, so total time is `O(n)`. The graph, two stacks over time, and distance array use `O(n)` auxiliary space.

For `n=1`, no edges exist and `f[0]=0` is returned.

## Alternatives and edge cases

- **Test every later index:** Verifying all possible jumps takes quadratic time and repeats boundary work.
- **Dijkstra's algorithm:** Edge costs are nonnegative, but the graph is already a forward DAG, so index-order relaxation is simpler and linear.
- **Build edges on the fly:** It can combine stack discovery and DP with careful ordering; the exact source separates graph construction from relaxation.
- **Pop equality in the first stack:** That would skip a valid equal destination.
- **Keep equality in the second stack:** That would choose an invalid destination that is not strictly smaller.
- **Adjacent values:** Exactly one rule always permits the adjacent jump.
- **Duplicate values:** They are valid destinations for the greater-or-equal rule and valid intermediates for the strictly-smaller rule.
- **Zero landing cost:** Relaxation handles it normally.
- **Cost at index zero:** It is never paid because the player starts there rather than jumping to it.
- **One element:** The minimum cost is zero.
- **Two edges to different boundaries:** Both are relaxed because either can lead to the optimal route.
- **Forward-only property:** It makes index order a valid topological order.
- **Input preservation:** Both arrays are read without modification.
