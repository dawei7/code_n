# Guided Example: Count Integers in Intervals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["CountIntervals", "add", "add", "count", "add", "count"], "arguments": [[], [2, 3], [7, 10], [], [5, 8], []]}`
- **Required output:** `[null, null, null, 6, null, 8]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an **empty** set of intervals, implement a data structure that can:

The objective is to compute `[null, null, null, 6, null, 8]` from `{"operations": ["CountIntervals", "add", "add", "count", "add", "count"], "arguments": [[], [2, 3], [7, 10], [], [5, 8], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store coverage counts over an enormous coordinate domain

Intervals may use coordinates up to one billion, so an array with one entry per integer is not practical. The solution uses an implicit segment tree: each node represents a contiguous coordinate segment, but child nodes are created only when an operation needs to descend into that segment.

For every node, `v` is the number of covered integers in its inclusive range `[l, r]`. If the whole node range is covered, then

`v = r - l + 1`.

This aggregate lets a query return a segment's coverage count without visiting every coordinate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["CountIntervals", "add", "add", "count", "add", "count"], "arguments": [[], [2, 3], [7, 10], [], [5, 8], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the node fields

A `Node` stores:

- `l` and `r`, its inclusive coordinate boundaries;
- `mid = (l + r) // 2`, which divides the range;
- `left` and `right` child references, initially absent;
- `v`, the covered-integer count, initially zero;
- `add`, a lazy full-cover marker, initially zero.

`__slots__` fixes these attribute names and avoids a separate instance dictionary for every node, reducing the substantial per-node memory overhead of an implicit tree.

Only additions of coverage occur; no operation clears an interval. Therefore, `add = 1` means the entire segment has been covered and that fact may still need to be pushed to children. Zero means there is no pending full-cover propagation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use an almost-domain-sized root

The root represents `[1, 10^9 + 1]`, one coordinate beyond the legal input domain. Updates never include that extra coordinate, and `count()` queries only `[1, 10^9]`, so it never contributes to the returned count.

The extra endpoint is an implementation choice rather than a problem value. Because the query does not fully contain the root, counting descends along the boundary needed to exclude `10^9 + 1` instead of simply returning `root.v`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, 6, null, 8]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["CountIntervals", "add", "add", "count", "add", "count"], "arguments": [[], [2, 3], [7, 10], [], [5, 8], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, 6, null, 8]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Ordered disjoint intervals:** Maintain merged intervals in a balanced search tree and a running union length. It can be efficient, but Python lacks a built-in ordered map with the needed predecessor operations.
- **Coordinate array or bitset:** The one-billion-sized domain makes direct storage infeasible.
- **Coordinate compression:** All future endpoints are not supplied in advance to this online class, so static compression is inconvenient.
- **Dynamic interval union list:** A plain sorted list can require linear insertion and merging per add in the worst case.
- **Repeated identical interval:** Full-cover assignment is idempotent and does not increase the count twice.
- **Partially overlapping intervals:** Only previously uncovered coordinates increase ancestor counts.
- **Nested interval:** Adding a range fully inside existing coverage leaves the union count unchanged.
- **Adjacent intervals:** They cover distinct inclusive coordinates, and their lengths add correctly even without explicit interval merging.
- **Single-point interval:** `left == right` descends to or fully covers a segment representing one integer.
- **Full legal domain:** Adding `[1, 10^9]` covers every valid coordinate but not the root's extra `10^9+1`.
- **Count before many adds:** The query still returns the exact current union and may allocate a boundary path due to `pushdown`.
- **Lazy parent followed by partial access:** Propagation fills both children before recursion so existing coverage is preserved.
- **Inclusive endpoints:** Every fully covered node uses `r - l + 1`.
- **Extra root coordinate:** It is excluded explicitly by `query(1, 10^9)` and never appears in a public update.
- **No removal operation:** A one-valued lazy marker is sufficient because coverage never needs to be cleared.
- **Internal mutation during count:** Query allocation changes representation, not the logical set or returned count.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q \log U)$. Let `U = 10^9` be the coordinate range and `Q` the total number of operations. The tree height is `O(\log U)`, about 30.
- **Auxiliary Space Complexity:** $O(Q log U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
