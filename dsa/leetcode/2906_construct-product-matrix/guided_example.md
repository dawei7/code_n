# Guided Example: Construct Product Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 2], [3, 4]]}`
- **Required output:** `[[24, 12], [8, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** 2D integer matrix `grid` of size $n * m$, we define a **0-indexed** 2D matrix `p` of size $n * m$ as the **product** matrix of `grid` if the following condition is met:

The objective is to compute `[[24, 12], [8, 6]]` from `{"grid": [[1, 2], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Flatten the matrix conceptually.** Row-major order lists cells as `grid[0][0]`, `grid[0][1]`, and so on through the final row. For any current cell, all other elements split into two groups: those before it in this order and those after it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 2], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If `prefix` is the product before the cell and `suffix` is the product after it, the required answer is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `prefix` is the product before the cell and `suffix` is t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\texttt{prefix}\cdot\texttt{suffix}\pmod{12345}.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[24, 12], [8, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 2], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[24, 12], [8, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Total product plus division:** Invalid under a:** - **Total product plus division:** Invalid under a composite modulus when current values lack modular inverses.
- **Separate prefix and suffix matrices:** Correct but wastes another $O(N)$ storage; the source stores suffixes in the output.
- **Single row or column:** Row-major traversal still acts like the standard one-dimensional except-self algorithm.
- **Factor equal to 12345:** It becomes zero modulo the modulus and is handled naturally.
- **Multiple modular zeros:** Any answer including one becomes zero; excluding one may still include another.
- **Minimum two cells:** Each output is simply the other value modulo 12345.
- **Large raw values:** Reducing after every multiplication keeps stored residues bounded.
- **Output-space convention:** Distinguish $O(N)$ returned storage from $O(1)$ extra working state.
- **Traversal order is part of the proof:** The reverse pass writes the product strictly after each cell, and the forward pass multiplies by the product strictly before it. Including the current factor in either update too early would violate the except-self requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=nm$ be the total number of cells. Two complete traversals perform constant work per cell, giving $O(N)$ time. Output matrix `p` contains $N$ values and uses $O(N)$ space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
