# Guided Example: Minimum Moves to Reach Target in Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sx": 1, "sy": 2, "tx": 5, "ty": 4}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given four integers `sx`, `sy`, `tx`, and `ty`, representing two points `(sx, sy)` and `(tx, ty)` on an infinitely large 2D grid.

The objective is to compute `2` from `{"sx": 1, "sy": 2, "tx": 5, "ty": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the larger coordinate identifies the last move

Suppose the current reverse state has `tx > ty`. The last forward move could not have increased the y-coordinate. A forward y-move from `(x,y)` produces:

`(x, y + max(x,y))`,

whose new y-coordinate is at least `x`. Such a result cannot have x strictly larger than y. Therefore, the last move must have increased x, while y remained `ty`.

The argument is symmetric when `ty > tx`: the last move must have increased y.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sx": 1, "sy": 2, "tx": 5, "ty": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reversing an x-increase

Let the predecessor be `(x, ty)` and the current larger coordinate be:

`tx = x + max(x, ty)`.

There are two cases.

If `x >= ty`, the maximum was x, so `tx = 2x`. The predecessor is `x = tx / 2`, which requires `tx` to be even. This case produces `tx >= 2ty`.

If `x < ty`, the maximum was `ty`, so `tx = x + ty`. The predecessor is `x = tx - ty`, and the resulting current ratio satisfies `ty < tx < 2ty`.

At the boundary `tx = 2ty`, subtraction gives predecessor `x = ty`, which is valid because `max(x,ty)=ty`. The source therefore uses:

- when `tx > 2 * ty`, require an even `tx` and halve it;
- otherwise, subtract `ty` from `tx`.

The y-larger branch applies the identical rules with the coordinates exchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let the predecessor be `(x, ty)` and the current larger coor... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an odd value above twice the other is impossible

When `tx > 2ty`, the subtraction predecessor `tx - ty` would still be greater than `ty`. If that predecessor were larger, the forward maximum would have been the predecessor itself, so the move should have doubled it rather than added `ty`. The only valid predecessor is `tx / 2`.

If `tx` is odd, no integer predecessor can double to it. The source immediately returns `-1`. The same reasoning handles odd `ty > 2tx`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sx": 1, "sy": 2, "tx": 5, "ty": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Forward breadth-first search:** It branches tw:** - **Forward breadth-first search:** It branches twice per state and is impractical on an unbounded grid with coordinates up to `10^9`.
- **Memoized forward recursion:** It still explores branching states and offers no advantage over the forced reverse predecessor.
- **Subtract repeatedly like the Euclidean algorithm:** The move rule sometimes doubles the current maximum; the ratio test and halving step are necessary to invert it correctly.
- **Start already equals target:** The loop does not run and the answer is 0.
- **Target coordinate below start:** The constraints exclude this initially, while the in-loop check rejects it if reverse processing overshoots.
- **Larger coordinate above twice the other and odd:** No integer doubling predecessor exists, so the target is unreachable.
- **Larger coordinate exactly twice the other:** The subtraction branch yields equal predecessor coordinates and represents a valid move.
- **Positive equal target coordinates:** The only predecessors have one coordinate zero.
- **Neither start coordinate is zero at equality:** No reverse path can reach that start, so the result is `-1`.
- **One start coordinate is zero:** It selects the corresponding equality predecessor without guessing.
- **Start `(0,0)` and positive target:** The forward maximum is always zero at the origin, so no move changes the point; reverse processing ultimately rejects the target.
- **Example `(1,1) -> (2,2)`:** Equality at the target requires a zero-coordinate predecessor, incompatible with the positive start, so the answer is `-1`.
- **Coordinates on an axis:** The nonzero coordinate can only double until the other coordinate becomes positive through a move that adds the maximum.
- **No mutation of caller data:** All parameters are immutable integers; the source rebinds local `tx` and `ty` only.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(log M)$. Let `M = \max(tx,ty)` for the original target. Each iteration performs constant-time comparisons and arithmetic and reduces the scale of the larger coordinate geometrically. The number of iterations is `O(\log M)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
