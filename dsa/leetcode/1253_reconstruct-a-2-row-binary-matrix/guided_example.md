# Guided Example: Reconstruct a 2-Row Binary Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"upper": 2, "lower": 1, "colsum": [1, 1, 1]}`
- **Required output:** `[[1, 0, 1], [0, 1, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the following details of a matrix with `n` columns and `2` rows :

The objective is to compute `[[1, 0, 1], [0, 1, 0]]` from `{"upper": 2, "lower": 1, "colsum": [1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each column sum determines its possible shape

A binary column with two rows has only three cases:

- sum zero forces `[0,0]`;
- sum two forces `[1,1]`;
- sum one must be either `[1,0]` or `[0,1]`.

The two-row answer is initialized entirely to zero. The algorithm processes columns once, filling forced columns and greedily assigning sum-one columns while treating `upper` and `lower` as remaining row quotas.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"upper": 2, "lower": 1, "colsum": [1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Forced sum-two columns

For `v == 2`, both cells must be one. The code assigns both entries and decrements both row quotas.

No alternative exists. If either quota becomes negative, the requested row has already been forced to contain more ones than allowed, so no matrix can exist.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For `v == 2`, both cells must be one.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Flexible sum-one columns

A sum-one column contributes one remaining one to exactly one row. The code gives it to the row with the larger current quota:

- if `upper > lower`, place it in the upper row;
- otherwise, place it in the lower row.

When quotas tie, choosing lower is arbitrary; a symmetric choice of upper would also work.

The goal is to consume the larger outstanding requirement first and keep the residual quotas balanced. Future sum-two columns affect both quotas equally, so they do not change which quota is larger. Future sum-one columns supply the remaining individual choices.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 0, 1], [0, 1, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"upper": 2, "lower": 1, "colsum": [1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 0, 1], [0, 1, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Process all sum-two columns first:** Subtract :** - **Process all sum-two columns first:** Subtract their forced contributions, then distribute sum-one columns according to the residual upper count. This is equally linear and can simplify the feasibility formula.
- **Closed-form feasibility test:** After forced twos, require nonnegative quotas and require their sum to equal the number of ones in `colsum`.
- **All column sums zero:** A solution exists only when both requested row sums are zero.
- **Too many sum-two columns:** A quota becomes negative and the method returns empty.
- **Too few available ones:** Residual quota remains positive at the end and the final check fails.
- **Tied quotas:** Either row can receive the current flexible one; the exact source chooses lower.
- **Multiple valid matrices:** The contract permits any, so greedy need not reproduce an example’s layout.
- **Maximum length:** The one-pass method handles \(10^5\) columns without recursion.
- **Output space:** \(O(n)\) is unavoidable because a valid matrix itself contains \(2n\) entries.
- **Column values restricted to zero, one, or two:** The case analysis relies on this guarantee.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let \(n=\lvert\texttt{colsum}\rvert\). Initializing the two output rows takes \(O(n)\), and the loop performs constant work per column, giving \(O(n)\) time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
