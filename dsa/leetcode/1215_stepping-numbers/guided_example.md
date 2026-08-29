# Guided Example: Stepping Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"low": 0, "high": 21}`
- **Required output:** `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **stepping number** is an integer such that all of its adjacent digits have an absolute difference of exactly `1`.

The objective is to compute `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]` from `{"low": 0, "high": 21}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Seed every positive one-digit stepping number

Every one-digit number is stepping because it has no adjacent digit pair that could violate the rule. The queue begins with `1` through `9` in increasing order.

If `low == 0`, the method appends zero to the answer before starting the positive-number generation. If `low > 0`, zero must not appear.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"low": 0, "high": 21}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate exactly the legal children

After removing value `v`, the code takes its last digit with `x = v % 10`.

When `x > 0`, appending `x - 1` creates `v * 10 + x - 1`. The new final digit differs from the old final digit by exactly one.

When `x < 9`, appending `x + 1` creates the other legal child.

At digit zero, only one is legal; at digit nine, only eight is legal. Every generated child remains a stepping number because all earlier adjacent pairs were already valid and the newly added pair is explicitly valid.

Conversely, remove the final digit from any multi-digit positive stepping number. The remaining prefix is a positive stepping number, and the removed digit must be one of exactly these generated children. Therefore, every positive stepping number is eventually generated once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the queue is numerically sorted

The seeds are increasing. Within one parent, the smaller legal child is enqueued before the larger child.

More importantly, every child of a smaller same-length parent is smaller than every child of the next larger parent. If `u < v`, then the largest child of `u` is at most `10u + 9`, while the smallest child of `v` is at least `10v`. Since `v >= u + 1`, `10v >= 10u + 10`.

Breadth-first processing also completes all shorter decimal lengths before longer ones, and every shorter positive integer is smaller than every longer positive integer. The queue therefore yields stepping numbers in increasing numeric order.

This ordering justifies `if v > high: break`. Once one dequeued value exceeds `high`, every remaining queued value is at least as large, so none can belong to the range.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"low": 0, "high": 21}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Depth-first generation plus sorting:** DFS can generate the same tree, but its natural order is not globally numeric and would require a final sort.
- **Scan every integer:** Testing all values from `low` through `high` wastes work when stepping numbers are sparse.
- **Digit dynamic programming:** It can count stepping numbers efficiently over much larger string bounds, but listing every answer still requires output-proportional work.
- **`low = 0`:** Zero is inserted once; it is never used as a leading-digit seed.
- **`high < 9`:** Ordered seeds cause an early break at the first value above the bound.
- **Last digit zero:** Only digit one may be appended, preventing a negative digit.
- **Last digit nine:** Only digit eight may be appended, preventing digit ten.
- **Inclusive endpoints:** Both `v >= low` and the pre-break `v <= high` logic include qualifying boundary values.
- **Sorted output:** BFS numeric ordering removes the need for a separate sort.
- **Unique generation:** Each number has exactly one parent formed by deleting its last decimal digit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $S$ be the number of stepping numbers from zero through `high`, inclusive.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
