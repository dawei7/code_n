# Guided Example: Falling Squares

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"positions": [[1, 2], [2, 3], [6, 1]]}`
- **Required output:** `[2, 5, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are several squares being dropped onto the X-axis of a 2D plane.

The objective is to compute `[2, 5, 5]` from `{"positions": [[1, 2], [2, 3], [6, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Representing a square's footprint

An input pair `[l, w]` describes a square with left edge `l` and side length `w`. The code uses the inclusive integer interval

`[l, r]` where `r = l + w - 1`.

This encoding preserves the “side contact does not overlap” rule for integer coordinates. A square ending geometrically at coordinate `l+w` occupies encoded positions through `l+w-1`. Another square beginning at `l+w` starts at the next encoded position, so their query intervals do not intersect.

If two footprints overlap with positive width, their inclusive encoded ranges share at least one integer position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"positions": [[1, 2], [2, 3], [6, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What each segment-tree node stores

A `Node` represents an inclusive coordinate interval `[node.l, node.r]` and stores:

- `mid`, its midpoint;
- `left` and `right` children, created only when needed;
- `v`, the maximum surface height anywhere in the interval;
- `add`, a pending lazy assignment meaning the entire interval has that uniform height.

The field name `add` is slightly misleading: it is not an amount to add. It stores an assignment value.

The root covers `[1, 10^9]`. The tree does not allocate a billion leaves. Children are created by `pushdown` only along intervals reached by queries and updates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Querying the supporting height

`query(l, r)` returns the maximum stored height in the requested footprint.

If the current node is completely covered, `node.v` is already the answer for that component interval.

For partial coverage, `pushdown(node)` ensures children exist and propagates any pending uniform assignment into both children. The query then recurses only into children whose ranges intersect the requested interval and takes the maximum returned value.

An uncovered part of the domain effectively has height zero. The local accumulator `v` begins at zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 5, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"positions": [[1, 2], [2, 3], [6, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 5, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Coordinate compression plus array segment tree:** Collect every left endpoint and `left + size - 1`, map them to `O(N)` indices, and use a conventional lazy tree. This gives `O(N\log N)` time and `O(N)` space with less dependence on the numeric coordinate ceiling.
- **Quadratic simulation:** For each new square, compare it with every earlier square to find overlapping support. It is simpler and takes `O(N^2)` time, acceptable only for smaller inputs.
- **Touching side edges:** `r = l + w - 1` ensures adjacent intervals do not overlap merely because one geometric right edge equals another left edge.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log C)$. Let `N` be the number of squares and let `C = 10^9` be the fixed root-domain width.
- **Auxiliary Space Complexity:** $O(N\log C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
