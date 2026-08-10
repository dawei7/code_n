## General

**Why a greedy choice is not obviously safe**

The multiplier attached to a node is its one-based position. A larger score generally benefits from appearing later, but precedence constraints can force nodes early or make placing one node unlock several others. Choosing the smallest available score at every step may look attractive, yet local score alone does not describe the future set of available nodes.

The small limit `n <= 22` allows the source to explore all relevant subsets of already placed nodes while merging different orders that lead to the same subset.

**Encode prerequisites with bitmasks**

Each node corresponds to one bit. For edge `source -> target`, the source sets:

`prerequisites[target] |= 1 << source`.

After all edges, bit `u` is set in `prerequisites[v]` exactly when `u` is a direct predecessor of `v`.

Given a mask of already placed nodes, node `v` is available when:

- its own bit is not in `mask`;
- every prerequisite bit is already in `mask`.

The second test is:

`mask & prerequisites[v] == prerequisites[v]`.

Requiring direct predecessors is sufficient. Every graph edge is represented directly, and if each appended node waits for all its incoming neighbors, the complete sequence respects every edge. Transitive dependencies are enforced through the chain of direct edges.

**Define the subset-DP state**

`dp[mask]` is the maximum profit among all valid topological prefixes whose placed-node set is exactly `mask`.

All nodes in `mask` occupy the first `popcount(mask)` positions, although their internal order may differ. Crucially, every such order has the same next position:

`popcount(mask) + 1`.

The empty prefix has profit zero:

`dp[0] = 0`.

Other entries begin at `-1` to mean unreachable. Scores and positions are positive, so every real profit is nonnegative and cannot be confused with that sentinel.

**Why the subset alone contains enough future information**

Suppose two valid prefix orders place the same subset `mask` but earn different profits. Their future possibilities are identical:

- they have the same unplaced nodes;
- a node's availability depends only on whether its prerequisite bits belong to `mask`;
- every future node receives the same sequence of remaining position numbers.

Therefore, the smaller-profit prefix can never catch up by making a future choice unavailable to the larger-profit prefix; both can make exactly the same choices from now on. It is safe to keep only the maximum profit for each subset.

This dominance property is the optimal substructure behind the DP.

**Organize states by prefix length**

The source uses `valid_masks` rather than scanning all `2^n` masks during every length. Initially it contains only zero.

The outer loop variable `placed` runs from zero through `n-1`. At its start, every mask in `valid_masks` contains exactly `placed` nodes and represents at least one valid topological prefix.

For each mask, the source tries every node. If it is unplaced and all prerequisites are present, appending it creates:

`next_mask = mask | (1 << node)`.

The node occupies one-based position `placed + 1`, so the candidate profit is:

`dp[mask] + (placed + 1) * score[node]`.

The maximum candidate is stored in `dp[next_mask]`.

**Avoid processing the same subset more than once in the next layer**

Many different valid prefixes can reach the same `next_mask`. The source appends it to `next_valid_masks` only when:

`dp[next_mask] == -1`.

On the first discovery, the state is added to the next layer and then assigned a candidate. Later discoveries update its DP value if better but do not append a duplicate.

This is safe because the entire current layer finishes before `valid_masks` is replaced. By the time the next outer iteration processes `next_mask`, every incoming transition from the preceding layer has had a chance to maximize its value.

**Why every valid topological order is represented**

Take any valid topological order. Its first node has no unmet prerequisite, so the transition from mask zero can append it. Assume the DP can reach the subset formed by the first `p` nodes. The next node's every predecessor occurs earlier in the valid order, so all its prerequisite bits are in that subset and the DP allows the next transition.

By induction, the DP contains the mask of every prefix of every valid topological order, including the full mask. The accumulated transition values equal the order's exact profit.

Conversely, the DP appends a node only after all incoming predecessors are placed, so every generated sequence is a valid topological order. It never evaluates an invalid order.

**Why the maximum is returned**

For each reachable mask, transitions consider every legal choice for the next position and retain the best accumulated profit. The dominance argument proves that discarding lower-profit orders with the same mask cannot remove an optimal completion.

At the full mask `(1 << n) - 1`, all nodes have been assigned positions. `dp[-1]` is Python indexing for this final array entry. Since the graph is guaranteed acyclic, at least one full topological order exists, so this state is reachable. Its stored value is the maximum profit over all valid orders.

**A small branching example**

For edges `0 -> 1` and `0 -> 2`, only node zero is available at the empty mask. After placing zero at position one, nodes one and two are both available.

If their scores are six and three, placing node two at position two and node one at position three gives:

`score[0] * 1 + 3 * 2 + 6 * 3`.

The alternate branch gives six the smaller multiplier. Both transitions are explored, and the full-mask DP entry keeps the better one.

## Complexity detail

There are `2^n` possible masks. Each reachable mask is placed in exactly one layer according to its number of set bits and processed once. Processing a mask scans all `n` nodes and performs constant-time bit operations per node. The worst-case time is `O(n * 2^n)`.

Building prerequisite masks costs `O(E)` for `E` edges, with `E <= n(n-1)/2`, and is dominated by subset DP at the maximum `n`.

The `dp` array has `2^n` entries. The current and next valid-mask lists can also contain `O(2^n)` states in the widest layers. Total auxiliary space is `O(2^n)`.

For `n = 22`, the DP array has 4,194,304 entries, so the asymptotic strategy is appropriate only because of the small node limit. Python object storage gives this a significant practical memory constant.

## Alternatives and edge cases

- **Greedy smallest available score first:** It often delays large scores, but unlocking effects can make a local choice globally suboptimal. Subset DP evaluates every feasible choice sequence.
- **Enumerate all permutations:** There are `n!` possible orders before even checking edges. Subset merging reduces the state space to `2^n`.
- **Backtracking without memoization:** Different orders repeatedly reach the same placed subset. Memoizing only the best profit for that subset is the decisive improvement.
- **Standard topological sort:** Kahn's algorithm finds one valid order, not necessarily the profit-maximizing one.
- **Store the full prefix order in the state:** Future feasibility depends only on the subset, and current profit summarizes the past objective contribution. The order itself is unnecessary.
- **No edges:** Every subset is reachable. The optimum places scores in non-decreasing order so larger scores receive larger multipliers, and the DP discovers that ordering.
- **A total chain:** Only one node is available at each step, so exactly one mask per layer is processed and the unique topological order is returned.
- **Multiple prerequisites:** The bitwise equality requires all bits, not merely one predecessor.
- **Node with no prerequisites:** Its prerequisite mask is zero, so the containment test succeeds whenever it is unplaced.
- **Disconnected DAG components:** Nodes from different components may interleave freely; the DP explores all profitable interleavings.
- **Duplicate routes but no duplicate edges:** Transitive relationships do not need extra handling; every direct edge is enforced.
- **Positive scores:** They make `-1` a safe unreachable sentinel. The same recurrence could support zero scores, but negative scores would require a different sentinel.
- **Full-mask access:** `dp[-1]` refers to the last list element, which is exactly mask `2^n - 1`.
- **DAG guarantee:** Without it, the full mask might remain unreachable and returning `-1` would expose invalid input rather than a meaningful profit.
