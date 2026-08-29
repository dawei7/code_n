# Guided Example: Maximum Linear Stock Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"prices": [1, 5, 3, 7, 8]}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **1-indexed** integer array `prices`, where $\text{prices}[i]$ is the price of a particular stock on the $i^{\text{th}}$ day, your task is to select some of the elements of `prices` such that your selection is **linear**.

The objective is to compute `20` from `{"prices": [1, 5, 3, 7, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

**Rewrite the pair condition into an invariant.** For two consecutively selected one-based indices $a<b$, linearity requires

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"prices": [1, 5, 3, 7, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\texttt{prices[b]}-\texttt{prices[a]}=b-a.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

$$
\texttt{prices[b]}-b=\texttt{prices[a]}-a.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"prices": [1, 5, 3, 7, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over previous days:** It can test the linear relation pairwise but wastes $O(n^2)$ time when equality of one invariant solves the problem.
- **One-based key:** Using `price - (i + 1)` creates different numeric labels but exactly the same groups.
- **All keys equal:** Every day can be selected and the answer is the sum of all prices.
- **All keys distinct:** The best linear selection has one day, so return the largest individual price.
- **Positive-price guarantee:** It justifies including every member of a chosen group. Negative prices would require selecting a beneficial subset.
- **Repeated prices:** Equal prices at different indices usually have different keys; equality of price alone is not enough.
- **Large sums:** Use a wide integer type outside Python.
- **No reconstruction needed:** The problem requests only maximum score, so storing group totals is sufficient.
- **Dictionary default of zero:** Because every price is positive, a previously unseen invariant key may safely begin with total zero before the current price is added.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of days and $u$ the number of distinct invariant keys. The source scans once and performs expected constant-time hash updates, taking expected $O(n)$ time. Finding the maximum among $u$ totals costs $O(u)$, which is at most $O(n)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
