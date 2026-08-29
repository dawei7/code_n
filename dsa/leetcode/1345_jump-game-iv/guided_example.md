# Guided Example: Jump Game IV

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, you are initially positioned at the first index of the array.

The objective is to compute `3` from `{"arr": [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute equal-value destinations

`g = defaultdict(list)` maps each array value to all indices where that value occurs. The loop over `enumerate(arr)` appends every index to exactly one list.

For example, if a value occurs at indices one, two, and seven, `g[value]` is `[1, 2, 7]`. From any one of these nodes, all three list entries represent same-value jump destinations, although the current index itself will later be rejected as already visited.

This preprocessing avoids searching the full array whenever BFS needs equal-value neighbors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process one shortest-distance layer at a time

The queue starts with index zero, the visited set starts with zero, and `ans` starts at zero. At the beginning of each outer iteration, every index currently in `q` is reachable in exactly `ans` jumps.

The expression `for _ in range(len(q))` captures the current layer size before new nodes are appended. It processes exactly that many nodes. Any newly discovered neighbor goes to the back of the queue and waits for the next layer, where its distance will be `ans + 1`.

When a popped index equals `len(arr) - 1`, BFS has reached the target. Because layers are processed in increasing distance, no later path can use fewer jumps, so returning `ans` is optimal. For a one-element array, zero is already the last index and the method returns zero on the first pop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate all three neighbor types

The tuple `(i + 1, i - 1, *g.pop(arr[i], []))` combines the right neighbor, left neighbor, and every index sharing `arr[i]`. The starred expression expands the value’s list into the tuple.

Each candidate `j` must lie inside the array and not yet be visited. A valid new node is appended and immediately added to `vis`. Marking it at enqueue time is important: if several current-layer nodes can reach the same destination, only the first enqueue occurs, preventing duplicate work while preserving its shortest distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bidirectional BFS:** Search simultaneously from index zero and the last index, expanding the smaller frontier. It has the same $O(n)$ worst-case bounds and can reduce practical work.
- **Repeated equal-value scans:** Looking through the full array for matches at every node is correct but can take $O(n^2)$ time.
- **Keeping buckets after expansion:** Even with a precomputed map, scanning the same large list from every matching node can become quadratic. Removing the bucket is essential.
- **Current index inside its own bucket:** It is harmless because `vis` already contains it, so it is never enqueued again.
- **One-element array:** The starting index is the target, so zero jumps are returned.
- **First and last values equal:** The last index is discovered from the first bucket expansion and returned at distance one.
- **All values equal:** Every index is enqueued from index zero in one expansion; the answer is one when $n > 1$.
- **All values distinct:** Equal-value buckets add no useful move, and BFS reduces to walking through adjacent indices.
- **Negative values:** Dictionary keys support them exactly like positive values; only equality matters.
- **Out-of-bounds adjacent index:** The range test rejects `-1` and `n` candidates safely.
- **Mark on enqueue:** Delaying the visited mark until dequeue would allow the same index to enter the queue several times from one layer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
