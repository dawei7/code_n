# Guided Example: Minimum Number of Operations to Move All Balls to Each Box

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"boxes": "110"}`
- **Required output:** `[1, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` boxes. You are given a binary string `boxes` of length `n`, where $\text{boxes}[i]$ is `'0'` if the $i^{\text{th}}$ box is **empty**, and `'1'` if it contains **one** ball.

The objective is to compute `[1, 1, 3]` from `{"boxes": "110"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Split each target's cost into left and right contributions

Moving a ball from position `p` to target `i` costs `abs(p - i)` operations. Balls to the left contribute `i - p`, while balls to the right contribute `p - i`. A ball already at `i` contributes zero.

The exact solution builds:

- `left[i]`, the total distance from all balls strictly left of `i` to `i`.
- `right[i]`, the total distance from all balls strictly right of `i` to `i`.

The final answer at `i` is `left[i] + right[i]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"boxes": "110"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive the left-to-right recurrence

`left[0]` is zero because no box lies to the left of index zero. `cnt` tracks how many balls lie in positions already passed.

Before computing `left[i]`, the code checks `boxes[i - 1]` and increments `cnt` if that box contains a ball. At that moment, `cnt` is exactly the number of balls at indices less than `i`.

Imagine moving the target from `i - 1` one step right to `i`. Every ball on the left becomes one step farther away, so the total cost increases by the number of those balls. Therefore:

`left[i] = left[i - 1] + cnt`.

For example, if three balls lie to the left, shifting the destination right by one requires one additional move from each, adding three.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Derive the right-to-left recurrence

The second pass is symmetric. `right[n - 1]` is zero because no box lies to the right of the last index. `cnt` is reset to zero.

When computing `right[i]`, the source first includes a possible ball at `boxes[i + 1]`. `cnt` then equals the number of balls strictly right of `i`.

Moving the target from `i + 1` one step left to `i` increases every right-side ball's distance by one. Thus:

`right[i] = right[i + 1] + cnt`.

The loop moves from `n - 2` down to zero so the needed state `right[i + 1]` is already known.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"boxes": "110"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One combined bidirectional loop:** Accumulate left and right costs into one answer list in a single outer loop, reducing the number of full arrays while retaining $O(n)$ time.
- **Brute-force every target and ball:** Direct distance summation takes $O(n^2)$ time.
- **Prefix counts and position sums:** Mathematical prefix formulas also answer each target in $O(1)$ after linear preprocessing, but use similar storage.
- **No balls:** Both arrays remain zero and every answer is zero.
- **One ball:** Results are its distances to all target indices.
- **Ball at current target:** It contributes zero and is excluded from both strict-side counts.
- **Multiple balls after moves:** The calculation concerns the initial state independently for every target, so simulated states are irrelevant.
- **Single box:** Both passes are empty and the result is zero whether or not it contains a ball.
- **All boxes contain balls:** Counts grow on each pass, producing symmetric distance totals.
- **Reset cnt:** The right pass must start with zero; retaining the left count would corrupt all values.
- **Loop bounds:** The left pass begins at one and the right pass at `n - 2` because boundary costs are already zero.
- **Binary characters:** Comparing with `'1'` directly determines whether to increment the count.
- **Elementwise sum:** `zip(left, right)` aligns contributions for the same target index.
- **Input preservation:** No actual balls are moved and `boxes` is unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of boxes. The left pass, right pass, and final `zip` comprehension each visit $n$ entries with constant work. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
