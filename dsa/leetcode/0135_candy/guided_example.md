# Guided Example: Candy

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ratings": [1, 0, 2]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

The objective is to compute `5` from `{"ratings": [1, 0, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the rule into two independent directions

Each child needs at least one candy. In addition:

- if `ratings[i] > ratings[i - 1]`, child `i` must receive more than the left neighbor;
- if `ratings[i] > ratings[i + 1]`, child `i` must receive more than the right neighbor.

Equal ratings impose no ordering requirement. Two equally rated neighbors may receive equal or different counts; minimizing the total normally lets both remain as low as their other constraints permit.

Trying to satisfy both directions in one left-to-right pass is difficult because a future decreasing run can force earlier children upward. The solution separates the two directions into `left` and `right` arrays, computes the minimum requirement from each side, and combines them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ratings": [1, 0, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the left array guarantees

Every entry begins at one, satisfying the universal minimum.

The forward loop starts at index one. When the current rating is greater than the previous rating, it sets:

`left[i] = left[i - 1] + 1`

Otherwise, `left[i]` remains one.

After this pass, `left[i]` is the smallest candy count that satisfies all comparisons with left neighbors within the prefix ending at `i`.

For an increasing run such as ratings `[1, 3, 5, 8]`, the required counts become `[1, 2, 3, 4]`. Each step must exceed the previous one by at least one, and using exactly one more is minimal. When the rating stops increasing, the current child has no obligation to exceed the left neighbor, so restarting at one is the cheapest possible choice under the left-only rules.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every entry begins at one, satisfying the universal minimum.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the right array guarantees

The backward pass is the mirror image. It starts at index `n - 2` and moves left. When `ratings[i] > ratings[i + 1]`, it sets:

`right[i] = right[i + 1] + 1`

Otherwise, the entry stays one.

Thus `right[i]` is the smallest number satisfying every comparison with right neighbors in the suffix beginning at `i`.

For a decreasing rating run `[8, 5, 3, 1]`, the right requirements become `[4, 3, 2, 1]`. The high-rated child at the left end must stand above the whole descending chain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ratings": [1, 0, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One candy array and two passes:** Build left r:** - **One candy array and two passes:** Build left requirements in one array, then scan right-to-left and raise an entry with `max(current, right-neighbor + 1)` when needed. It uses $O(n)$ space with one array.
- **Slope counting:** Track lengths of increasing and decreasing rating runs and add triangular-number contributions. It achieves $O(1)$ auxiliary space but peak and plateau accounting is easier to get wrong.
- **Repeated relaxation:** Start everyone at one and repeatedly repair violated neighbor constraints until stable. It is intuitive but can require $O(n^2)$ time.
- **Priority queue by rating:** Process children from lower to higher ratings so lower-rated neighbor counts are known first. It works but adds $O(n\log n)$ sorting or heap cost.
- **One child:** Both arrays are `[1]`, so the result is one.
- **All ratings equal:** No strict comparison fires; everyone receives one and the result is $n$.
- **Strictly increasing ratings:** The minimum distribution is `1, 2, ..., n`.
- **Strictly decreasing ratings:** The right pass creates `n, ..., 2, 1`.
- **Valleys:** A local low point may remain at one even when both neighbors require larger counts.
- **Uneven peaks:** Taking the maximum, rather than adding directional counts, prevents double-counting the peak.
- **Runtime dependency:** The selected source uses `List` in its annotation without importing it. A standalone module needs `from typing import List`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of children.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
