# Guided Example: Sort Items by Groups Respecting Dependencies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "m": 1, "group": [0, 0, 0], "beforeItems": [[], [0], [1]]}`
- **Required output:** `[0, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` items each belonging to zero or one of `m` groups where $\text{group}[i]$ is the group that the `i`-th item belongs to and it's equal to `-1` if the `i`-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

The objective is to compute `[0, 1, 2]` from `{"n": 3, "m": 1, "group": [0, 0, 0], "beforeItems": [[], [0], [1]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Give every ungrouped item its own group

An item with group `-1` has no contiguity relationship with any other ungrouped item. The code assigns each such item a new unique group ID beginning at `m`. This allows the same group-level logic to handle it as a singleton block.

`group_items` has `n + m` slots, enough for the original groups plus at most `n` unique new ones. Original groups with no items and unused extra slots remain empty. The loop mutates the input `group` list while assigning IDs and records every item in its group’s list.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "m": 1, "group": [0, 0, 0], "beforeItems": [[], [0], [1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Separate internal and cross-group dependencies

For each item `i` and every prerequisite `j` in `beforeItems[i]`, the directed requirement is `j -> i`.

If `group[j] == group[i]`, both items will live in the same final block. The code adds `i` to `item_graph[j]` and increments `item_degree[i]`. This edge will be enforced by that group’s internal topological sort.

If their groups differ, every item in `j`’s group block must appear before every item in `i`’s group block for `j` to precede `i` while groups stay contiguous. The code adds a directed edge from `group[j]` to `group[i]` and increments the destination group’s indegree.

The same pair of groups may receive several edges from different item dependencies. The code retains those duplicate graph edges and increments indegree for each. During traversal, each stored edge produces one matching decrement, so correctness is preserved even without deduplicating group edges.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Topological sorting with indegrees

The helper receives a degree array, adjacency graph, and iterable of nodes to sort. It enqueues every supplied node whose indegree is zero. Removing such a node is safe because no unprocessed prerequisite remains. For each outgoing edge, it decrements the destination degree and enqueues that destination when the degree reaches zero.

If every supplied node is removed, `res` is a valid topological order. If fewer are removed, the remaining nodes participate in or depend on a directed cycle, so no valid ordering exists and the helper returns an empty list.

First, the solution topologically sorts all `n + m` possible group IDs. Empty groups simply behave as zero-indegree nodes with no output items. If the group graph has a cycle, contiguity makes the requirements impossible: each group in the cycle would need its whole block before the next.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "m": 1, "group": [0, 0, 0], "beforeItems": [[], [0], [1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Topologically sort all items then bucket by group:** This can also work when combined with a separate group order, but the exact solution avoids storing cross-group edges in the item graph because group ordering already enforces them.
- **Deduplicate group edges:** A set of group-pair edges can reduce repeated adjacency entries and indegree counts, potentially improving constants when many item edges connect the same groups.
- **Treat all ungrouped items as one group:** This is incorrect because it would force unrelated items to be contiguous. Each receives its own group.
- **Empty original groups:** They appear in group topological order but contribute no items, so they do not affect the final sequence.
- **Internal item cycle:** The per-group topological sort processes too few items and the method returns an empty list.
- **Cross-group cycle:** The group topological sort fails even if every group’s internal dependencies are acyclic.
- **No dependencies:** All indegrees are zero. Any group order and any internal item order are valid, and the method still emits contiguous groups.
- **Duplicate group-level edges:** They are safe because every increment has a corresponding stored edge and later decrement.
- **Input mutation:** Ungrouped assignments overwrite `-1` entries in `group`. Copy the list first if caller-visible preservation is required.
- **Any valid order accepted:** Queue order among simultaneously available nodes only chooses one of potentially many correct topological results.
- **Unused allocated group slots:** The `n + m` capacity simplifies indexing. Empty unused slots add only linear overhead and append nothing.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+G+E)$. Let $G=n+m$ be the number of allocated group slots and let $E$ be the total number of dependency entries across `beforeItems`.
- **Auxiliary Space Complexity:** $O(n+G+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
