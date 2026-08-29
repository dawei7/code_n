# Guided Example: Put Marbles in Bags

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"weights": [1, 3, 5, 1], "k": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `k` bags. You are given a **0-indexed** integer array `weights` where $\text{weights}[i]$ is the weight of the $i^{\text{th}}$ marble. You are also given the integer `k.`

The objective is to compute `4` from `{"weights": [1, 3, 5, 1], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A distribution is determined by its cut boundaries

The contiguity rule means splitting `weights` into `k` non-empty bags requires choosing exactly `k-1` cuts between adjacent marbles.

A cut after index `i` separates:

- a left bag ending with `weights[i]`;
- a right bag beginning with `weights[i+1]`.

Its variable contribution to total score is:

$$
\texttt{weights}[i]+\texttt{weights}[i+1].
$$

The source constructs all `n-1` adjacent boundary contributions with `pairwise(weights)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"weights": [1, 3, 5, 1], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Separate the fixed endpoint contribution

Regardless of cuts:

- the first marble is the first endpoint of the first bag;
- the last marble is the last endpoint of the final bag.

Their sum `weights[0]+weights[-1]` appears in every distribution score.

Every internal cut adds its two adjacent endpoint weights. Therefore:

$$
\text{score}
=
\texttt{weights}[0]+\texttt{weights}[n-1]
+
\sum_{\text{chosen cuts }i}
\bigl(\texttt{weights}[i]+\texttt{weights}[i+1]\bigr).
$$

When taking maximum score minus minimum score, the fixed outer-endpoint term cancels.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose smallest cuts for the minimum

Exactly `k-1` boundary values must be selected.

To minimize their sum, choose the `k-1` smallest contributions. If a chosen contribution were larger than an unchosen one, exchanging them would lower the score while preserving the number of cuts and validity.

After sorting `arr` ascending, these values are `arr[:k-1]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"weights": [1, 3, 5, 1], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Heaps for partial selection:** Find `k-1` smallest and largest without a full sort when `k` is small.
- **`k=1`:** No boundaries, so difference zero.
- **`k=n`:** All boundaries are forced, also giving zero.
- **Single-marble bag:** Its weight appears as both endpoints, correctly through adjacent cuts.
- **Repeated weights:** Boundary values may tie; any tied choices give the same score.
- **Fixed first and last weights:** They cancel from maximum-minus-minimum.
- **Exactly `k-1` cuts:** This enforces `k` non-empty bags.
- **Contiguous bags:** Every gap subset automatically preserves contiguity.
- **Large sums:** Use wide arithmetic.
- **Pairwise iterator:** It generates every adjacent boundary exactly once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Creating `n-1` adjacent sums costs $O(n)$. Sorting them costs $O(n\log n)$ and dominates. The two slice sums inspect $O(k)$ values.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
