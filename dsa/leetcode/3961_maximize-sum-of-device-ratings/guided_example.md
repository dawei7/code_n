# Guided Example: Maximize Sum of Device Ratings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"units": [[1, 3], [2, 2]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `units` of size `m × n` where $\text{units}[i][j]$ represents the capacity of the $j^{\text{th}}$ unit in the $i^{\text{th}}$ device. Each device contains **exactly** `n` units.

The objective is to compute `4` from `{"units": [[1, 3], [2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the one-unit case is separate

When `n=1`, each device contains only its current minimum. Donating that only unit empties the source, whose rating becomes zero. The receiver gains another unit, but its new minimum cannot exceed its old rating. Therefore an operation cannot compensate for the rating lost by the emptied source. Since operations are optional, performing no transfers is optimal.

The source returns



which is the original rating sum in this case.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"units": [[1, 3], [2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What one donation can do when there are at least two units

For `n \ge 2`, a source remains nonempty after donating once. If it removes one occurrence of its minimum `a_i`, its smallest remaining original unit is `b_i`. This is true even when the two smallest values are equal: then `a_i=b_i`, and removing one minimum correctly leaves another equal minimum.

No sequence of allowed operations can make device `i`'s final rating exceed `b_i`. The device can remove at most one of its own original units, so at least `n-1` original units remain. The smallest of those remaining originals is at most the original second-smallest value `b_i`. Receiving more units cannot increase a minimum.

Thus `\sum_i b_i` is a natural upper bound if every device could independently reach its second minimum. The transfers cannot quite realize all of those upper bounds at once, because every removed unit must be placed somewhere.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why one device must absorb the global minimum

Consider the globally smallest original unit value `A`. There are two possibilities:

- its owner does not remove that occurrence, so the owner's final rating is at most `A`; or
- its owner removes it, in which case some other device receives it and that receiver's final rating is at most `A`.

Either way, at least one device, call it `j`, has final rating no greater than `A`. For all other devices, the general upper bound `b_i` still applies. Therefore

$$
\text{final sum}
\le
\sum_{i\ne j}b_i+A
=
\sum_i b_i-b_j+A.
$$

Since `b_j \ge B`, this is at most

$$
\sum_i b_i-B+A.
$$

This proves that no arrangement can exceed the expression computed by the source. It also explains why the globally smallest first minimum and the globally smallest second minimum are the only two cross-device values needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"units": [[1, 3], [2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Linear scan for the smallest two values:** Each row's first and second order statistics can be found in one pass without sorting. That would achieve `O(U)` time, `O(1)` explicit auxiliary space, and no input mutation. It is a stronger implementation choice, but it is not what the exact stored source does.
- **Simulating all transfers:** Trying source, destination, and moved-unit combinations obscures the minimum structure and grows combinatorially. The upper-bound-and-construction argument reduces the optimization to two order statistics per device plus two global minima.
- **Sending donations to several receivers:** Spreading small donated values risks lowering several device ratings. Concentrating all donated minima in the one deliberately sacrificed sink confines that damage to a single rating.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `m` be the number of devices, let `n` be the number of units in each device, and let
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
