# Guided Example: Minimum Cost to Acquire Required Items

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cost1": 3, "cost2": 2, "costBoth": 1, "need1": 3, "need2": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given five integers `cost1`, `cost2`, `costBoth`, `need1`, and `need2`.

The objective is to compute `3` from `{"cost1": 3, "cost2": 2, "costBoth": 1, "need1": 3, "need2": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parameterize a plan by the number of shared items

Suppose exactly `x` type-3 items are bought. They contribute `x` units to both requirements. Any remaining shortage is filled most directly with one-sided items:

$$
C(x)=x\cdot\texttt{costBoth}
+\max(0,\texttt{need1}-x)\cdot\texttt{cost1}
+\max(0,\texttt{need2}-x)\cdot\texttt{cost2}.
$$

Because all costs are positive, buying more than `max(need1,need2)` shared items cannot help: both requirements are already met, and every extra item only increases cost.

The problem is to minimize this function over an enormous integer range, potentially up to $10^9$. The source evaluates only three meaningful breakpoints.

For a fixed `x`, the remaining one-sided purchase counts in the formula are forced in an optimum. Buying fewer would leave a requirement unmet, while buying more contributes beyond an already met requirement at positive cost. Thus `C(x)` really is the minimum plan among all plans with exactly `x` shared items.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cost1": 3, "cost2": 2, "costBoth": 1, "need1": 3, "need2": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Candidate A: buy no shared items

`a = need1 * cost1 + need2 * cost2`

is $C(0)$. Each requirement is met independently by its dedicated item type.

This is best when shared items are expensive compared with buying one item of each one-sided type.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `a = need1 * cost1 + need2 * cost2`

is $C(0)$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Candidate B: use shared items for the larger requirement

`b = costBoth * max(need1, need2)`

buys enough type-3 items to satisfy both requirements by itself. The smaller requirement may be exceeded, which is explicitly allowed.

This candidate matters when a shared item is even cheaper than satisfying the remaining one-sided units after the smaller requirement is filled.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cost1": 3, "cost2": 2, "costBoth": 1, "need1": 3, "need2": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Loop over every shared-item count:** Requireme:** - **Loop over every shared-item count:** Requirements reach $10^9$, so enumeration is far too slow.
- **Always buy `min(need1,need2)` shared items:** This ignores whether shared items are too expensive or cheap enough to justify oversupplying the smaller side.
- **Compare `costBoth` only with `cost1+cost2`:** That decides the overlap interval but not whether shared items should cover the larger-side remainder.
- **Require exact contributions:** The contract permits exceeding a need, which is why the all-shared candidate is legal.
- **Both needs zero:** Buying nothing gives cost zero.
- **One need zero:** Shared and one-sided items compete only for the nonzero requirement.
- **Equal needs:** The overlap and all-shared candidates coincide.
- **Shared cost equals both one-sided costs combined:** Every overlap count ties across the first interval; endpoint evaluation remains exact.
- **Shared cost equals one remaining side's cost:** Every oversupply count in the second interval ties.
- **Very expensive shared item:** The independent candidate wins.
- **Very cheap shared item:** Buying `max(need1,need2)` shared items may win.
- **Positive prices:** Buying beyond the larger need is never beneficial.
- **No input mutation:** All five arguments remain unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of multiplications, additions, minimums, and maximums independent of requirement sizes. Time is $O(1)$ and auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
