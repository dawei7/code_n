# Guided Example: Minimum Cost for Cutting Cake I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 3, "n": 2, "horizontalCut": [1, 3], "verticalCut": [5]}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `m x n` cake that needs to be cut into `1 x 1` pieces.

The objective is to compute `13` from `{"m": 3, "n": 2, "horizontalCut": [1, 3], "verticalCut": [5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**A boundary may have to be cut more than once.** There are $m-1$ horizontal boundary lines and $n-1$ vertical boundary lines. Once vertical cuts divide the cake into several vertical pieces, applying one horizontal boundary across the original width requires a separate cut in every vertical piece. If there are currently `v` vertical pieces, choosing horizontal boundary cost $a$ adds $a\cdot v$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 3, "n": 2, "horizontalCut": [1, 3], "verticalCut": [5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Symmetrically, when there are `h` horizontal pieces, a vertical boundary of cost $b$ adds $b\cdot h$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The order matters because each cut increases the multiplier for every future perpendicular cut.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 3, "n": 2, "horizontalCut": [1, 3], "verticalCut": [5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over cut subsets:** For Cake I's tiny $m,n\le20$, richer DP is conceivable, but it ignores the exchange property and scales poorly compared with sorting.
- **Min-cost-first greedy:** Incorrect. Cheap early cuts increase the multiplier paid by later expensive perpendicular cuts.
- **One combined tagged list:** Store every cost with its orientation, sort globally descending, and update piece counts. This is equivalent but allocates an additional combined array.
- **Equal horizontal and vertical costs:** Either can go first; the source chooses vertical and remains optimal.
- **One row:** `horizontalCut` is empty, `h=1` throughout, and each vertical boundary is paid once.
- **One column:** The symmetric horizontal-only case is handled by stream exhaustion.
- **Both dimensions one:** Both arrays are empty, the loop never runs, and cost is zero.
- **Repeated costs:** Sorting retains all boundary occurrences; each boundary is still processed once.
- **Positive costs:** The exchange argument works cleanly, and no required cut should be omitted.
- **Piece counts, not completed cuts:** After $x$ horizontal boundaries have been processed, `h=x+1` horizontal pieces exist.
- **Short-circuit safety:** Exhausted-array checks must precede indexed comparisons.
- **Input mutation:** Both cost arrays are permanently sorted descending.
- **Constraint difference from Cake II:** This source and proof already scale beyond the small Cake I limits; the greedy rule does not rely on $m,n\le20$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Sorting $m-1$ horizontal costs takes $O(m\log m)$ time and sorting $n-1$ vertical costs takes $O(n\log n)$. The merge loop performs exactly $m+n-2$ selections, adding $O(m+n)$ time. Total time is $O(m\log m+n\log n)$.
- **Auxiliary Space Complexity:** $O(m + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
