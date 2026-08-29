## General

**View active ones as connected components**

At every step, positions whose bits are one form contiguous groups. Two active positions belong to the same group exactly when they are connected through adjacent active positions.

The source maintains these groups with a disjoint-set union structure. `vis[v]` says whether position `v` has already changed to one. `p` stores parent links, and `size[root]` stores the group length for each root.

Input positions are one-based, so every activated value is reduced by one before indexing the arrays.

**Activate one position and merge active neighbors**

When position `v` becomes one, it can connect to at most two existing groups: the active position immediately left and the active position immediately right.

If the left neighbor exists and is active, the source checks that neighbor component's size, then unites `v` with it.

It performs the analogous check and union for the right neighbor.

No other component can be affected because contiguous binary groups connect only through immediate adjacency.

Although `vis[v]` is marked true after these unions, `v` already has initialized parent `v` and size one. Union operations can therefore treat it as the newly created singleton component safely.

**Understand what ans records**

The subtle part is that the code checks a neighboring component's size before merging the new position into it.

If that existing component has size exactly `m`, it existed at the previous step but will cease to be a maximal size-$m$ group when the new adjacent one joins it. The current loop index is `i`, while the current activation step is one-based `i+1`.

Therefore the component's final valid step is the previous step, whose one-based number is exactly `i`. The assignment `ans = i` is not off by one; it intentionally records the last moment before destruction.

If both neighboring components have size `m`, they both disappear at the same activation and the same previous-step value is recorded.

**Why newly created groups need not be recorded immediately**

Suppose the current activation creates a new component of size `m`. The code does not set `ans` at that moment.

If `m < n`, the final state has one component of size `n`, so this size-$m$ group must eventually be extended or merged by a later adjacent activation. Immediately before that future activation, the pre-merge size check sees the component and records its last surviving step.

Thus the algorithm records a group's disappearance rather than its creation. That still captures its latest existence.

The one exception is `m == n`. The full-size group is created only at the final step and is never destroyed later. The source handles it before DSU processing by returning `n` directly.

**Path compression and component sizes**

`find(x)` follows parent pointers to the representative and compresses the path on return. Later queries for the same vertices become faster.

`union(a, b)` finds both roots. If distinct, it attaches root `pa` under root `pb` and adds `size[pa]` into `size[pb]`.

No union-by-rank heuristic is used, but path compression and the restricted number of adjacent unions keep the implementation efficient for the stated input.

Size is meaningful only at a current root. Every check therefore calls `find` before indexing `size`.

**Tracing the size-one example**

For activation order three, five, one, two, four with `m = 1`:

- After step one, position three is an isolated size-one group.
- After steps two and three, more isolated groups exist.
- At step four, position two activates beside groups at one and three. Before merging, the source sees size-one neighbors and sets `ans = 3`, the previous step.
- Position five remains an isolated size-one group through step four.
- At step five, position four activates beside the large left group and position five. The pre-merge check sees the right size-one group and sets `ans = 4`.

The returned value four is exactly the latest step containing a maximal group of one.

**Why every recorded group is maximal**

DSU components contain all active positions connected by adjacency. If an adjacent position were already active, it would have been unioned when the later of the two positions activated.

Therefore each component is a maximal contiguous run of ones, precisely matching the problem's group definition.

**Why the result is correct**

Every size-$m$ component with $m<n$ eventually disappears in a later merge. The source detects it immediately before that merge and records the exact last step when it existed.

Taking later assignments overwrites earlier ones, so `ans` becomes the latest disappearance time among all such components. If none ever exists, it remains negative one. The special full-length case covers the only component that can survive forever through the last step.

## Complexity detail

There are $N$ activations and at most two unions per activation. With path compression, DSU operations are near constant amortized; the conventional bound is $O(N\alpha(N))$, where $\alpha$ is the inverse Ackermann function.

The manifest simplifies this effectively linear behavior to $O(N)$. Because the exact union function does not use rank or size to choose its parent direction, the strongest textbook inverse-Ackermann guarantee is less direct; the practical operation count remains near linear for this adjacency workload.

Arrays `vis`, `p`, and `size` each contain $N$ entries, so auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Boundary-length array:** Store each active interval's length at both endpoints and update a count of size-$m$ groups in strict $O(N)$ time.
- **Reverse-time deletion:** Start with all ones and remove positions backward, tracking when a size-$m$ segment appears.
- **Rebuild the binary string each step:** It can cost $O(N^2)$.
- **m equals n:** The only qualifying group appears at final step, handled by the early return.
- **No qualifying group:** No pre-merge size check succeeds, so negative one remains.
- **New group of size m:** It is recorded later when destroyed, not at creation.
- **Group surviving to final state:** Only the size-$n$ group can do so.
- **Position zero:** The condition `if v` prevents a left-neighbor access outside the array.
- **Last position:** The explicit upper-bound condition prevents a right-neighbor access outside the array.
- **Two neighboring groups:** One activation can merge left component, singleton, and right component.
- **Permutation guarantee:** Every position activates exactly once, so no duplicate activation needs handling.
- **Root sizes:** `size` must be read through `find` because nonroot entries may be stale.
- **Step numbering:** Zero-based loop index `i` equals the previous activation's one-based step, which is exactly what destruction recording needs.
